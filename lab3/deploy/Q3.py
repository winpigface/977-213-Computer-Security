import os
import random
import re
from Crypto.Hash import MD5

flag = open('/home/ctf/flagQ3.txt', 'r').read().strip()

def printflag():
    print('977-213{'+flag+'}')


def oHashPlus(message):
    message = str.encode(message)
    h = MD5.new(message)
    return h.hexdigest()[:10]


def main():
    print("Q3: strong-collision resistance.")
    print("I think the problem with oHash was its too short digest size. So I'll double the size to 10 hex digits, called it oHashPlus")
    print("I use this hash to generate a crypto wallet ID from a given username. I heard the hash output looks random, so there shouldnt be 2 usernames with the same wallet ID.")
    print("Break this claim: give me two usernames (containing only a-z or 0-9) that result in the same hash")

    user1 = input('$').strip()
    user2 = input('$').strip()
    if user1 == user2:
        print('Give me 2 UNIQUE usernames!')
        exit(1)

    if not re.match("^[a-z0-9_-]*$", user1) or not re.match("^[a-z0-9_-]*$", user2):
        print('usernames are invalid! They must contain either a-z or 0-9', user1, user2)
        exit(1)

    if oHashPlus(user1) != oHashPlus(user2):
        print('Wrong')
        exit(1)

    printflag()
    
if __name__ == '__main__':
    main()
