# a decorator takes another function as an argument and extends the behaviour of that function
# there are function decorators and class decorators
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper():
        # can do something before the function
        print("start")
        func()
        # can do something after the function
        print('end')
    return wrapper

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@start_end_decorator #this makes the print_name function act as the decorator
@debug
def print_name():
    print("Ahmed")

print_name() #calling first debug, then start_end_decorator, then print_name. (called in the order they are listed)

#another example use this as template
import functools #optional but useful

def decorator(func):
    @functools.wraps(func) #optional but useful
    def wrapper(*args, **kwargs):
        #do something before function
        print('hello')
        result = func(*args, **kwargs)
        #do something after function
        print('end')
        return result
    return wrapper

@decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)


#another example, decorator within functions

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet("Ahmed")

#decorators for classes
import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")
    
say_hello()
say_hello()