from pwn import *
import re

print("Hello World!")

io = remote('172.26.201.17',2223)

recv = io.recvline()

print("recv : ",recv)
recv = recv.decode("utf-8")

#recv = str(recv)
print(recv)
nums = re.findall(r'\d+',recv)
print("nums 1 is " , nums[0])
print("nums 2 is ",nums[1])

print(type(recv))
print("I recived: "+ recv)
print("num is:",nums)

recv = io.sendline(str(int(nums[0])+int(nums[1])).encode("utf-8"))
print("recvline :: ",io.recvline())
