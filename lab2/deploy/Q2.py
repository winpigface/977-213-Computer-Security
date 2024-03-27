import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

flag = open('/home/ctf/flagQ2.txt', 'r').read().strip()
nonce = os.urandom(8)

def printflag():
    print('977-213{'+flag+'}')


key = os.urandom(AES.block_size)

def main():
    print("Q2: Avoid reusing counter in CTR. You should never repeat the counter (nonce+monotonic counter) in CTR mode! "
          "2 ciphertexts encrypted using AES-128 in CTR mode are given below (in hex string): ")

    # load plaintexts
    pt1 = open('/home/ctf/pt1.txt', 'rb').read().strip()
    pt1 = pt1[:32]
    pt2 = open('/home/ctf/pt2.txt', 'rb').read().strip()
    pt2 = pt2[:32]

    # ct1 = AES-128-CTR-Enc(key, nonce, pt1)
    cipher1 = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ct1 = cipher1.encrypt(pt1)

    # ct2 = AES-128-CTR-Enc(key, nonce, pt2)
    cipher2 = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ct2 = cipher2.encrypt(pt2)
    print(ct1.hex())
    print(ct2.hex())

    print('Oops the first plaintext is leaked below: ')
    print(pt1.decode('utf-8'))

    print('Recover the second plaintext!')

    try:
        res = input('$').rstrip()
        pt2str = pt2.decode('utf-8')
        if res == pt2str:
            printflag()
        else:
            print('Wrong')
    except Exception:
        print('Dont try to hack my code!')

if __name__ == '__main__':
    main()
