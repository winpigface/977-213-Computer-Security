from pwn import *
import re
import Solve

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
        # z = {1,2,3,...,prime - 1}
        range_prime = set(range(1,prime_number))
        g = int()
        print("Finding generator...")
        for i in range(prime_number):
            if(Solve.generator(i,prime_number,range_prime)):
                g = i
                break
            else:
                continue
        io.sendline(str(g).encode())
        question_text2 = io.recvrepeat(timeout=0.5).decode("utf-8")
        print(question_text2)
        
        
        
