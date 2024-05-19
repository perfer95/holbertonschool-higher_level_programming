#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """
    Function that divides 2 integers and prints the result.
    """
    result_div = 0

    try:
        result_div = a / b
    except ZeroDivisionError:
        result_div = None
    except TypeError:
        result_div = None
    finally:
        print("Inside result: {}".format(result_div))

    return result_div
