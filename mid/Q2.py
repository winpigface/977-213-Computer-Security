from pwn import *
import re

io = remote('172.26.201.17',912)

q = io.recv().decode()
print(q)
plaintext = re.findall(r'Plaintext \(in string\): (.*)',q)[0].encode()
IV = re.findall(r'IV \(in hex str\): (.*)',q)
IV1 = bytes.fromhex(IV[0])
IV2 = bytes.fromhex(IV[1])
ciphertext = re.findall(r'Ciphertext \(in hex str\): (.*)',q)
ciphertext1 = bytes.fromhex(ciphertext[0])
ciphertext2 = bytes.fromhex(ciphertext[1])

key = bytes(plaintext ^ IV ^ ciphertext for plaintext,IV,ciphertext in zip(plaintext,IV1,ciphertext1))

flag = bytes(ciphertext2 ^ key ^ IV2 for ciphertext2,key,IV2 in zip(ciphertext2,key,IV2))
print("flag:",flag)
io.sendline(flag)
print(io.recv().decode())


