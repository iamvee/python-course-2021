def decorator(f):
    def inner(s):
        return "00000" +f(s) + "00000"
    return inner


@decorator
def echo(s):
    return s


# echo = decorator(echo)

value = echo("hello")
print(value)
