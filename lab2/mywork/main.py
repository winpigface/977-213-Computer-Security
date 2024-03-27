from pwn import *
import re
import Solve

io = remote('172.26.201.17',2132)

#SHOW text 'Enter 1-5: (note Q5 is worth 2 points)'
print(io.recvline().decode('utf-8'))
#INPUT number question ,and send number to io
Number_question = input('Choose number of question : ')
io.sendline(Number_question.encode('utf-8'))
print("--------------------")
match Number_question:
    case '1':
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode('utf-8')
        print(question_text)
        print("--------------------")
        # GET IV,data by use re
        IV = re.findall(r'IV:\s(.*)',question_text)[0] 
        # SEND answer
        io.sendline(Solve.Q1(IV).encode('utf-8'))
        print(io.recvline().decode('utf-8'))
    case '2':
        # SHOW question
        question_text = io.recvline().decode('utf-8')
        print(question_text)
        question_ciphertext1 = io.recvline().decode('utf-8')
        print(question_ciphertext1)
        question_ciphertext2 = io.recvline().decode('utf-8')
        print(question_ciphertext2)
        question_plaintext = io.recvrepeat(timeout=0.5).decode('utf-8')
        print(question_plaintext)
        print("--------------------")
        # GET ciphertext1 , ciphertext2 ,plaintext1 by use re
        ciphertext1 = re.findall(r'(.*)\s',question_ciphertext1)[0]
        ciphertext2 = re.findall(r'(.*)\s',question_ciphertext2)[0]
        plaintext1 = re.findall(r'x.*x',question_plaintext)[0]
        print("Ciphertext 1 =",ciphertext1)
        print("Ciphertext 2 =",ciphertext2)
        print("Plaintext 1 =",plaintext1)
        # SEND answer
        io.sendline(Solve.Q2(ciphertext1,ciphertext2,plaintext1))
        print(io.recvline().decode('utf-8'))
    case '3':
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode('utf-8')
        print(question_text)
        search_2Byte = Solve.Q3_hex_2Byte()
        print(search_2Byte) 
        for i in range(len(search_2Byte)):
            # S1S20e0e0e0e0e0e0e0e0e0e0e0e0e0e R1R20e0e0e0e0e0e0e0e0e0e0e0e0e0e
            hex_find_secret = '0e'*14 + (search_2Byte[i] + '0e' *14)
            io.sendline(hex_find_secret.encode('utf-8'))
            # USE [1:] because don't need $ from output
            ciphertext_find_secret = io.recvline()[1:]
            # cipbertext from S1S20e0e0e0e0e0e0e0e0e0e0e0e0e0e (first block)
            first_block = ciphertext_find_secret[0:32]
            # ciphertext form R1R20e0e0e0e0e0e0e0e0e0e0e0e0e0 (second block) 
            second_block = ciphertext_find_secret[32:64]
            # print("find secret:",ciphertext_find_secret)
            # IF first_block == second_block, it  means it has same plaintext
            if (first_block == second_block):
                answer = search_2Byte[i]
                print("Secret =",answer)
                break
        # READY to guess type 'c'
        io.sendline(b'c')
        print(io.recvline().decode('utf-8'))
        # SEND answer
        io.sendline(answer.encode('utf-8'))
        print(io.recvline().decode('utf-8'))

    case '4':
        # SHOW question
        question_text = io.recvline().decode('utf-8')
        print(question_text)
        question2_text = io.recvline().decode('utf-8')
        print(question2_text)
        plaintext = io.recvline().decode('utf-8')
        plaintext = re.findall(r'Gimme 100 Baht',plaintext)[0]
        print(plaintext)
        ciphertext = io.recvline().decode('utf-8')
        print(ciphertext)
        IV = io.recvline().decode('utf-8')
        print(IV)
        last_question_text = io.recvrepeat(timeout=0.5).decode('utf-8')
        print(last_question_text)
        plaintext_ans = re.findall(r'Gimme 900 Baht',last_question_text)[0]
        ciphertext_ans,IV = Solve.Q4(plaintext,ciphertext,IV,plaintext_ans)
        # SEND answer
        io.sendline(ciphertext_ans.encode('utf-8'))
        io.sendline(IV.encode('utf-8')) 
        print(io.recvline().decode('utf-8'))

    case '5':
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode('utf-8')
        print(question_text)
        flag_encrypt = re.findall(r'\(see generate_key\(\)\)\n(.*)',question_text)[0]
        plaintext = re.findall(r'Good\sluck!',question_text)[0]
        ciphertext = re.findall(r'keys\n(.*)\n',question_text)[0]
        key1,key2 = Solve.Q5(plaintext,ciphertext)
        flag = Solve.Q5_decrypt_flag(key1,key2,flag_encrypt)
        # SHOW flag
        print(flag)
