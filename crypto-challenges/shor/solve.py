from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from math import gcd

# egcd function and modinv from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



file_in = open("oligarchy.pem", "rb").read()
key = RSA.import_key(file_in)

n = key.n
e = key.e
f = open("are_you_shor.txt", "r")
a = int(f.readline().split()[1])
r = int(f.readline().split()[1])
c = int(f.readline().split()[1])

p = (gcd(pow(a, r//2, n)-1, n))
q = n//p
phi = (p-1)*(q-1)
d = modinv(e, phi)

priv = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(priv)
print (cipher.decrypt(bytes.fromhex(hex(c)[2:])).decode('utf-8'))
