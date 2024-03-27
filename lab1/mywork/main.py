from pwn import *
import re
import Solve

io = remote('172.26.201.17',2131)
recv = io.recvline().decode('utf-8')
print(recv)
# INPUT number of question to solve
Q_number = input('')
recv = io.sendline(Q_number.encode('utf-8'))
# SHOW question
recv = io.recvline().decode("utf-8")
print(recv)
# SOLVE question 
match Q_number:
    case '1':
        ciphertext = re.findall(r'"(.*)"',recv)
        key = re.findall(r'=(\d+)',recv)
        print("----------------------")
        print(f"ciphertext = {ciphertext[0]}")
        print(f"key = {key[0]}")
        # SEND answer
        io.sendline(Solve.Q1(ciphertext[0],key[0]).encode('utf-8'))
        # SHOW result
        print(io.recvline().decode("utf-8"))
    case '2':
        # SHOW all text in question 2
        pattern = r'="(.*)"'
        recv = io.recvregex(pattern.encode('utf-8')).decode('utf-8')
        plaintext = re.findall(r'\s"(.*)"\s',recv)
        key = re.findall(r'="(.*)"',recv)
        # UNPACK string (split string to char)
        key_char = [*key[0]]
        print(recv)
        print("----------------------")
        print(f"plaintext = {plaintext[0]}")
        print(f"key = {key[0]}")
        # SEND answer
        io.sendline(Solve.Q2(plaintext[0],key_char).encode('utf-8'))
        # ENTER to show result
        io.recvline()
        print(io.recvline().decode("utf-8"))
    case '3':    
        # GET ciphertext in question 3
        shift_cipher = re.findall(r':\s(.*)',recv)
        # SHOW hint in question 3
        recv = io.recvline().decode('utf-8')
        hint = re.findall(r'``(.*)``',recv)
        print(recv)
        print("----------------------")
        print(f"ciphertext = {shift_cipher[0]}")
        print(f"hint = {hint[0]}")
        # SEND answer
        io.sendline(Solve.Q3(shift_cipher[0],hint[0]).encode('utf-8'))
        # SHOW result
        print(io.recvline().decode("utf-8"))
    case '4':
        # GET OTP and ciphertext from question 4
        recv = io.recvline().decode('utf-8')
        OTP = re.findall(r':\s(.*)',recv)
        print(recv)
        recv = io.recvline().decode('utf-8')
        ciphertext = re.findall(r':\s(.*)',recv)
        print(recv)
        print("----------------------")
        # SEND answer
        io.sendline(Solve.Q4(ciphertext[0],OTP[0]).encode('utf-8'))
        # SHOW result
        print(io.recvline().decode('utf-8'))
    case _:
        print("NOT FOUND")


