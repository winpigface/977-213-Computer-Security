import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

flag = open('/home/ctf/flagQ1.txt', 'r').read().strip()

def printflag():
    print('977-213{'+flag+'}')

def main():
    print("Q1: CBC mode of operation. "
          "Using Python's pycryptodome AES-CBC (https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode) "
          "implementation to encrypt .1MB of zeroes, i.e.: ")
    print("data = '\\x00'*int(1*10**5)")
    print("data = data.encode()")
    print()
    print("Please use 128-bit long zeroed key, use the following IV shown in hexstr below, and answer in hexstr: ")
   
    iv = os.urandom(AES.block_size)
    
    print("IV:", iv.hex())
    data = b'\x00'*int(10**5)
    key = b'\x00'*int(16)

    try:
        c = input('$').rstrip()
        c = bytes.fromhex(c)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        d = cipher.decrypt(c)
        p = unpad(d, AES.block_size)
        if p==data:
            printflag()
        else:
            print('Wrong')
    except Exception:
        print('Dont try to hack my code!')


if __name__ == '__main__':
    main()
