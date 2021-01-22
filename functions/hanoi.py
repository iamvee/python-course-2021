def hanoi(n, start, middle, stop):
    if n == 1:
        print(start, '-->', stop)
    else:
        hanoi(n-1, start, stop, middle)
        hanoi(1, start, middle, stop)
        hanoi(n - 1, middle, start, stop)


hanoi(3, 'A', 'B', 'C')
