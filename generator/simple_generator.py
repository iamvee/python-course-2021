def my_generator():
    yield 10
    yield 20
    yield 3
    yield 15


gen = my_generator()
lst = [10, 20, 3, 15]

for i in gen:
    print(i)