def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):

        result = 1
        if args in cache:
            result = cache[args]
            print(f"In decorator: {result}")
        else:
            result = func(*args, **kwargs)
            cache[args] = result

        return result
    return wrapper

@cache
def func(a):
    a = a ** 2
    print(f"Not in decorator: {a}")
    return a

func(2)
func(3)
func(4)
func(2)