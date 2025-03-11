import math
'''
def calculateArea(type):
    if type == "circle":
        ray = int(input("Insert ray length >  "))
        return ray**2*math.pi
    if type == "rectangle":
        base = int(input("Insert Base length >  "))
        height = int(input("Insert Height length >  "))
        return base*height        
    if type == "square":
        line = int(input("Insert Line length >  "))
        return line**4

if __name__ == "__main__":
    print(calculateArea(str(input("Insert a Type of shape [Circle, Rectangle, Square] >  ")).lower()))
'''


# 1. Basic function
def greet(name):
    """This function greets the person by name."""
    return f"Hello, {name}!"

# 2. Function with default argument
def greet_default(name="World"):
    """This function greets the person with a default name."""
    return f"Hello, {name}!"

# 3. Function with variable number of arguments (*args)
def print_all(*args):
    """This function prints all passed arguments."""
    for arg in args:
        print(arg)

# 4. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    """This function prints all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 5. Lambda function (Anonymous function)
add = lambda a, b: a + b
square = lambda x: x ** 2

# 6. Recursive function
def factorial(n):
    """This function computes the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 7. Function with nested function
def outer_func(x):
    """This function demonstrates a nested function."""
    def inner_func(y):
        return y + 1
    return inner_func(x)

# 8. Higher-order function (Function returning a function)
def power(n):
    """Returns a function that raises its input to the power of n."""
    return lambda x: x ** n

# 9. Function with exception handling
def divide(x, y):
    """Divides x by y, with exception handling."""
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except Exception as e:
        return f"An error occurred: {e}"

# 10. Function with a docstring
def multiply(x, y):
    """
    Multiplies two numbers.
    
    Parameters:
    x (int or float): The first number
    y (int or float): The second number
    
    Returns:
    int or float: The product of x and y
    """
    return x * y

# Special Characters and Escape Sequences
# 11. Using special characters
def special_characters():
    # Newline
    print("Hello\nWorld!")
    
    # Tab space
    print("Hello\tWorld!")
    
    # Backslash
    print("C:\\Program Files\\MyApp")
    
    # Single and double quotes inside a string
    print('It\'s a great day!')
    print("He said, \"Hello!\"")

    # Raw string (useful for paths in Windows)
    print(r"C:\Users\Name\Documents")
    
    # Multiline string
    print("""This is a
    multiline string!""")
    
    # String formatting with f-string
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    
    # String formatting with format()
    print("Hello {}. You are {} years old.".format(name, age))

# 12. Special Commands
def special_commands():
    # Use of the pass statement (does nothing)
    def empty_function():
        pass  # Placeholder for future code
    
    # Use of assert statement (checks for conditions)
    assert 3 > 2, "This should never fail"
    
    # Use of the global statement
    counter = 0
    def increment():
        counter = 0
        #counter = 0
        counter += 1
    increment()
    print("Global counter:", counter)

    # Use of nonlocal statement (refers to variables in the nearest enclosing scope)
    def outer():
        a = 10
        def inner():
            nonlocal a
            a += 5
        inner()
        print("Value of a after nonlocal:", a)
    
    outer()

# 13. Special Python Commands
def special_python_commands():
    # eval() - Executes a string as Python code
    expression = "3 + 5"
    result = eval(expression)
    print(f"Result of eval: {result}")
    
    # exec() - Executes Python code dynamically (can execute multiple lines)
    code = """
def foo():
    return 'Hello from foo!'
result = foo()
"""
    exec(code)
    print(f"Result of exec: {result}")
    
    # dir() - List all the attributes of an object
    print("Attributes of list:", dir(list))
    
    # help() - Display documentation
    '''help(str)  # Display help for str class'''

# 14. Special Characters in Strings
def special_characters_in_strings():
    # Unicode characters
    print("Smiley face: \u263A")
    
    # ASCII Characters
    print("Arrow: \x2192")
    
    # Other special characters
    print("Tab character:\tThis is a tab")
    print("Newline character:\nThis is a new line")

# 15. Decorators
def my_decorator(func):
    """A simple decorator that prints a message before calling a function."""
    def wrapper(*args, **kwargs):
        print("Function is being called...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# 16. Context Manager (using with statement)
class MyContextManager:
    def __enter__(self):
        print("Entering the context...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context...")
        if exc_type:
            print(f"An exception occurred: {exc_val}")

def context_manager_example():
    with MyContextManager():
        print("Inside the context...")
        # Uncomment the next line to test exception handling
        # raise ValueError("An error occurred inside the context!")

# 17. Function annotations (type hints)
def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

# 18. Using break and continue in loops
def break_continue_example():
    for i in range(10):
        if i == 5:
            break  # Stop the loop when i equals 5
        print(i)
    
    for i in range(10):
        if i == 5:
            continue  # Skip the iteration when i equals 5
        print(i)

# Main function to run examples
if __name__ == "__main__":
    print(greet("Alice"))
    print(greet_default())
    print(f"Sum using lambda: {add(10, 20)}")
    print(f"Square using lambda: {square(5)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(outer_func(10))
    
    power_of_2 = power(2)
    print(f"2 to the power of 3: {power_of_2(3)}")
    
    print(divide(10, 2))
    print(divide(10, 0))
    
    print(multiply(2, 3))
    
    special_characters()
    special_commands()
    special_python_commands()
    special_characters_in_strings()
    say_hello("Bob")
    context_manager_example()
    break_continue_example()
    print(add_numbers(5, 7))
