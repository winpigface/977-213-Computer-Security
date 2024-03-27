from random import randrange
Q3_CT = ['nqzabtijqamiagzqopb', 'zafqhqdkftuzsueqmekuzftqiadxp', 'gvwjizdnzsomzhzgztzvntjmijo', 'kzanmdhrdwsqdldkdxdzrxnqmns']
ind = randrange(len(Q3_CT))
print('[Optional Question] Decrypt the following shift cipher: '+Q3_CT[ind])
print('Hint: the plaintext contains a word ``easy``')

ans = input()
if 'easy' not in ans or len(ans) != len(Q3_CT[ind]):
    print('Wrong')
else:     
    dist = [(ord(Q3_CT[ind][i])-ord(ans[i]))%26 for i in range(len(Q3_CT[ind]))]
    if all(x == dist[0] for x in dist):
        print('Another FLAG: 977-213{CongratzOnYourFirstBruteForce}')

