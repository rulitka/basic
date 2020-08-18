def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        first_number = int(str(abs(result))[0])
    return first_number
