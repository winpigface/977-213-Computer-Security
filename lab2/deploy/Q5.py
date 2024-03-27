from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import random

flag = open('/home/ctf/flagQ5.txt', 'r').read().strip()

def getflag():
    return '977-213{'+flag+'}'

DIGIT = '0123456789'

# key = 6 random digits padded to DES key size (64 bits or 8 bytes)
def generate_key():
    random_digits = ''.join(random.choice(DIGIT) for _ in range(6))
    random_digits = str.encode(random_digits)
    return pad(random_digits, 8)

key1 = generate_key()
key2 = generate_key()

# c = DES(key2, DES(key1, m))
def double_encrypt(m):
    m = str.encode(m)
    msg = pad(m, DES.block_size)

    cipher1 = DES.new(key1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)

    cipher2 = DES.new(key2, DES.MODE_ECB)
    return cipher2.encrypt(enc_msg)

def main():
    f = getflag()
    c = double_encrypt(f)
    print('Q5: 2DES=DES. Heres the flag encrypted using 2DES. Each key is 6-random digits padded to DES key size (see generate_key())')
    print(c.hex())

    pt = 'Good luck!'
    c = double_encrypt(pt)
    print('Heres a ciphertext for "Good luck!" encrypted using the same algorithm and the same keys')
    print(c.hex())

if __name__ == '__main__':
    main()

