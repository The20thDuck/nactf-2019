from Cryptodome.Util.number import bytes_to_long, long_to_bytes

f = open("rsa.txt", "r")
n = int(f.readline().split()[1])
d = int(f.readline().split()[1])
c = int(f.readline().split()[1])
print (long_to_bytes(pow(c, d, n)))