#DECORATORS
"""
Decorators help us to add functionality to our functions while avoiding code redundancy 

FUNCTIONS AS FIRST CLASS OBJECTS
    In python functions are objects ,they can be saved as variables ,passed as arguments to other functions and returned by other functions

"""
#EXAMPLES
def hello(name):
    return "Hello" + " "+name

print(hello("dave"))

#storing a function in a variable
greeting=hello
print(greeting("irungu"))

# passed as arguments to other functions
def salutation(func):
    return func("Walter")

print(salutation(greeting))

#We can define function inside other functions (Inner functions)
def main_function(name):
    print(f'Hello {name}')
    
    def greet():
        print("GReetings")

    return greet

main_function("chibu")
#by returning greet without parenthesis () main_function is returning the function itself so that we can use it later on,to invoke the function later you can use
main_function("chibu")()

# if i had not return greet function,while there is print statement inside the greet function ,it wont be interpreted if greet is not invoked 

#Decorators
"""

To write your first decorator you need to write a function that 
    Takes a function as an argument
    Has an inner function defined inside of it
    returns the inner function

A decorator can be invoked by a function call() 0r @pie_syntax

"""


def decorator(func):
    def wrapper():
        print("I am the output that lets you know before function is about to be called")
        func()
        print("I am the output that lets you know the function has been called")
    
    return wrapper

def get_called():
    print("I am the function and I am being called.")
    
get_called=decorator(get_called)
get_called()

#use @ symbol to perform function decoration .this is called pie syntax

@decorator
def hello():
    print("hello ")

hello()

#When to use decorators
"""
the primary function of decorator is to reduce the amount of code that we write 
if you find yourslf writing the same code in diff functions,that a great opportunity to use decorators

"""
#eg
# def sweep_hours(time):
#     if 1100<time<2100:
#         print("sweeping the floors")
#     else:
#         print("I'm of duty")

# def wash_dishes(time):
#     if 1100<time<2100:
#         print("washing the dishes")
#     else:
#         print("I'm of duty")

# def chop_vegetables(time):
#     if 1100<time<2100:
#         print("chopping the vegetables")
#     else:
#         print("I'm of duty")

#refactored version
def checking_hours(func):
    def wrapper(time):
        if 1100<time<2100:
            func(time)
        else:
            print("I'm of duty")
    return wrapper

@checking_hours
def sweep_hours(time):
    print("sweeping the floors")

@checking_hours
def wash_dishes(time):
    print("washing the dishes")

@checking_hours
def chop_vegetables(time):
    print("chopping the vegetables")
    
sweep_hours(700)

#