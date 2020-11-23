import matplotlib.pyplot as mpl
import lab1
import lab2
import lab3
import lab4


# lab1
random_sequence = lab1.generate_random_sequence(0, 4096, 150889, 714025)
print(random_sequence)


# lab2
even_distribution_sequence = lab2.generate_even_distribution(random_sequence)
print(even_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), even_distribution_sequence[:100])

exponential_distribution_sequence = lab2.generate_exponential_distribution(3, even_distribution_sequence)
print(exponential_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), exponential_distribution_sequence[:100])

normal_distribution_sequence = lab2.generate_normal_distribution(1, 2, exponential_distribution_sequence)
print(normal_distribution_sequence)
mpl.figure()
mpl.scatter(list(range(0, 100)), normal_distribution_sequence[:100])


# lab3




# lab4
lab4.generate_two_demensional_sequence(0.1)
lab4.generate_two_demensional_sequence(0.5)
lab4.generate_two_demensional_sequence(0.9)
