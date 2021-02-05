def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def combination(n, k):
    """
    calculate combination .. ..

    >>> combination(3, 1)
    3

    :param n:
    :param k:
    :return:
    """
    return factorial(n)/(factorial(k)*factorial(n-k))


def pascal(n):
    result = []
    for k in range(n+1):
        result.append(combination(n, k))

    return result


for j in range(1, 10):
    print(pascal(j))

