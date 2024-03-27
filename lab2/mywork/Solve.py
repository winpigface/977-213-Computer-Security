from Crypto.Cipher import AES,DES 
from Crypto.Util.Padding import pad,unpad

def Q1(IV):
    # data 0.1MB of zero
    data = '\x00'*int(1*10**5)
    data = data.encode('utf-8')
    # 128-bit long zero key (16 bytes = 128 bit)
    key = b'\x00'*16
    # COVERT IV from hex_str to bytes
    IV_bytes = bytes.fromhex(IV)
    print("Key =",key)
    print("IV bytes =",IV_bytes)
    # ENCRYPT use AES mode CBC
    cipher = AES.new(key,AES.MODE_CBC,IV_bytes)
    ciphertext = cipher.encrypt(pad(data,AES.block_size))
    return ciphertext.hex()

def Q2(ciphertext1,ciphertext2,plaintext1):
    ciphertext1_byte = bytes.fromhex(ciphertext1)
    ciphertext2_byte = bytes.fromhex(ciphertext2)
    plaintext1_byte = plaintext1.encode('utf-8')
    # FIND E(key,CTR) = C1 ^ P1
    Encrypt_CTR = bytes(cipher1 ^ plain1 for cipher1,plain1 in zip(ciphertext1_byte,plaintext1_byte))
    print("Encrypt_CTR =",Encrypt_CTR)
    # FIND P2 = E(key,CTR) ^ C2 
    # USE same E(key,CTR) because,CTR is reuse 
    plaintext2 = bytes(cipher2 ^ encrypt_CTR for cipher2,encrypt_CTR in zip(ciphertext2_byte,Encrypt_CTR))
    print("plaintext2 =",plaintext2)
    return plaintext2

# ALL posible 2-byte secret
def Q3_hex_2Byte():
    hex_text = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    hex_1Byte = []
    hex_2Byte = []
    for i in range(len(hex_text)):
        for j in range(len(hex_text)):
            hex_1Byte.append(hex_text[i] + hex_text[j])
    for i in range(len(hex_1Byte)):
        for j in range(len(hex_1Byte)):
            hex_2Byte.append(hex_1Byte[i] + hex_1Byte[j])
    return hex_2Byte

def Q4(plaintext,ciphertext,IV,plaintext_ans):
    plaintext_byte = plaintext.encode('utf-8')
    plaintext_ans_byte = plaintext_ans.encode('utf-8')
    ciphertext_byte = bytes.fromhex(ciphertext)
    # E(key,IV) = P1 ^ C1
    Encrypt_OFB = bytes(plain ^ cipher for plain,cipher in zip(plaintext_byte,ciphertext_byte))
    print("Encrypt_OFB =",Encrypt_OFB)
    # C2 = E(key,IV) ^ P2 
    # USE same E(key,IV) because,IV is reuse
    ciphertext2 = bytes(Encrypt_OFB ^ plain_ans for Encrypt_OFB,plain_ans in zip(Encrypt_OFB,plaintext_ans_byte))
    print("ciphertext2 =",ciphertext2)
    return ciphertext2.hex(),IV
    
def Q5(plaintext,ciphertext):
    # P -> E1(key1,ECB) -> X -> E2(key2,ECB) -> C
    # C -> D1(key2,ECB) -> X -> D2(key1,ECB) -> P
    # FIND X (Meet in middle attack)
    print("Finding...")
    store_Encrypt = []
    store_Decrypt = []
    store_Key = []
    plaintext_byte = plaintext.encode('utf-8')
    ciphertext_byte = bytes.fromhex(ciphertext)
    # 0 - 999999 posible digit key
    for i in range(1000000):
        key = format(i,'06')  
        key = pad(key.encode('utf-8'),DES.block_size)
        # ENCRYPT by all posible key, Then store in to array
        cipher = DES.new(key,DES.MODE_ECB)
        cipher_encrypt = cipher.encrypt(pad(plaintext_byte,DES.block_size))
        store_Encrypt.append(cipher_encrypt)
        # DECRYPT by all posible key, Then store in to array
        plain = DES.new(key,DES.MODE_ECB)
        plain_decrypt = plain.decrypt(ciphertext_byte)
        store_Decrypt.append(plain_decrypt)
        # STORE key in array 
        store_Key.append(key)
    # INTERSEC store_Encrypt array and store_Decrypt
    find_same = set(store_Encrypt) & set(store_Decrypt)
    if find_same:
        print("FOUND")
        print("same text is",find_same)
        # USE for-loop to get data in set 
        # THEN find index key by use index of store_Encrypt and store_Decrypt
        for text_findKey in find_same:
            # key1 is form first Encrypt and, key2 is form first Decrypt
            key1 = store_Key[store_Encrypt.index(text_findKey)]
            key2 = store_Key[store_Decrypt.index(text_findKey)]
        print("Key1 =",key1)
        print("key2 =",key2)
        return key1,key2

def Q5_decrypt_flag(key1,key2,flag_encrypt):
    decrypt2 = DES.new(key2,DES.MODE_ECB)
    decrypt1 = DES.new(key1,DES.MODE_ECB)
    flag_encrypt_byte = bytes.fromhex(flag_encrypt)
    first_decrypt = decrypt2.decrypt(flag_encrypt_byte)
    second_decrypt = decrypt1.decrypt(first_decrypt)
    
    flag = second_decrypt.decode('utf-8')
    return flag
