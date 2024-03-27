import random
import sympy
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import json

class DHKE:
    def __init__(self,G,P):
        self.G_param = G
        self.P_param = P

    def check_generator(self):
        
        out = set()
        l = list()
        X = 1
        for i in range(1,self.P_param):
            # g^x should be non-repetitive
            X = (X*self.G_param) % self.P_param
            if X in out:
                print('Not a generator. Aborting...')
                return False
            out.add(X)
            l.append(X)

        return True

    def generate_privatekey(self):
        self.pk = random.randrange(start = 1,stop = self.P_param-1)

    def generate_publickey(self):
        self.pub_key = pow(self.G_param,self.pk,self.P_param)

    def exchange_key(self,other_public):
        self.share_key = pow(other_public,self.pk,self.P_param)

def share_key_to_AES_key(share_key):
    return SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder='big')).digest()


flag = open('/home/ctf/flagQ1.txt', 'r').read().strip()

def getflag():
    return '977-213{'+flag+'}'

def main():
    prime = sympy.randprime(2**20, 2**24)
    print('Q1: Generator checker. Perform Diffie-Hellman Key Exchange (DHKE) to get a shared key used to encrypt the flag.')
    print()
    print('DHKE parameters:')
    print('Prime:',prime)
    g = input('Enter generator (in int): ').strip()
    g = int(g)

    d = DHKE(g,prime)

    if not d.check_generator():
        exit(1)

    d.generate_privatekey()
    d.generate_publickey()

    print(g, 'is a generator')
    print('My public key:', str(d.pub_key))

    other_public = input('Enter your public key (in int): ').strip()
    other_public = int(other_public)

    if not 1 < other_public < (prime-1):
        print('Invalid public key')
        exit(1)


    d.exchange_key(other_public)

    key = share_key_to_AES_key(d.share_key)
    cipher = AES.new(key, AES.MODE_GCM)
    header = b'Decrypt this ciphertext to get the flag. encryption_key=SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder="big")).digest(), where share_key is a shared key created using DHKE and of int type. Encryption is done using AES256-GCM'
    msg = getflag()
    msg = str.encode(msg)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(msg)

    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag) ]
    result = json.dumps(dict(zip(json_k, json_v)))
    #print(header)

    print()
    print('Ciphertext is encoded using base64. See header for instructions on how to get the flag')
    print()
    print(result)

if __name__ == '__main__':
    main()
