import matplotlib.pyplot as mpl
import numpy as np


def replace_zeros(data):
    min_nonzero = np.min(np.nonzero(data))
    data[data == 0] = min_nonzero
    return data


def calculate_unique_number(number, a, c, restriction):
    return (number * a + c) % restriction


def generate_random_sequence(number, a, c, restriction):
    first_value = 0
    numbers = [number]
    while len(numbers) <= restriction:
        number = calculate_unique_number(number, a, c, restriction)
        if number == first_value:
            break
        numbers.append(number)
    print(len(numbers))
    return numbers


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


random_sequence = generate_random_sequence(0, 4096, 150889, 714025)
print(random_sequence)

even_distribution_sequence = generate_even_distribution(random_sequence)
print(even_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), even_distribution_sequence[:100])


exponential_distribution_sequence = generate_exponential_distribution(3, even_distribution_sequence)
print(exponential_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), exponential_distribution_sequence[:100])

normal_distribution_sequence = generate_normal_distribution(1, 2, exponential_distribution_sequence)
print(normal_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), normal_distribution_sequence[:100])



