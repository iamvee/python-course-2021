def echo(s):
    return s


def change_string(s):
    return "*" + s + "*"


def echo_new(s):
    return change_string(echo(s))


value = echo_new("hello")
print(value)
