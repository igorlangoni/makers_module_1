# Defining Functions

Python's built in functions are nice, but we can go further. We can create our
own functions. In this step, you will learn how.

<!-- OMITTED -->
## Learning objectives

In this section, you will learn how to:
- Define your own functions

## Custom Functions

Imagine if you were writing a program to calculate an employee's monthly pay
after tax. The calculation would involve several steps:

1. Find their gross annual salary
2. Calculate their national insurance contribution
3. Calculate the income tax deduction
4. Calculate their pension contribution
5. Check if they're paying off a student loan. If they are, make the correct
   deduction.
1. Add a bonus, if they get one

Many of these steps could be further broken down into multiple sub-steps.

If you had to do this every time that you needed to show someone's net monthly
salary it would get tiresome and the codebase would get very large. What if you
could wrap all those steps in a custom function and then just call that function
when you need to do those calculations?

Your codebase would be more concise, less repetitive and, last but not least,
that long series of calculations would get its own meaningful name — the name
of the function.

## Part One: Your First Functions

Let's start with something simple. Do this in a Python REPL:

``` python
>>> def greet():
...     return "Hello!"
...
>>> greet()
'Hello!'
```

Let's look at this step by step:

* To define a function, we use the `def` keyword.
* Then we give the  function's name: `greet`
* Then some empty parentheses `()` (these will be used for arguments later)
* Then a colon `:`. This introduces a block of code, just like an `if` statement.


On the next line is where we write the function body, indicated by the
indentation.

Right now the `greet()` function does not take any arguments. We can tell that
because the parentheses are empty `()`.

Let's change it so we can pass in an argument to greet a specific person.

```Python
>>> def greet(name):
...     return f"Hello, {name}!"
...
>>> greet("Alex")
'Hello, Alex!'
```

Now it takes one argument, a person's name, and uses interpolation to return a
personal greeting. Nice!



Notice how function signature (the first line) defines `name`. This is
referenced later on line 2 where we do the interpolation. This is a variable
that will hold whatever name we provide when executing the function.

If we do this...

``` python
>>> greet("Mina")
'Hello, Mina!'
```

`"Mina"` is assigned to the `name` variable and `Hello, Mina!` is returned.

If we do this...

```Python
>>> greet("Bakary")
'Hello, Bakary!'
```

`"Bakary"` is assigned to the `name` variable and `Hello, Bakary!` is returned.

If we do this...

```Python
>>> greet("Rabiah")
'Hello, Rabiah!'
```

`"Rabiah"` is assigned to the `name` variable and `Hello, Rabiah!` is returned.

### Multiple arguments

So far, the functions we've defined only take a single argument (input) each.
What if you needed to provide multiple arguments? In this case, include them all
in the parentheses separated by commas.

For example:

```python
>>> def greet_everyone(name1, name2, name3):
...     return f"Hello {name1}, {name2} and {name3}!"
...
>>> greet_everyone("Mina", "Bakary", "Rabiah")
'Hello Mina, Bakary and Rabiah!'
```

## Over to You

In a new file, define and execute some functions, one for each task below...

* Add two numbers together
* Add three numbers together
* Concatenate the names of a few of your closest friends
* Calculate the number of seconds in X weeks, where X is a number (like 3)

## Printing vs Returning

You will have noticed that sometimes we use `print` and sometimes we use
`return`. You may have wondered whether they do the same thing, or when to use
one or the other.

Here are some rules of thumb you can use to decide which to use:

1. Is the value necessary to pass some automatic test? If so, use `return`.
2. Is the value the end-result of a function you have written? If so, use `return`.
3. Do you want to see the value purely to see what your program is doing? If so, use `print`.
4. Do you want to show you the end-user this value right away? If so, use `print`.

But what is the difference? Let's look at an example:

```python
# File: add_five.py
def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result = add_five(23)
print(result)
```

In this case we've got a function called `add_five` which adds five to a number
and `return`s the result. It also `print`s some debugging information so we can
see what it is doing. At the end, we call the function and assign its return
value to a variable `result`. We then `print` that `result`.

If you save this and run it you will get:

```shell
; python3 add_five.py
I have received 23
I have calculated 23 + 5 = 28
28
```

This is all as it should be.

Let's say we want to use `add_five` multiple times, like so:

```python
# File: add_five.py
def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result_1 = add_five(23)
result_2 = add_five(result_1)
result_3 = add_five(result_2)
print(result_3)
```

If you run this you will see:

```shell
; python3 add_five.py
I have received 23
I have calculated 23 + 5 = 28
I have received 28
I have calculated 28 + 5 = 33
I have received 33
I have calculated 33 + 5 = 38
38
```

Very nice! We're using `print` to show some debugging information to check what
our program is doing, and then `return` properly returns the result of the
function so it can be saved and used again.

This is using `return` and `print` properly.

If, however, we use `print` instead of `return`, let's see what happens:

```python
# File: add_five.py
def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    print(num_after_adding)

result_1 = add_five(23)
result_2 = add_five(result_1)
result_3 = add_five(result_2)
print(result_3)
```

```shell
; python3 add_five.py
I have received 23
I have calculated 23 + 5 = 28
28
I have received None
Traceback (most recent call last):
  File "add_five.py", line 9, in <module>
    result_2 = add_five(result_1)
  File "add_five.py", line 4, in add_five
    num_after_adding = num + 5
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Not so good. It seems like when we call `add_five` a second time it is getting
`None` instead of the right number!

This is because if we don't `return`, the function won't `return` its result to
be used by the code that called it. It will instead return the default value
`None`.

You can imagine `print` as saying "Python, show this value to the user and then
discard it — I don't care about it anymore!"

Whereas `return` says "Python, share this very important value with the person
who called me so that they can use it — after all I did spent a lot of effort
calculating it properly."

If you would like to check your understanding, try writing a function that when
called will return the right value below:

```python
def superify(name):
    pass # Fill out the function here instead of `pass`

# Don't edit below this line.

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"
```

## Reflect and Review

In this section we learned how to define functions.

**Please pause at this point to reflect and review your learning...**

In a few sentences, describe:

* The benefit of being able to define your own functions
* The syntax and structure of a function


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=10_defining_functions.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F11_putting_chapter_1_into_practice.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F10_defining_functions.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
