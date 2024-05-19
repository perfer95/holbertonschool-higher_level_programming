#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """
    Function that prints the first x elements of a list and only integers.
    """
    count = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
        except ValueError:
            continue

    print("")
    return count
