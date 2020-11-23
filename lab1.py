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



