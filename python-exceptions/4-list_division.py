#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """
    Function that divides element by element 2 lists.
    """
    new_list = []
    result_div = 0

    for i in range(0, list_length):
        try:
            result_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result_div = 0
        except ZeroDivisionError:
            print("division by 0")
            result_div = 0
        except IndexError:
            print("out of range")
            result_div = 0
        finally:
            new_list.append(result_div)

    return new_list
