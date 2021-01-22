def calculator(a, b, operator='add'):
    if operator == 'add':
        return a + b
    elif operator == 'sub':
        return a - b
    elif operator == 'mul':
        return a * b
    elif operator == 'div':
        return a / b


print(calculator(10, 20))