# Demo Python scripts for inner functions
print("yeet")

def outer(num1):
    def inner_increment(num1):
        return num1+1
    num2 = inner_increment(num1)
    print(num1, num2)

# inner_increment(10)
outer(10)

def factorial(number):

    # Error Handling
    if not isinstance(number,int):
        raise TypeError("Sorry, 'number' must be an integer")
    if not number >= 0:
        raise ValueError("Sorry, 'number' must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)

# Call Outer Function
print(factorial(4))

##############
# Processing CSV of Wifi Hotspots in NYC

def process(file_name):

    def do_stuff(file_process):
        wifi_locations = {}

        for line in file_process:
            values = line.split(',')
            # Build the dict and increment values.
            wifi_locations[values[3]] = wifi_locations.get(values[3], 0) + 1

        max_key = 0
        for name, key in wifi_locations.items():
            all_locations = sum(wifi_locations.values())
            if key > max_key:
                max_key = key
                business = name

        print(f'There are {all_locations} WiFi hotspots in NYC, '
              f'and {business} has the most with {max_key}.')

    if isinstance(file_name, str):
        with open(file_name, 'r', encoding = "utf8") as f:
            do_stuff(f)
    else:
        do_stuff(file_name)

process('NYC_Wi-Fi_Hotspot_Locations.csv')

###############
# Messing with *args, a list of positional arguments

def test_var_args(f_arg, *argzzzzz):
    print("first normal arg:", f_arg)
    for arg in argzzzzz:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

# Messing with **kwargs, a dictionary of keyworded arguments

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s = %s" %(key,value))

greet_me(name="yasoob", ears="sam's ears")

kwargs = {"name": "yasoob", "ears": "sam's ears", "ears" : "mikey's ears"} # ears kwarg gets overwritten from "sam's ears" to "mikey's ears"
greet_me(**kwargs)

# Factory method for exponential function

def genexp(number):
    """
    Examples of use:

    >>> exp_two = genexp(2)
    >>> exp_three = genexp(3)
    >>> print(exp_two(7))
    128
    >>> print(exp_three(5))
    243
    """

    # Define the inner function ...
    def nth_power(power):
        return number ** power
    # ... that is returned by the factory function.

    return nth_power

exp_seven = genexp(7)
print(exp_seven(2))

###########
Using a decorator as a factory function to:
Take a function as an argument
Return a new function that includes the old function inside the closure

def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_2bytwo(n):
    return 2*n

print(raise_2bytwo(7))

@generate_power(2)
def raise_two(n):
    return(n)

print(raise_two(7))

@generate_power(3)
def raise_three(n):
    return n

print(raise_three(5))

#####
# Test dict with duplicate keys

testD = {"a": 1, "a": 2}
items = testD.items()
print(items)
