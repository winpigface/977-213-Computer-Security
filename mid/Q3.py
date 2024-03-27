from pwn import *
import re

io = remote('172.26.201.17',913)

q = io.recv().decode()
print(q)
iv_dic = {}
while True:
    plaintext = "aaa"
    io.sendline(plaintext.encode())
    text = io.recv().decode()
    ciphertext = re.findall(r'Ciphertext: (.*)',text)[0]
    IV = re.findall(r'IV: (.*)  Ciphertext:',text)[0]
    iv_dic[IV] = ciphertext
    if(len(iv_dic) == 4):
        break
print(iv_dic)
io.sendline(b'c')
text = io.recv().decode()
print(text)
encrypt_password = re.findall(r'encrypted password: (.*)',text)[0]
IV =re.findall(r'IV: (.*) , encrypted password:',text)[0]
print(IV)
ciphertext = iv_dic.get(IV)
print(ciphertext)
encrypt_OFB = bytes(a ^ b for a,b in zip(bytes.fromhex(str(ciphertext)),plaintext.encode()))
answer = bytes(a ^ b for a,b in zip(bytes.fromhex(encrypt_password),encrypt_OFB))
print(answer.decode())
io.sendline(answer)
print(io.recv().decode())
    


