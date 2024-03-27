from pwn import *
import re
import Solve

io = remote("172.26.201.17", 2133)
recv = io.recvline().decode("utf-8")
print(recv)
num_question = input("Choose num question: ")
io.sendline(num_question.encode("utf-8"))
match num_question:
    case "1":
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text)
        print("------------------------------------------")
        UUID = re.findall(r"\d\sUUID:\s(.*)", question_text)
        UUID_HASH = re.findall(r"\d\sHash\(UUID\):\s(.*)", question_text)
        check_protection = Solve.Q1(UUID, UUID_HASH)
        print(check_protection)
        # SEND answer
        io.sendline(check_protection.encode("utf-8"))
        print(io.recvline().decode("utf-8"))

    case "2":
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text)
        print("------------------------------------------")
        password_Hash = re.findall(r"password hash.\n(.*)", question_text)[0]
        print("Password Hash =", password_Hash)
        Login_password = Solve.Q2(password_Hash)
        # SEND answer
        io.sendline(Login_password.encode("utf-8"))
        print(io.recvline().decode("utf-8"))
        print(io.recvline().decode("utf-8"))

    case "3":
        # SHOW question
        question_text = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text)
        print("------------------------------------------")
        a, b = Solve.Q3()
        # SEND answer
        io.sendline(a.encode("utf-8"))
        io.sendline(b.encode("utf-8"))
        print(io.recvline().decode("utf-8"))

    case "5":
        # SHOW question in Q5.1
        question_text1 = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text1)
        print("------------------------------------------")
        key = re.findall(r"key=b'(.*)'", question_text1)[0].encode("utf-8")
        message = b"Welcome to the Jungle!"
        # SEND answer in Q5.1
        HMAC_base64 = Solve.Q5_1(key, message)
        io.sendline(HMAC_base64)
        print("------------------------------------------")
        # SHOW question in Q5.2
        question_text2 = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text2)
        header = re.findall(r"Header:\ (.*)", question_text2)[0].encode("utf-8")
        nonce = re.findall(r"Nonce\ in\ base64:\ (.*)", question_text2)[0].encode(
            "utf-8"
        )
        ciphertext_base64, tag_base64 = Solve.Q5_2(key, message, header, nonce)
        io.sendline(ciphertext_base64)
        io.sendline(tag_base64)
        print(io.recvline().decode("utf-8"))
