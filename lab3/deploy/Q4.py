import os
from Crypto.Cipher import AES

flag = open('/home/ctf/flagQ4.txt', 'r').read().strip()

key = os.urandom(11)

def printflag():
    print('977-213{'+flag+'}')

# Use lazy Davies-Mayer to build hash from block cipher
# https://en.wikipedia.org/wiki/One-way_compression_function#Davies%E2%80%93Meyer
# H = E(m, prevH) # xor prevH # too lazy to do this xor
def hash_block(m, prevH):
    if len(m) > AES.block_size:
        raise('Block size must be 16 bytes')
    cipher = AES.new(m, AES.MODE_ECB) # Mode shouldnt matter since we only do one-block encryption
    return cipher.encrypt(prevH)

# simple Merkle-Damgard construction
# output = hash_block(bn, hash_block(bn-1, ..., hash_block(b1, b'1'*32)...))
# assume msg is a multiple of AES.block_size bytes
def hash(msg):
    if len(msg) % AES.block_size != 0:
        raise('Block size is not a multiple of 16 bytes')
    num_blocks = int(len(msg)/AES.block_size)
    prevH = b'1'*32
    for i in range(0, num_blocks):
        m = msg[i*AES.block_size:(i+1)*AES.block_size]
        newH = hash_block(m, prevH)
        prevH = newH
    return prevH

# MAC = H(key || msg) 
def mac(message):
    message = key+str.encode(message)
    return hash(message).hex()

def command(c):
    if c == 'LAUGH':
        print('55555555555555555')
    elif c == 'FLAG':
        printflag()
    elif c == 'EXIT':
        exit(1)
    else:
        print('I dont know what to do with this command',c)

def atk(newMsg, oldHash):
    newMsg = str.encode(newMsg)
    return hash_block(newMsg, oldHash)

def main():
    print("Q4: Never brew your own crypto!")
    token = mac("LAUGH")
    print('To make me laugh, give me `LAUGH` command with this token:', token)


    commands = input('Enter command: ').strip()
    mac_commands = mac(commands)
    token = input('Enter token: ').strip()

    if mac_commands != token:
        print('Unauthorized commands')
        exit(1)

    commands = commands.split()
    for c in commands:
        command(c)


   
if __name__ == '__main__':
    main()
