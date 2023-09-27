import datetime

# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# Some will have no methods. Some will have one or two simple methods. Some will
# have more complex methods.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: Greeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = Greeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution follows.

class Greeter():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return 'Hello, ' + self.name + "!"

    def say_goodbye(self):
        return 'Goodbye, ' + self.name + "!"


# == EXERCISES ==

# Class name: Animal
# Purpose: a generic animal
# Methods:
#   1. Name: __init__
#      Arguments: none
#   No other methods required
# Example usage:
#   > animal = Animal()
#   > animal
#   <Animal object at 0x7f8b8c0b8e80>

class Animal():
    def __init__(self):
        pass


# Class name: Vehicle
# Purpose: a generic vehicle
# Methods:
#   1. Name: __init__
#      Arguments: none
#   No other methods required
# Example usage:
#   > vehicle = Vehicle()
#   > vehicle
#   <Vehicle object at 0x7f8b8c0b8e80>

class Vehicle():
    def __init__(self):
        pass

# Class name: Cat
# Purpose: miaows at the user
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: speak
#      Arguments: none
#      Returns: the string 'miaow'
# Example usage:
#   > cat = Cat()
#   > cat.speak()
#   'miaow'


class Cat():
    def __init__(self):
        pass

    def speak(self):
        return "miaow"


# Class name: Dog
# Purpose: woofs at the user
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: speak
#      Arguments: none
#      Returns: the string 'woof'
# Example usage:
#   > dog = Dog()
#   > dog.speak()
#   'woof'

class Dog():
    def __init__(self):
        pass

    def speak(self):
        return "woof"

# Class name: StringFormatter
# Purpose: transforms strings
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: block_caps
#      Arguments: one, a string
#      Returns: the string in block caps
#   3. Name: lower_case
#      Arguments: one, a string
#      Returns: the string in lower case
# Example usage:
#   > string_formatter = StringFormatter()
#   > string_formatter.block_caps('hello')
#   'HELLO'
#   > string_formatter.lower_case('HELLO')
#   'hello'

class StringFormatter():
    def __innit__(self):
        pass

    def block_caps(self, phrase):
        return phrase.upper()
    
    def lower_case(self, phrase):
        return phrase.lower()

# Class name: Calculator
# Purpose: performs basic arithmetic
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(2, 3)
#   6
#   > calculator.subtract(3, 2)
#   1
#   > calculator.divide(6, 2)
#   3.0

class Calculator():
    def __init__(self):
        pass

    def add(self, n1, n2):
        return n1 + n2
    
    def multiply(self, n1, n2):
        return n1 * n2
    
    def subtract(self, n1, n2):
        return n1 - n2
    
    def divide(self, n1, n2):
        return n1 / n2

# Class name: Apprentice
# Purpose: represents an apprentice
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the apprentice's name
#   2. Name: cohort
#      Type: string
#      Purpose: the cohort the apprentice is in
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name, one string representing a cohort
#   2. Name: format_details
#      Arguments: none
#      Returns: the name and cohort, separated by one comma and one space
# Example usage:
#   > apprentice = Apprentice('Rita Smith', 'June 2030')
#   > apprentice.name
#   'Rita Smith'
#   > apprentice.cohort
#   'June 2030'
#   > apprentice.format_details()
#   'Rita Smith, June 2030'

class Apprentice():
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    
    def format_details(self):
        return f"{self.name}, {self.cohort}"

# Class name: Cohort
# Purpose: represents a cohort
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the cohort name
#   2. Name: start_date
#      Type: Date
#      Purpose: the cohort start date
#   3. Name: end_date
#      Type: Date
#      Purpose: the cohort end date
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name,
#                 one string representing a start_date,
#                 one string representing an end_date
#   2. Name: calculate_duration
#      Arguments: none
#      Returns: the number of days between start_date and end_date
# Example usage:
#   > cohort = Cohort('June 2020', '2020-06-01', '2020-09-01')
#   > cohort.name
#   'June 2020'
#   > cohort.start_date
#   datetime.date(2020, 6, 1)
#   > cohort.end_date
#   datetime.date(2020, 9, 1)
#   > cohort.calculate_duration()
#   92

class Cohort():
    from datetime import datetime, timedelta

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = datetime.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:]))
        self.end_date = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:]))
    
    def calculate_duration(self):
        long = self.end_date - self.start_date
        return long.days


