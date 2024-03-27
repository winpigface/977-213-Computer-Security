import os

DEPLOY = True
flag = open('/home/ctf/flagQ4.txt', 'r').read().strip()


def printflag():
    print('977-213{'+flag+'}')


def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))


def main():
    ct = "12113d6e6b8a3e51a58f6c6699df1303ce9966046264fd1aaca8b00541ca626e0af4ba567cd3e08a200df5a574dfa2c21b65d6b30642ff725b61ff62510633944923789b0052553fab888e5711137d7de2a1d7"
    pt = '8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.'
    otp = "2a341d010daa0c6485e61f46edb77623bdf80b6142058e3a9e9d95252eac42562a95d4325cbc8eef0062938500b7c7af3b0ca5936b379c1a7b049e11386341b43d4c58ff6f723c518bf1e1226333151883c5f9"

    print('Decrypt using One-time Pad:')
    print('(In hexstr) OTP:', otp)
    print('(In hexstr) ciphertext:', ct)
    recv = input('$').strip()
    if pt == recv:
        printflag()


if __name__ == '__main__':
    main()
