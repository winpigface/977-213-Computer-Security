from pwn import *
import re


io = remote('172.26.201.17',911)

q = io.recv().decode()
print(q)
cipher = re.findall(r'!\n(.*)',q)[0]
answer = ""
for key in range(1,26):
    for char in cipher:
        char_ord = (ord(char) - ord('a'))
        char_de = chr((char_ord - key) % 26 + ord('a'))
        answer += char_de
    if (answer == "fourthofjuly"):
        break
    else:
        answer = ""
io.sendline(answer.encode())
print(io.recv().decode())
        
