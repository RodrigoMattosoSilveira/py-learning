import numpy as np
import random
from math import trunc


def get_random_normal(_mu, _sigma):
    # print('mu:', _mu)
    # print('sigma:', _sigma)
    i = random.randint(0, 999)
    s = np.random.normal(_mu, _sigma, 1000)
    return trunc(s[i] + 0.5)


def get_random_pareto(a, m):
    # print('mu:', _mu)
    # print('sigma:', _sigma)
    s = (np.random.pareto(a, 1000) + 1) * m
    j = random.randint(1, 100)
    random_number = trunc(s[j] + 0.5)
    return random_number


def get_random_poison(a):
    # print('mu:', _mu)
    # print('sigma:', _sigma)
    s = np.random.poisson(a, 1000)
    j = random.randint(1, 100)
    random_number = trunc(s[j] + 0.5)
    return random_number


# Random Number Generator Arbitrary Probability Distribution
# Utility function to find ceiling of r in arr[length..h]
def find_ceil(arr, r, length, h):
    while length < h:
        mid = length + ((h - length) >> 1)  # Same as mid = (length+h)/2
        if r > arr[mid]:
            length = mid + 1
        else:
            h = mid

    if arr[length] >= r:
        return length
    else:
        return -1


# Random Number Generator Arbitrary Probability Distribution
def rng_apd(arr, freq, n):

    # Create and fill prefix array
    prefix = [0] * n
    prefix[0] = freq[0]
    for i in range(n):
        prefix[i] = prefix[i - 1] + freq[i]
    print(prefix)
    # prefix[n-1] is sum of all frequencies.
    # Generate a random number with
    # value from 1 to this sum
    r = random.randint(0, prefix[n - 1]) + 1

    # Find index of ceiling of r in prefix array
    index_c = find_ceil(prefix, r, 0, n - 1)
    print(index_c)
    return arr[index_c]
