#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    import sys

    arg_v = sys.argv
    len_argv = len(arg_v) - 1  # Just arguments no file name
    sum = 0

    if len_argv > 1:
        for i in range(1, len_argv + 1):
            sum += int(arg_v[i])
    print(sum)
