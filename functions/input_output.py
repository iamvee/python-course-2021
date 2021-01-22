def my_sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result


val = my_sum(10, 20, 10, 1)
print(val)
