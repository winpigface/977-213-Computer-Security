import random
import sympy
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import json
import sys
from Crypto.Hash import SHA256
from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Util.Padding import pad

def fast_pow(a,b,p):
    if b < 10:
        return pow(a,b)%p
    if b%2 == 1:
        A = fast_pow(a, int((b-1)/2),p)
        return (A*A*a) % p
    A = fast_pow(a, int(b/2),p)
    return (A*A)%p

def share_key_to_AES_key(share_key):
    return SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder='big')).digest()


flag = open('/home/ctf/flagQ3.txt', 'r').read().strip()

def getflag():
    return '977-213{'+flag+'}'

def main():
    sys.setrecursionlimit(1500)
    print('Q3: Subgroup confinement attack. Slightly different from Q1 and Q2')
    print()
    g = 3
    p = 0xeaaad7fa50e8dca2204395316e33e3bacef0a88e29942c698cf2b054f5fc91ce1ed52c4bd3715b87dfddc5a5946476211402c6d12a9ff9678eacd091c08b3b25
    a = random.randrange(2, p-1)
    A = fast_pow(g,a,p)
    print('DHKE parameters (in hex):')
    print('Prime:', hex(p))
    print('Generator:', hex(g))

    B = int(input('Enter your public key (in int): ').strip())
    if not 1 < B < (p-1):
        print('Invalid public key')
        exit(1)

    share_key = fast_pow(B,a,p)
    key = share_key_to_AES_key(share_key)

    cipher = AES.new(key, AES.MODE_GCM)
    header = b'Decrypt this ciphertext to get the flag. encryption_key=SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder="big")).digest(), where share_key is a shared key created using DHKE and of int type. Encryption is done using AES256-GCM'
    msg = getflag()
    msg = str.encode(msg)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(msg)

    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag) ]
    result = json.dumps(dict(zip(json_k, json_v)))

    print()
    print('See header for instructions on how to get the flag')
    print()
    print(result)

if __name__ == '__main__':
    main()
