import numpy as np
import random

def normalize_array(arr):
    return (arr - np.mean(arr)) / np.std(arr)

def scale_array(arr, factor=1.0):
    rand = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
    if factor == 1:
        return arr * rand[random.randint(0, 9)]
    return arr * factor