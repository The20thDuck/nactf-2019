from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Hash import SHA
import random
#a = random.getrandbits(1023)
#key = RSA.generate(1024)
#print (key.e)
#print (key.p-1)
#print (key.q-1)
#p = key.p
#q = key.q
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

p = 9960790708615937009284515896420992382616146649424202003598709977705284731824391501396341958622537086351398446468676388585649433846248179850654716012602629
q = 13071851875798789997515167836941937732155195547529833929753754888425695318683119452480511389453222711440983256985153676220988126867480284802958736192638351
a = 84733215803103612460901465701232424798609470209825913961212238457798293111098195061837071495218083197429913141798442522950831495758395873695688189182925448736211066067276791533151828542439575601763801135131479532656528730453020404557236783254278625529895480234633323403399468237577058553920576024305830379725
n = p * q
e = 65537
phi = (p-1)*(q-1)
print ("n: ", n)
r = phi//6
#print ("r: {}".format(r))
#print (pow(a, r, n))
test = gcd(pow(a, r//2, n)-1, n)


message = b'nactf{d0wn_wi7h_7h3_0lig4rchy}'
h = SHA.new(message)
key = RSA.construct((n, e))
public_key = key.publickey().export_key()
file_out = open("oligarchy.pem", "wb")
file_out.write(public_key)
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
hexmessage = int(ciphertext.hex(), 16)
#print (hexmessage)

p = test
q = n//test
print ("n: ", p*q)
phi = (p-1)*(q-1)
d = modinv(e, phi)
priv = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(priv)
print (cipher.decrypt(bytes.fromhex(hexmessage)))

print ("n: {}".format(n))
print ("e: {}".format(e))
print ("a: {}".format(a))
print ("r: {}".format(r))