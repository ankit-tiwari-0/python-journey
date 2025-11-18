from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("acces denied: only admin")
        else:
            return func(user_role)
    return wrapper


@require_admin
def acces_tea(role):
    print("Acess granted to tea inventory")

acces_tea("user")
acces_tea("admin")    