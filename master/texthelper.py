import numpy as np


def rollover(text, max_len):
    return_list = []
    return_list = [text[i:i+max_len] for i in range(0, len(text), max_len)]

    return return_list

