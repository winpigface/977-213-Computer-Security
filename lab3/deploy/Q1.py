import os
import uuid
import random
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

flag = open('/home/ctf/flagQ1.txt', 'r').read().strip()

def printflag():
    print('977-213{'+flag+'}')

hexdigit = '0123456789abcdef'

def recv_message(message, transmit_error):
    out = message
    if transmit_error:
        c = message[0]
        c2 = c
        while c2 == c:
            c2 = random.choice(hexdigit)
        out = c2 + message[1:]
    return out


def simulate_network_error():
    return bool(random.getrandbits(1))


def generate_random_uuid():
    out = ''
    for i in range(0,10):
        out += str(uuid.uuid4())+','
    return out[:-1]


def hash(message):
    message = str.encode(message)
    h = SHA256.new(message)
    return h.hexdigest()


def main():
    print("Q1: Integrity check via hashing.") 
    print("Use pycrptodome's SHA256 (https://pycryptodome.readthedocs.io/en/latest/src/hash/sha256.html).")
    print("You are given 20 strings in form of long UUIDs below. To ensure integrity, each string is accompanied with its SHA256 digest. Your goal is to check whether the received UUIDs string is transmitted to you with integrity preservation or not.")

    sim_err_list = []
    # To make sure you know the answer, repeat it 20 times!
    for i in range(0,20):
        uuid = generate_random_uuid()
        h = hash(uuid)
        sim_err = simulate_network_error()
        sim_err_list.append(sim_err)
        uuid = recv_message(uuid, sim_err)
        print(i, 'UUID:', uuid)
        print(i, 'Hash(UUID):',h)


    print("Return 20 characters consisting of either 'Y' or 'N', where 'Y' means that integrity is preserved")
    print("For example: YYYYYYYYYYYYYYYYYYYY indicates all strings are received with integrity protection, while YYYYYYYYYYYYYYYYYYYN means only last string has been tampered with during transmission")
    resp = input('$').strip()
    if len(resp) != 20 or set(resp) == set(b'YN'): #resp != 'Y' and resp != 'N':
        print('Invalid response')
        exit(-1)

    for i in range(0,20):
        resp_bool = False if resp[i] == 'N' else True
        if resp_bool == sim_err_list[i]:
            print('Wrong!')
            exit(-1)
        
    printflag()

   
if __name__ == '__main__':
    main()
