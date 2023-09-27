# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions based on some
# requirements.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do.
# Note that some solutions will require more than one line of code.
#
# Here is an example of the rules:
#
# Method name: add_ten
# Purpose: adds ten to the given number
# Rules:
#   Takes one number as an arg
#   Adds ten and returns the new value
# Example:
#   Call:    add_ten(5)
#   Returns: 15

# And here is an example of a correct solution:

def add_ten(number):
    new_number = number + 10
    return new_number

# Let's get started.

# == EXERCISES ==

# Method name: say_hello
# Purpose: returns the string 'hello'
# Arguments: none
# Example:
#   Call:    say_hello()
#   Returns: "hello"

def say_hello():
    return "hello"

# Method name: say_goodbye
# Purpose: returns the string 'goodbye'
# Arguments: none
# Example:
#   Call:    say_goodbye()
#   Returns: "goodbye"

def say_goodbye():
    return "goodbye"

# Method name: say_hello_to
# Purpose: greets the given name
# Arguments: one string
# Example:
#   Call:    say_hello_to("Sam")
#   Returns: "Hello, Sam!"

def say_hello_to(name):
    return f"Hello, {name}!"

# Method name: say_goodbye_to
# Purpose: says goodbye to the given name
# Arguments: one string
# Example:
#   Call:    say_goodbye_to("Sam")
#   Returns: "Goodbye, Sam!"

def say_goodbye_to(name):
    return f"Goodbye, {name}!"

# Method name: square
# Purpose: multiplies the given number by itself
# Arguments: one number
# Example:
#   Call:    square(5)
#   Returns: 25

def square(n1):
    return n1 * n1

# Method name: divisible_by_three
# Purpose: returns true if the given number is divisible by three
# Arguments: one number
# Example:
#   Call:    divisible_by_three(9)
#   Returns: True
#   Call:    divisible_by_three(10)
#   Returns: False

def divisible_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False

# Method name: add
# Purpose: adds two numbers together
# Arguments: two numbers
# Example:
#   Call:    add(5, 10)
#   Returns: 15

def add(n1, n2):
    return n1 + n2

# Method name: multiply
# Purpose: multiplies two numbers together
# Arguments: two numbers
# Example:
#   Call:    multiply(5, 10)
#   Returns: 50

def multiply(n1, n2):
    return n1 * n2

# Method name: add_number_strings
# Purpose: adds two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    add_number_strings("5", "10")
#   Returns: 15
# Note: return value should be a number, not a string

def add_number_strings(str1, str2):
    sum = int(str1) + int(str2)
    return sum

# Method name: multiply_number_strings
# Purpose: multiplies two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    multiply_number_strings("5", "10")
#   Returns: 50
# Note: return value should be a number, not a string

def multiply_number_strings(str1, str2):
    mult = int(str1) * int(str2)
    return mult

# Method name: both_odd
# Purpose: returns true if both numbers are odd
# Arguments: two numbers
# Example:
#   Call:    both_odd(5, 11)
#   Returns: True
#   Call:    both_odd(5, 10)
#   Returns: False
#   Call:    both_odd(6, 10)
#   Returns: False

def both_odd(n1, n2):
    if n1 % 2 == 0 or n2 % 2 == 0:
        return False
    else:
        return True

# Method name: both_even
# Purpose: returns true if both numbers are even
# Arguments: two numbers
# Example:
#   Call:    both_even(4, 10)
#   Returns: True
#   Call:    both_even(5, 10)
#   Returns: False
#   Call:    both_even(5, 11)
#   Returns: False

def both_even(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return True
    else:
        return False

# Method name: one_odd
# Purpose: returns true if at least one number is odd
# Arguments: two numbers
# Example:
#   Call:    one_odd(5, 10)
#   Returns: True
#   Call:    one_odd(5, 11)
#   Returns: True
#   Call:    one_odd(4, 8)
#   Returns: False

def one_odd(n1, n2):
    if n1 % 2 != 0 or n2 % 2 != 0:
        return True
    else:
        return False

# Method name: one_even
# Purpose: returns true if at least one number is even
# Arguments: two numbers
# Example:
#   Call:    one_even(5, 10)
#   Returns: True
#   Call:    one_even(4, 10)
#   Returns: True
#   Call:    one_even(5, 9)
#   Returns: False

def one_even(n1, n2):
    if n1 % 2 == 0 or n2 % 2 == 0:
        return True
    else:
        return False

# Method name: truncate_string
# Purpose: truncates (shortens) a string to 10 characters
# Arguments: one string
# Rules:
#   If the string is longer than 10 characters
#   return the first 10 characters followed by '...'
#   If the string is 10 characters or less
#   return the whole string
# Example:
#   Call:    truncate_string("This is a long string")
#   Returns: "This is a ..."
#   Call:    truncate_string("Short")
#   Returns: "Short"

def truncate_string(phrase):
    if len(phrase) <= 10:
        return phrase
    else:
        return phrase[0:10] + "..."

# Congrats, you're done with this file, go back to the Challenges README.
