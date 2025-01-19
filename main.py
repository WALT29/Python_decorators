#DECORATORS



"""
Decorators help us to add functionality to our functions while avoiding code redundancy 

FUNCTIONS AS FIRST CLASS OBJECTS
    In python functions are objects ,they can be saved as variables ,passed as arguments to other functions and return by other functions

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