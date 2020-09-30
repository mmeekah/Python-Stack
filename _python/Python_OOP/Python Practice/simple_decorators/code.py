import functools
user = {"username": "Jose", "access_level":"guest"}




# def secure_get_admin():
#     if user["access_level"]=="admin":
#         return "1234"

def make_secure(func):  #func->get_admin_pwd
    @functools.wraps(func)
    def secure_function():
        if user["access_level"]=="admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function   


@make_secure
def get_admin_pwd():
    return "1234"


print(get_admin_pwd.__name__)