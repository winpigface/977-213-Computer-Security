import random

def getflag():
    flag = ""
    with open("/home/ctf/flag.txt", "r") as f:
        flag = f.read()[:-1]
    return "977_213{"+flag+"}"




for i in range(0,100):
    num1 = random.randint(0,10000)
    num2 = random.randint(0,10000)
    print("Add two numbers: "+str(num1)+","+str(num2))
    val = input('$ ')
    if val.isdigit() and int(val) != num1+num2:
        print("Goodbye")
        exit(1)

print(getflag())
