def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Executing function name is {func.__name__}")
        result= func(*args,**kwargs)
        print(f"Finished executing function {func.__name__}")
        return result
    return wrapper

@decorator
def greet():
    print("Hello !!")

greet()