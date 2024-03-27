from random import randrange, choices
import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


pt = ['scan',
'cumbersome',
'committee',
'momentous',
'inflame',
'announce',
'determined',
'standing',
'flippant',
'intelligent',
'cumbersome',
'betray',
'committee',
'motion',
'handsome',
'concerned',
'smooth',
'overflow'
]

k = []
ct = []
for i in range(len(pt)):
    k.append(randrange(26)+1)
    ct.append(caesar(pt[i], k[i]))

print(pt)
print(ct)
print(k)


k = []
ct = []
for i in range(len(pt)):
    k.append(''.join([string.ascii_lowercase[k] for k in  choices(range(0,26), k=len(pt[i]))]))
    out = ''
    for j in range(len(pt[i])):
        out += caesar(pt[i][j], ord(k[i][j])-ord('a'))
    ct.append(out)
print(pt)
print(ct)
print(k)

ct = ['nqzabtijqamiagzqopb', 'zafqhqdkftuzsueqmekuzftqiadxp', 'gvwjizdnzsomzhzgztzvntjmijo']
ct = ct[2]
for i in range(27):
    pt = caesar(ct, i)
    print(pt, 'easy' in pt)

