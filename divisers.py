def diviser(n):
    return sum(n % i == 0 for i in range(1, 10))