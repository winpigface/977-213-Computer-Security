import os
from random import randrange

DEPLOY = False
flag = open('/home/ctf/flagQ3.txt', 'r').read().strip()


def printflag():
    print('977-213{'+flag+'}')


def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def main():
    Q3_CT = ['nqzabtijqamiagzqopb', 'zafqhqdkftuzsueqmekuzftqiadxp', 'gvwjizdnzsomzhzgztzvntjmijo', 'kzanmdhrdwsqdldkdxdzrxnqmns']
    ind = randrange(len(Q3_CT))
    print('Decrypt the following shift cipher: '+Q3_CT[ind])
    print('Hint: the plaintext contains a word ``easy``')

    ans = input('Answer: ')
    if 'easy' not in ans or len(ans) != len(Q3_CT[ind]):
        print('Wrong')
    else:
        dist = [(ord(Q3_CT[ind][i])-ord(ans[i]))%26 for i in range(len(Q3_CT[ind]))]
        if all(x == dist[0] for x in dist):
            printflag()
    


if __name__ == '__main__':
    main()
