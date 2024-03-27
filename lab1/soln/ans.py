from pwn import *


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


r = remote('localhost', 2222)


# Q1
r.recvuntil('"')
ct = r.recvuntil('"')[:-1].decode('utf-8')

r.recvuntil('=')
key = int(r.recvuntil('.')[:-1].decode('utf-8'))

pt = caesar(ct, 26-key)

print(ct, key, pt)
r.sendline(pt)

# Q2
r.recvuntil('"')
pt = r.recvuntil('"')[:-1].decode('utf-8')
r.recvuntil('"')
key = r.recvuntil('"')[:-1].decode('utf-8')

ct = ''
for i in range(len(pt)):
    ct += caesar(pt[i], ord(key[i])-ord('a'))

print(pt, key, ct)
r.sendline(ct)


# Q3
r.recvuntil('cipher: ')
ct = r.recvline().rstrip().decode('utf-8')
print('Q3', ct)
for i in range(0,26):
    pt = caesar(ct, i)
    if 'easy' in pt:
        print(pt)
        r.sendline(pt)
r.interactive()



