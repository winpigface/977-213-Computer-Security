import random
import re
from Crypto.Hash import SHA3_256

flag = open('/home/ctf/flagQ6.txt', 'r').read().strip()
#flag = 'aaa'

def printflag():
    print('977-213{'+flag+'}')

def h(mb):
    for i in range(0,1000):
        h = SHA3_256.new(mb)
        mb = h.digest()
    return h.hexdigest()

def hash(message):
    out = []
    for m in message:
        out.append(h(str.encode(m)))
    return out

def checkpwd(pwd, pwdhash):
    for i in range(0,len(pwdhash)):
        if i >= len(pwd) or i >= len(pwdhash):
            return False
        m = pwd[i]

        out = h(str.encode(m))
        if out != pwdhash[i]:
            return False
    return True

digits = '1234567890'
def main():
    print("Q6: side-channel attack.")
    print("I invented a new way for password authentication. Break it!")

    # pwd = random 10 digits
    pwd = ''.join([random.choice(digits) for i in range(10)])
    pwdhash = hash(pwd)
    #print(pwd)
    #print(pwdhash)

    # I give you 10000 tries to crack
    for i in range(0,10000):
        print("Enter 10-digit PIN to login:")
        resp = input('$').strip()
        
        if not re.match("^[0-9_-]*$", resp):
            print('PIN must be 0-9')
            exit(1)
        
        if checkpwd(resp, pwdhash):
            print('Welcome back, Oak')
            printflag()
            exit(1)
        else:
            print("Wrong")
    print('You spent too much time....')
   
if __name__ == '__main__':
    main()
