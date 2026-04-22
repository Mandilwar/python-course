def hello():
    print("Hello World")
hello()

hello_world = hello
hello_world()

def add():
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    res = n + m
    print(res)
add()

def greet(name):
    print(f'Hi {name}, Welcome to the Team')

greet("Umang Mandilwar")

def print_times(s_string, num_times):
    """
    Hi My Name is Umang Mandilwar
    I work in a pharma company named Eli Lilly since 17th July 2023.
    I love playing Cricket and Lawn Tennis
    """
    for i in range(num_times):
        print(s_string)
print_times.__doc__
print_times("Umang",3)

def square(x):
    y=x**2
    print(f"Square of {x} is ",y)
    return y
res=square(4)
print(res)

def square_cube(x):
    a = x**2
    b = x**3
    return a,b
res=square_cube(8)
print(res)

# Practice 1
def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b
res=max_of_two(3,8)
print(res)