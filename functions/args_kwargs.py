def temp_fun(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get('mode'))


temp_fun(1, 2, 3, 4, 5, whatever=100, mode="sdfjsdkjfsdl")