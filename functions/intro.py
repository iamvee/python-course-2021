def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def pascal(n):
    result = []
    for k in range(n+1):
        temp = factorial(n)/(factorial(k)*factorial(n-k))
        result.append(temp)

    return result


for j in range(1, 10):
    print(pascal(j))

