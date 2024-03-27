import os
import random
from base64 import b64decode, b64encode
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES

flag = open('/home/ctf/flagQ5.txt', 'r').read().strip()
#flag = "abc"

def printflag():
    print('977-213{'+flag+'}')


def mac(key, message):
    h = HMAC.new(key, message, SHA256)
    return b64encode(h.digest()).decode('utf-8')


def main():
    print("Q5: MAC+Authenticated encryption.")
    print("Using key=b'oak1234567890abc' to perform the following operations. Output it in BASE64 (not HEXSTR)")
    print()
    print("Q5.1: HMAC-SHA256(key, 'Welcome to the jungle!') in base64")
    key = b'oak1234567890abc'
    msg = 'Welcome to the Jungle!'
    msg = str.encode(msg)
    token = mac(key, msg)

    recv_token = input('$').strip()
    if token != recv_token:
        print('Wrong')
        exit(1)

    print("Q5.2: AES-128-GCM(key, 'Welcome to the Jungle!') (authenticated encryption) with:")
 
    nonceb64 = 'DpOK8NIOuSOQlTq+BphKWw=='
    header = 'PleaseSendThisToIP21.36.222.155'

    print('Header:', header)
    print('Nonce in base64:', nonceb64)

    nonce = b64decode(nonceb64)
    header = str.encode(header)

    recv_ct = input('Enter ciphertext in base64: ').strip()
    recv_tag = input('Enter MAC tag in base64: ').strip()
    try:
        recv_ct = b64decode(recv_ct)
        recv_tag = b64decode(recv_tag)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        cipher.update(header)
        plaintext = cipher.decrypt_and_verify(recv_ct, recv_tag)
        if plaintext == msg:
            printflag()
        else:
            print('How is that possible????')

    except (ValueError, KeyError):
        print("Incorrect decryption")



if __name__ == '__main__':
    main()
