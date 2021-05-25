def val_checker(lamda_func):
    def _val_checker(func):
        def wrapper(arg):
            if lamda_func:

        return wrapper
    return _val_checker
return val_checker






@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
