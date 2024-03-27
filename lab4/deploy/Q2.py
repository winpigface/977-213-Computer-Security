import random
import sympy
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import json
import sys
from Crypto.Hash import SHA256

def fast_pow(a,b,p):
    if False:
        return pow(a,b,p)
    if b < 10:
        return pow(a,b)%p
    if b%2 == 1:
        A = fast_pow(a, int((b-1)/2),p)
        return (A*A*a) % p
    A = fast_pow(a, int(b/2),p)
    return (A*A)%p

class DHKE:
    def __init__(self,G,P):
        self.G_param = G
        self.P_param = P

    def check_generator(self):
        
        X = 1
        for i in range(1,self.P_param):
            # g^x should be non-repetitive
            X = (X*self.G_param) % self.P_param
            if i != 1 and X == 1:
                print('Not a generator')
                print('g =',self.G_param,'P =',self.P_param,'i=',i)
                return False

        return True

    def generate_privatekey(self):
        self.pk = random.randrange(start = 1,stop = self.P_param-1)

    def generate_publickey(self):
        self.pub_key = fast_pow(self.G_param,self.pk,self.P_param)

    def exchange_key(self,other_public):
        self.share_key = fast_pow(other_public,self.pk,self.P_param)

def share_key_to_AES_key(share_key):
    return SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder='big')).digest()


flag = open('/home/ctf/flagQ2.txt', 'r').read().strip()

def getflag():
    return '977-213{'+flag+'}'

prime = 0xE69278B9117E6F2DCC5414A5AD30C7F6BD783171222A78943B9E14CAAA8C356CED8919FEEA0690DB507DA6E9B90FD55E3B63DE94D7E773A9FAE904B610A99FD1573B0EE6E7D6D61A59CD4500BA36A963C847C721FEBA8CC3487C22A744CC57A03DBEDCD58C20DD0F02C653E8D56B58CCE2A5653C36F62A122312FAA7AC9F2CEB
g = 2

def main():
    sys.setrecursionlimit(1500)
    print('Q2: Big exponent. Similar to Q1')
    print()
    print('DHKE parameters (in hex):')
    print('Prime:', hex(prime))
    print('Generator:', hex(g))

    me = DHKE(g,prime)
    me.generate_privatekey()
    me.generate_publickey()

    other_pub = int(input('Enter your public key (in int): ').strip())

    if not 1 < other_pub < (prime-1):
        print('Invalid public key')
        exit(1)

    me.exchange_key(other_pub)

    print('My public key (in hex):', hex(me.pub_key))


    key = share_key_to_AES_key(me.share_key)
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
    print('See header (or associated data) for instructions on how to get the flag')
    print()
    print(result)

if __name__ == '__main__':
    main()
