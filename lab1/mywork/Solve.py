import re
import binascii
def Q1(ciphertext,key):
    plaintext = ""
    for char in ciphertext:
        ascii_num = ord(char)
        decode_num = ((ascii_num - int(key)) - ord('a')) % 26
        decode_char = chr(decode_num+ord('a'))
        print(char,ord(char),decode_num+ord('a'),decode_char)
        plaintext +=  decode_char
    print(plaintext)
    return plaintext

def Q2(plaintext,key):
    ciphertext = ""
    i = 0
    for char in plaintext:
        # a-z should be 0-25
        # BUT a-z in ASCII is 97-122
        num_char = ord(char) - ord('a')
        num_key = ord(key[i]) - ord('a')
        ciphertext_num =  (num_char + num_key) % 26
        print(char,ord(char),ciphertext_num+ord('a'),chr(ciphertext_num + ord('a')))
        ciphertext += chr(ciphertext_num + ord('a'))
        i += 1
    return ciphertext

def Q3(ciphertext,hint):
    key = 1
    while key<=26:
        plaintext = ""
        for char in ciphertext:
            ascii_num = ord(char)
            decode_num = ((ascii_num - int(key)) - ord('a')) % 26
            decode_char = chr(decode_num+ord('a'))
            plaintext += decode_char
        print(plaintext)
        find_hint = re.search(hint,plaintext)
        # IF find easy in text it will be break ,if not it plus 1 key then continue
        if find_hint:
            print(plaintext.encode('utf-8'))
            return plaintext
            break
        else:
            key += 1
            continue

def Q4(ciphertext,OTP):
    # CONVERT hex (16-digit)[0-9a-f] -> dec (10-digit)[0-9]
    ciphertext_int = int(ciphertext,16)
    OTP_int = int(OTP,16)
    print("cipher_int :",ciphertext_int,'\n')
    print("OTP_int:",OTP_int,'\n')
    # XOR ( int ^ int )
    plaintext_XOR = ciphertext_int ^ OTP_int 
    print("XOR_int:",plaintext_XOR,'\n')
    # COVERT plaintext_XOR int -> hex (to use bytes.fromhex())
    # THEN convert it in to bytes
    plaintext = bytes.fromhex(hex(plaintext_XOR)[2:]).decode('utf-8')
    print(plaintext)
    return plaintext

def Q5(ciphertext,plaintext_set):
    flag = re.findall(r'[0-9a-f]{32}',ciphertext)
    print(ciphertext[len(ciphertext):32])
