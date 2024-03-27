from pwn import *

r = remote('localhost', 1337)
r.interactive()
