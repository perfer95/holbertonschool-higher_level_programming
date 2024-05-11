#!/usr/bin/python3
# 100-print_tebahpla.py

flag = True
for i in range(122, 96, -1):
    print("{}".format(chr(i) if flag else chr(i - 32)), end="")
    flag = not flag

