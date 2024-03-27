import os
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 2-byte secret
secret = os.urandom(2)
flag = open('/home/ctf/flagQ3.txt', 'r').read().strip()

key = os.urandom(AES.block_size)

def printflag():
    print('977-213{'+flag+'}')

# ct = AES-128-ECB-Enc(key, pt)
def enc(pt):
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt, AES.block_size))
    res = ct.hex()
    return res

def main():
    print('Q3: ECB is bad. Recover the secret.')
    print('You are given an AES-128-ECB Oracle where output=AES-128-ECB-Enc(key,secret||input), where secret is 2 bytes. '
          'Enter plaintext in hexstr below. If you are ready to guess the secret, type "c": ')

    try:
        while(1):
            msg = input('$').rstrip()
            if msg == 'c':
                break
            msg = bytearray.fromhex(msg)
            pt = secret + msg
            ct = enc(pt)
            print(ct)

        print('Can you guess my 2-byte secret in hexstr? ')
        ans = input('$').rstrip()

        if ans == secret.hex():
            printflag()
        else:
            print('Wrong')
    except Exception:
        print('Dont try to hack my code!')

if __name__ == '__main__':
    main()
