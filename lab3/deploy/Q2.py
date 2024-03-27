import random
from Crypto.Hash import MD5

flag = open('/home/ctf/flagQ2.txt', 'r').read().strip()

def printflag():
    print('977-213{'+flag+'}')


def oHash(message):
    message = str.encode(message)
    h = MD5.new(message)
    return h.hexdigest()[:5]


chars = 'qwertyuiop[]asdfghjkl;zxcvbnm,./1234567890-='
def main():
    print("Q2: weak-collision resistance.")
    print("I invented a new hash function called `Oak Hash` (oHash in short). I envision it to be used as a login mechanism on my low-memory computer. So I limit the hash output to only 5 hex digits of MD5 hash")
    pwd = ''.join([random.choice(chars) for i in range(20)])
    #print(pwd)
    pwd_hash = oHash(pwd)
    print("My password is super strong and very long. So there is no chance that you can crack it. To make it more interesting, I'll even give you my password hash.")
    print(pwd_hash)

    print("Enter password to login:")

    resp = input('$').strip()
    if oHash(resp) == pwd_hash:
        print('Welcome back, Oak')
        printflag()
    else:
        print("Well, tough luck")

   
if __name__ == '__main__':
    main()
