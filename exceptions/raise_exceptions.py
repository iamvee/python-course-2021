class NegativeValueForFactorialError(Exception):
    pass


def factorial(n):
    if type(n) != int:
        raise Exception

    if n < 0:
        raise NegativeValueForFactorialError(f"{n} is negative; negative values are not allowed")
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

1/0
print(factorial(-1))
try:
    print(factorial(-1))
except NegativeValueForFactorialError:
    print("my plan")