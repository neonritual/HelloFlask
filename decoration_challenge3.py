####
## CHALLENGE:
## Create a logging_decorator() which is going to log the name of the function that was called,
# the arguments it was given and finally the returned output.
####

def logging_decorator(function):
    def wrapper(*args):
        return f"You called {function.__name__}{args}, and it returned: {function(args[0], args[1])}"
    return wrapper

@logging_decorator
def good_pet(name, species):
    return f"{name} is a good {species}."


print(good_pet('maru', 'cat'))
