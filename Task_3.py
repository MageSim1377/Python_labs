import datetime

def log_calls(ы):
    def dec(func):
        def wrapper(*args, **kwargs):
            
            result = func(*args, **kwargs)

            with open(ы, "a") as file:
                file.write(f"{datetime.datetime.now()}, {func.__name__}, {args}\n")

            return result
        return wrapper
    return dec

@log_calls("log.txt")
def someFunc(a, b, c):
    print(f"{a + b + c}")

someFunc(1, 2, 3)