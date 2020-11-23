import matplotlib.pyplot as mpl
import numpy as np
import math as math


def calculate_sum(array):
    random_sum = 0
    for random_value in array:
        random_sum += random_value
    return random_sum


def generate_two_dimensional_normal_random_value(dispersion_x, dispersion_y, standart_deviation_x, standart_deviation_y, correaltion):
    random_values = np.random.sample(6)
    print(random_values)
    sum = calculate_sum(random_values)
    print(sum)
    x = math.sqrt(2) * standart_deviation_x * (sum - 3) + dispersion_x
    dispersion = dispersion_y + correaltion * standart_deviation_x/standart_deviation_y * x - dispersion_x
    standart_deviation = standart_deviation_y * math.sqrt(1 - correaltion ** 2)
    a = np.random.sample(6)
    sum2 = calculate_sum(a)
    y = math.sqrt(2) * standart_deviation * (sum2 - 3) + dispersion
    return x, y


def generate_two_demensional_sequence(correlation):
    array = []
    for i in range(1000):
        array.append(generate_two_dimensional_normal_random_value(0, 0, 1, 1, correlation))
    array_x = [x for x, y in array]
    array_y = [y for x, y in array]
    mpl.figure()
    mpl.scatter(array_x, array_y)
    mpl.show()

