# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
# Each one takes a single argument.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Delete and replace the `pass` placeholder with your own code — it is just
#   filler.
#
# * You may be required to write for loops, use control flow, slice notation,
#   and string methods.
#
# * Just exactly returning the example return won't work — you'll need to think
#   about the purpose of the function and fulfil that.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: return the string uppercase
# Example:
#   Call:    block_caps_a_string("hello world")
#   Returns: "HELLO WORLD"
def block_caps_a_string(string):
    # your code goes here (delete the pass below)
    return string.upper()



# Purpose: return the string lowercase
# Example:
#   Call:    lower_case_a_string("HELLO WORLD")
#   Returns: "hello world"
def lower_case_a_string(string):
    # your code goes here (delete the pass below)
    return string.lower()


# Purpose: return the length of the string
# Example:
#   Call:    length_of_a_string("hello")
#   Returns: 5
def length_of_a_string(string):
    # your code goes here (delete the pass below)
    return len(string)


# Purpose: return the string reversed
# Example:
#   Call:    reverse_a_string("hello")
#   Returns: "olleh"
def reverse_a_string(string):
    # your code goes here (delete the pass below)
    return string[len(string)::-1]


# Purpose: return the string with uppercase swapped to lowercase and vice versa
# Example:
#   Call:    swap_the_case_of_a_string("Hello World")
#   Returns: "hELLO wORLD"
def swap_the_case_of_a_string(string):
    # your code goes here (delete the pass below)
    return string.swapcase()



# Purpose: checks if the number given is odd
# Example:
#   Call:    is_integer_odd(1)
#   Returns: True
#   Call:    is_integer_odd(2)
#   Returns: False
def is_integer_odd(integer):
    # your code goes here (delete the pass below)
    if integer % 2 == 0:
        return False
    else:
        return True


# Purpose: checks if the number given is even
# Example:
#   Call:    is_integer_even(1)
#   Returns: False
#   Call:    is_integer_even(2)
#   Returns: True
def is_integer_even(integer):
    # your code goes here (delete the pass below)
    if integer % 2 == 0:
        return True
    else:
        return False


# Purpose: converts an integer to a float
# Example:
#   Call:    integer_to_float(1)
#   Returns: 1.0
def integer_to_float(integer):
    # your code goes here (delete the pass below)
    return float(integer)


# Purpose: converts an integer to a string
# Example:
#   Call:    integer_to_string(1)
#   Returns: "1"
def integer_to_string(integer):
    # your code goes here (delete the pass below)
    return str(integer)


# Purpose: returns the integer one lower than the one given
# Example:
#   Call:    return_one_lower(4)
#   Returns: 3
def return_one_lower(integer):
    # your code goes here (delete the pass below)
    return integer-1


# Purpose: returns the integer one higher than the one given
# Example:
#   Call:    return_one_higher(4)
#   Returns: 5
def return_one_higher(integer):
    # your code goes here (delete the pass below)
    return integer+1


# Purpose: rounds a float up to the nearest integer
# Example:
#   Call:    round_up(4.5)
#   Returns: 5
def round_up(float):
    # your code goes here (delete the pass below)
    return int(round(float+0.5))


# Purpose: rounds a float down to the nearest integer
# Example:
#   Call:    round_down(4.5)
#   Returns: 4
def round_down(float):
    # your code goes here (delete the pass below)
    return int(round(float-0.5))


# Purpose: converts a float to a string
# Example:
#   Call:    float_to_string(1.0)
#   Returns: "1.0"
def float_to_string(float):
    # your code goes here (delete the pass below)
    return str(float)


# Purpose: converts a float to an integer
# Example:
#   Call:    float_to_integer(1.0)
#   Returns: 1
def float_to_integer(float):
    # your code goes here (delete the pass below)
    return int(float)


# Purpose: checks if a float is positive
# Example:
#   Call:    float_is_positive(1.0)
#   Returns: True
#   Call:    float_is_positive(-1.0)
#   Returns: False
def float_is_positive(float):
    # your code goes here (delete the pass below)
    if float > 0:
        return True
    else:
        return False


# Purpose: checks if a float is negative
# Example:
#   Call:    float_is_negative(1.0)
#   Returns: False
#   Call:    float_is_negative(-1.0)
#   Returns: True
def float_is_negative(float):
    # your code goes here (delete the pass below)
    if float < 0:
        return True
    else:
        return False


# Purpose: converts a boolean to a string
# Example:
#   Call:    boolean_to_string(True)
#   Returns: "True"
def boolean_to_string(boolean):
    # your code goes here (delete the pass below)
    return str(boolean)


# Congrats, you're done with this file. Move on to the next one.
