import datetime

def timing(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now().time().microsecond
        result = func(*args, **kwargs)
        end = datetime.datetime.now().time().microsecond
        print(f"Time passed: {end - start}")
        return result
    return wrapper

@timing
def someAbsolutelyRandomFunction():
    for i in range(10 ** 3):
        for j in range(10 ** 3):
            0 == 0
    return "What?"

someAbsolutelyRandomFunction()