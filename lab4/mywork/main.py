from pwn import *
import re
import olve

io = remote("172.26.201.17", 2134)
recv = io.recvline().decode("utf-8")
print(recv)
num_question = input("Choose num question: ")
io.sendline(num_question.encode("utf-8"))
match num_question:
    case "1":
        question_text = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text)
        prime_number = re.findall(r"Prime:\ (.*)", question_text)[0]
        prime_number = int(prime_number)
        print(prime_number)
        p = [2, 3, 5, 7]
        for i in p:
            print(i)
            if Solve.set_H(i, prime_number):
                print("Y")
                io.sendline(str(i).encode())
                print(io.recvline())
                break
            else:
                print("N")
                continue
