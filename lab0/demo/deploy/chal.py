print("Echo demo! Get the flag!")

import os

with open("/home/ctf/flag.txt", "r") as f:
    while True:
        val = input('$ ')
        if val == '1234321':
            print("977_213{"+f.read()[:-1]+"}")
            break
        print(val)
