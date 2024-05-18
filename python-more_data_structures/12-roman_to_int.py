#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string):
    """
    Function that converts a Roman numeral to an integer.
    """
    if (not isinstance(roman_string, str)) or (roman_string is None):
        return 0
    roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    result = 0
    num = ""
    roman_string = roman_string[::-1]

    for letter in roman_string:
        num = roman_nums[letter]

        if num * 3 > result:
            result += num
        else:
            result -= num

    return result
