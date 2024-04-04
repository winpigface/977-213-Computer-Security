from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

def generator(g, prime):
    w = set()
    for pows in range(1,prime):
        num = pow(g,pows,prime)
        w.add(num)
    return len(w) == prime - 1

def public_key(g,my_privateKey,prime):
    return pow(g,my_privateKey,prime)

def create_share_key(teacher_publicKey,my_privateKey,prime):
    return pow(teacher_publicKey,my_privateKey,prime)

def encryption_key(share_key,nonce,header,ciphertext,tag):
    encryption_key = SHA256.new(share_key.to_bytes(share_key.bit_length(),byteorder="big")).digest()
    nonce = b64decode(nonce)
    header = b64decode(header)
    tag = b64decode(tag)
    ciphertext = b64decode(ciphertext)
    cipher = AES.new(encryption_key,AES.MODE_GCM,nonce=nonce)
    cipher.update(header)
    plaintext = cipher.decrypt_and_verify(ciphertext,tag)
    return plaintext.decode("utf-8")

def RSA_format():
    message = b'You can attack now!'
    key = RSA.importKey(open('../deploy/public.pem').read())
    cipher = PKCS1_OAEP.new(key)
    print(key.n,key.e)
