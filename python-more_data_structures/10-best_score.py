#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """
    Function that returns a key with the biggest integer value.
    """
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None

    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    best = values[0]
    key_best = keys[0]

    for i in range(1, len(values)):
        if values[i] > best:
            best = values[i]
            key_best = keys[i]

    return key_best

