from math import factorial


def combination(n, k):
    """
    calculate combination .. ..

    >>> combination(3, 1)
    3.0
    >>> combination(4, 2)
    6.0

    :param n:
    :param k:
    :return:
    """
    return factorial(n)/(factorial(k)*factorial(n-k))


if __name__ == '__main__':
    import doctest
    doctest.testmod()