def typeCheck(t1, t2):
    def dec(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], t1) or not isinstance(args[1], t2):
                raise TypeError("Wrong types, man! You should be more careful with that thing")
            
            result = func(*args, **kwargs)

            return result
        return wrapper
    return dec

@typeCheck(int, int)
def add(a, b):
    return a + b

print(add(2, "lol"))