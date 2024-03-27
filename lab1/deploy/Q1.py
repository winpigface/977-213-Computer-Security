import os
from random import randrange

DEPLOY = False
flag = open('/home/ctf/flagQ1.txt', 'r').read().strip()


def printflag():
    print('977-213{'+flag+'}')


def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def main():
    Q1_PT = ['scan', 'cumbersome', 'committee', 'momentous', 'inflame', 'announce', 'determined', 'standing', 'flippant', 'intelligent', 'cumbersome', 'betray', 'committee', 'motion', 'handsome', 'concerned', 'smooth', 'overflow']
    Q1_CT = ['qayl', 'hzrgjwxtrj', 'seccyjjuu', 'prphqwrxv', 'xcuapbt', 'fsstzshj', 'ijyjwrnsji', 'jkreuzex', 'tzwddobh', 'qvbmttqomvb', 'fxpehuvrph', 'adsqzx', 'pbzzvggrr', 'lnshnm', 'vobrgcas', 'zlkzbokba', 'fzbbgu', 'zgpcqwzh']
    Q1_K = [24, 5, 16, 3, 15, 5, 5, 17, 14, 8, 3, 25, 13, 25, 14, 23, 13, 11]

    ind = randrange(len(Q1_PT))

    print('Q1: "'+Q1_CT[ind] + '" is encrypted using the shift cipher with key='+str(Q1_K[ind])+'. Please decrypt it.')
    ans = input('Enter the decrypted plaintext: ')

    while ans != Q1_PT[ind]:
        print('Your answer is incorrect. Try again')
        ans = input('Enter the decrypted plaintext: ')
    
    printflag()


if __name__ == '__main__':
    main()
