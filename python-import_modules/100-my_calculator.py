#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_v = sys.argv
    len_argv = len(arg_v) - 1  # Just arguments no file name

    if len_argv == 3:
        a = int(arg_v[1])
        b = int(arg_v[3])
        operator = arg_v[2]

        if operator == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            exit(0)
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            exit(0)
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            exit(0)
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
