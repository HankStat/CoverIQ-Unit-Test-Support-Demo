import pytest
import numpy as np
from array_ops import normalize_array, scale_array
import random

def generate_random_array(length, min_value, max_value):
    # Generates a random array of integers.
    random_array = []
    for _ in range(length):
        random_array.append(random.randint(min_value, max_value))
    return random_array

def test_normalize_random_array():
    arr = np.array(generate_random_array(5, 0, 10))
    norm_arr = normalize_array(arr)
    np.testing.assert_allclose(norm_arr.mean(), 0, atol=1e-06)
    np.testing.assert_allclose(norm_arr.std(), 1, atol=1e-06)

def test_scale_array():
    arr = np.array([1, 2, 3])
    scaled = scale_array(arr, factor=2.5)
    np.testing.assert_allclose(scaled, np.array([2.5, 5.0, 7.5]), rtol=1e-05)
