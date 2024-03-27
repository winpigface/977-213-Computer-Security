import os
import random
import time

flag = open('/home/ctf/flagQ6.txt', 'r').read().strip()

def getflag():
    return '977-213{'+flag+'}'

def encrypt(pt, otp):
    return bytes(a ^ b for a, b in zip(pt, otp))

def main():
    pt = open('/home/ctf/pt.txt', 'rb').read().strip()
    print("Just read the code")
    
    # How to get random otp? perhaps by the code below
    random.seed(0)
    otp = bytes(random.getrandbits(8) for i in range(len(pt)))
    ct = encrypt(pt, otp)
    print(ct.hex())

    flagb = str.encode(getflag())
    otp = bytes(random.getrandbits(8) for i in range(len(flagb)))
    ct = encrypt(flagb, otp)
    print(ct.hex())

if __name__ == '__main__':
    main()
