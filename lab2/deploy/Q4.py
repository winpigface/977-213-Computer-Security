import os
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = os.urandom(AES.block_size)
iv = os.urandom(AES.block_size)
flag = open('/home/ctf/flagQ4.txt', 'r').read().strip()

def printflag():
    print('977-213{'+flag+'}')

# pt = AES-128-OFB-Enc(key, iv, pt)
def enc(pt):
    cipher = AES.new(key, AES.MODE_OFB, iv)
    ct = cipher.encrypt(pad(pt, AES.block_size))
    res = ct.hex()
    return res

# pt = AES-128-OFB-Dec(key, new_iv, ct)
def dec(ct, new_iv):
    new_iv = bytes.fromhex(new_iv)
    ct = bytes.fromhex(ct)
    cipher = AES.new(key, AES.MODE_OFB, new_iv)
    pt = cipher.decrypt(ct)
    try:
        pt = unpad(pt, AES.block_size)
    except Exception:
        pass

    return pt.decode('utf-8', errors="ignore")

def main():
    print('Q4: Encryption does not provide integrity!!')
    print('You intercept a string plaintext (1 line below), the corresponding (hexstr) AES-128-OFB ciphertext (2 lines below) and (hexstr) IV (3 lines below):')
    pt = b'Gimme 100 Baht'
    ct = enc(pt)
    print(pt.decode('utf-8'))
    print(ct)
    print(iv.hex())

    print('Enter a hexstring ciphertext and IV that will be decrypted by the receiver as "Gimme 900 Baht"')
    try:
        ansct = input('$').rstrip()
        ansiv = input('$').rstrip()
        pt_ans = dec(ansct,ansiv)
        if pt_ans == "Gimme 900 Baht":
            printflag()
        else:
            print('Wrong')
    except Exception:
        print('Dont try to hack my code')

if __name__ == '__main__':
    main()
