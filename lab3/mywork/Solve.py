from Crypto.Hash import SHA256, MD5, HMAC
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import random


def Q1(UUID, UUID_HASH):
    # HASH UUID
    check = ""
    for i in range(len(UUID)):
        hashing_UUID = SHA256.new(UUID[i].encode())
        hashing_UUID_hex = hashing_UUID.hexdigest()
        if hashing_UUID_hex == UUID_HASH[i]:
            check += "Y"
        else:
            check += "N"
    return check


def Q2(password_Hash):
    i = 0
    print("Finding another password that have same hash...........")
    while True:
        MD5_Hash = MD5.new(str(i).encode("utf-8"))
        MD5_Hash_Hex = MD5_Hash.hexdigest()[:5]
        if MD5_Hash_Hex == password_Hash:
            print("Found same hash, Use this password to login: ", str(i))
            return str(i)
        else:
            i += 1


def Q3():
    store = {}
    while True:
        char = "abcdefghijkmnopqrstupwxyz0123456789"
        username = "".join(random.choice(char) for _ in range(10))
        a = MD5.new(username.encode("utf-8"))
        a_hex = a.hexdigest()[:10]
        if a_hex in store:
            print("found 2 username same hash")
            print("Same Hash is =", a_hex)
            print("username 1:", store[a_hex])
            print("username 2:", username)
            return store[a_hex], username
        else:
            store[a_hex] = username


def Q5_1(key, message):
    h = HMAC.new(key, message, SHA256)
    base64 = b64encode(h.digest())
    print("HMAC in base64 =", base64.decode("utf-8"))
    return base64


def Q5_2(key, message, header, nonce):
    nonce = b64decode(nonce)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    print("ciphertext=", ciphertext)
    print("tag =", tag)
    ciphertext_base64 = b64encode(ciphertext)
    tag_base64 = b64encode(tag)
    print("c_base64 =", ciphertext_base64)
    print("t_base64 =", tag_base64)
    return ciphertext_base64, tag_base64
