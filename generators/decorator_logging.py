from functools import wraps

def log_activity(func):
    @wraps(func)

    def wrapper(*arg, **kwargs):
        print(f"calling: {func.__name__}")
        result = func(*arg, **kwargs)
        print(f"Fini: {func.__name__}")
        return result
    return wrapper


@log_activity
def brew_chai(type, milk="goat milk"):
    print(f"Brewing {type} chai and milk type {milk}")

brew_chai("mashala")    