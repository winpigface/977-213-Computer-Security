import os
from random import randrange

DEPLOY = False
flag = open('/home/ctf/flagQ2.txt', 'r').read().strip()


def printflag():
    print('977-213{'+flag+'}')


def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def main():
    Q1_PT = ['scan', 'cumbersome', 'committee', 'momentous', 'inflame', 'announce', 'determined', 'standing', 'flippant', 'intelligent', 'cumbersome', 'betray', 'committee', 'motion', 'handsome', 'concerned', 'smooth', 'overflow']
    Q2_PT = Q1_PT
    Q2_CT = ['zshw', 'dqrieemfse', 'bwitxzrov', 'ckfuqpbpf', 'nfjyhtv', 'qlkfpkhc', 'thhoogrwib', 'pejpqnqk', 'htkhrytk', 'mtvhcuquadu', 'rwhzlnwmdd', 'aaoywp', 'eejqiyiju', 'mjpcpk', 'avnrrfib', 'nbwohehmk', 'esqdsr', 'kajzqrgk']
    Q2_K = ['hqhj', 'bwfhanurga', 'ziwhpgykr', 'qwtqdwnvn', 'fsenhhr', 'qyxrvxfy', 'qdokxujjey', 'xljcnfde', 'cicscygr', 'egcdrjiowqb', 'pcvyhweyrz', 'zwvhwr', 'cqxeafpfq', 'avwubx', 'tvaozrwx', 'lnjmdnuih', 'mgcpzk', 'wffilgso']

    ind = randrange(len(Q2_PT))

    print('Q2: consider OTP of letters where its encryption is done by performing an addition mod 26 between each letter of plaintext and the corresponding letter from OTP')
    print('For example: ')
    print('Plaintext: hel')
    print('OTP(key): wrl')
    print('Ciphertext: dvw')
    print('because h=7, w=22, h+w mod 26 = 29 mod 26 = 3 = d')
    print('e=4, r=17, e+r=26 mod 21 = v')
    print('l=11, l+l=22 mod 26 = w')
    print('Now encrypt the following plaintext: "'+Q2_PT[ind]+'" with key="'+Q2_K[ind]+'"')

    ans = input('Enter the ciphertext: ')
    while ans != Q2_CT[ind]:
        print('Your answer is incorrect. Try again')
        ans = input('Enter the ciphertext: ')
    
    printflag()


if __name__ == '__main__':
    main()
