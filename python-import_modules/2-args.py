#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    import sys

    arg_v = sys.argv
    len_argv = len(arg_v) - 1  # Just arguments no file name

    if len_argv > 1:
        print(len_argv, "arguments:")
        for i in range(1, len_argv + 1):
            print("{:d}: {}".format(i, arg_v[i]))
    elif len_argv == 1:
        print(len_argv, "argument:")
        for i in range(1, len_argv + 1):
            print("{:d}: {}".format(i, arg_v[i]))
    elif len_argv == 0:
        print(len_argv, "arguments.")
