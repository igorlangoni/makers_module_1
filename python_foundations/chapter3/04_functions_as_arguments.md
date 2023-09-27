# Functions as Arguments

In chapter 1, you learned that functions are like little machines that take
inputs (arguments) and give back some outputs (return values). In this section,
you'll see that the arguments can also be other functions.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Assign a function to a variable
* Pass a function to another function as an argument
* Define a function that takes another function as an argument

## Part One: A Reminder

To declare a function, you use the `def` keyword, followed by the function's
name, then some parentheses, with any args inside, and a colon. The function
body goes below, indented once.

```python
>>> def hello(name):
...     return "hello " + name
...
>>>
```

If you type the name of a function, without parentheses, you just get the
function returned back to you.

```python
>>> hello
<function hello at 0x103b7da60>
```

## Part Two: Exercise I

What will happen if you do this. Try it now in a Python REPL.

```python
>>> def add(num1, num2):
...     return num1 + num2
...
>>> adder = add
>>> adder(1,2)
```

<details>
  <summary>Spoiler alert!</summary>

  We declared a new function, called add. Then assigned it to a variable and
  executed the function using the variable. If you do this in a Python REPL you
  should see `3` returned. Doing this demonstrates that we can 'pass
  functions around' the exact same way that we can pass around strings, or
  integers or any other object. You can assign them to variables and, as it
  turns out, you can pass them into other functions as arguments as well.

</details>

## Part Three: Flexible Functions

Flexibility is the name of the game, here. If you have, or can define, a
function that takes another function as an argument, you can start to combine
functions in interesting ways that bring a lot of flexibility.

Here's an example.

```python
def calculate_tax_for_the_shire(grossPay):
    # The friendly Shire has a 20% tax rate
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    # Dodgy Mirkwood has a 90% tax rate
    return grossPay * 0.9


def calculate_tax_for_mordor(grossPay):
    # Terrible Mordor has a 90% tax rate plus a fixed tax of £500.
    return grossPay * 0.9 + 500


def report_pay(gross_pay, calculate_tax):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"


print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(4320.0, calculate_tax_for_mirkwood))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

```

This is useful because it allows us to reuse the logic in `report_pay` with
different tax formulas without having to change `report_pay` at all, or do any
logic outside of the functions.

Consider putting the above in a Python file, running it, and playing around with
it. Try creating a new tax calculation function for a zero-tax, or a fixed tax
rate, and pass it in to `report_pay`.

## Part Four: Exercise II

### Weather Report

In this exercise you will create a weather reporting function that takes another
function as its argument.

Here are some instructions:

* Declare a function called `report_weather` that takes a temperature and a
  function as its two arguments
* Declare two other functions, each of which takes a temperature as an argument
  - One is called `as_sun_lover` and it returns 'great' if the temp is 25
    Celsius, or above. Otherwise it returns 'not great'
  - One is called `as_snow_lover` and it returns 'great' if the temp is
    0, or below. Otherwise it returns 'not great'
* Combine the functions to generate customised weather reports

#### Expected Behaviour

```python
>>>  report_weather(24, as_sun_lover)
'not great'
>>>  report_weather(25, as_sun_lover)
'great'
>>>  report_weather(1, as_snow_lover)
'not great'
>>>  report_weather(0, as_snow_lover)
'not great'
```

## Looking Ahead

In the next two sections, you'll learn how to do interesting things to lists and
dictionaries using methods that take functions as arguments.

## Reflect and Review

In this section, you learned that functions can be used as arguments.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

* How to assign a function to a variable
* How to pass a function as an argument
* How to define a function that takes a function as an argument


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=04_functions_as_arguments.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F05_advanced_lists.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F04_functions_as_arguments.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
