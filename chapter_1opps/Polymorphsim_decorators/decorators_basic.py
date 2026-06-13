'''A decorator is a function that adds extra functionality to
another function without changing its original code.'''

'''A decorator must return a function, not execute it immediately.
So we create wrapper() and return it using'''

def my_decorator(func):
    def wraper():
        print("Before function call")
        func()
        print("After function call")
    return wraper
@ my_decorator
def hello():
    print("I am the function call")
hello()

# math exmple 

def math_decorator(func):
    def wrapper(a,b):
        print("My fucction is to perfom math operations in  elemnts")
        func(a,b)
        print(f"addition of 2 numbers is {a+b}")
        print(f"The substracion is {a-b}")
        print(f"The multiplication is {a*b}")
    return wrapper
@ math_decorator

def math(a,b):
    print("see the magic")
math(5,2)

        
