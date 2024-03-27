from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA

DEPLOY = True

if DEPLOY:
    flag = open('/home/ctf/flagQ4.txt', 'r').read().strip()
else:
    flag = 'ab'

def getflag():
    return '977-213{'+flag+'}'

def main():
    print('Q4: RSA Assumption.')
    print()
    print('You have intercepted a flag sent to Alice, encrypted using PKCS1_OAEP.')
    
    # Alice:
    key = RSA.generate(2048)
    public_key = key.publickey().export_key('PEM')
    private_key = key.export_key('PEM')
    print()
    print('Alice announces her public key (in PEM format) as follows:')
    print(public_key.decode('utf-8'))
    print()

    # Bob:
    alice_public_key = RSA.importKey(public_key)
    alice_public_key = PKCS1_OAEP.new(alice_public_key)
    encrypted_flag = alice_public_key.encrypt(str.encode(getflag()))

    print()
    print('Intercepted message (in hex):')
    print('0x'+encrypted_flag.hex())

    print()
    print('Hint: you have discovered one RSA factor', hex(key.p))
    print('Hint2: you may need to use // operator for big integer division in Python')

if __name__ == '__main__':
    main()
