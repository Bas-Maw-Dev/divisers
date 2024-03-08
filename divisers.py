def diviser(n):
    number_of_divisers = 0
    for i in range(1, 10):
        if n % i == 0:
            number_of_divisers += 1
    return number_of_divisers