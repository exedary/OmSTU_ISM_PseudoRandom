import numpy as np


def replace_zeros(data):
    min_nonzero = np.min(np.nonzero(data))
    data[data == 0] = min_nonzero
    return data


def generate_even_distribution(sequence):
    even_distribution = []
    sequence_len = len(sequence)
    for randomValue in sequence:
        even_distribution.append(randomValue / sequence_len)
    return even_distribution


def generate_exponential_distribution(lambda_value, even_sequence):
    exponential_distribution = []
    even_sequence = replace_zeros(even_sequence)
    for even_value in even_sequence:
        exponential_distribution.append(-lambda_value * np.log(even_value))
    return exponential_distribution


def generate_normal_distribution(a, sigma, exp_sequence):
    normal_distribution = []
    for exponential_value in exp_sequence:
        normal_distribution.append(sigma * exponential_value + a)
    return normal_distribution
