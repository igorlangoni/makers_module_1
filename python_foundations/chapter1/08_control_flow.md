# Control Flow

If you were asked you to print `'Hello World'`, to the terminal, you might find
this a quick and simple step. If you were asked to print `'Hello World'` to the
terminal a thousand times, you might (quite rightly) think this to be a rather
time consuming, and no doubt, excruciatingly boring task.

Sometimes we want to execute sections of code repeatedly. When all is said and
done, is not the purpose of programming to make our job of manually inputting
instructions easier? For repetitive tasks, such as searching meticulously
through a big set of data, or adding a single value to a large list; we can use
loops.

Loops are a way of giving an instruction and executing some code to either a
*fixed* number of iterations, or to continue doing a task until a *condition* is
met.

<!-- OMITTED -->

## Learning Objectives

In this section you will learn to:

* Execute code repeatedly using _for loops_.
* Execute code repeatedly using _while loops_.

## Part One: For Loops

Let's go back to our earlier example. If I asked you to print `'Hello World'` to
the terminal, you might write something like this:

``` python
>>> print('Hello World')
```

And you would be right. But if you needed to execute that line multiple times,
it would be easier to nest that `print()` method in a loop. Specifically, a
`for` loop:

```python
>>> for i in range(5):
...     print('Hello World')
```

How did that go in your terminal? Let's break down what is happening in this
`for` loop. Give these examples a go in your Python REPL:

``` python
>>> for number in range(10):
...     print(number)
... 
0
1
2
3
4
5
6
7
8
9
```

After the keyword `for` we use a `loop variable`, sometimes called an `index
variable`. In our first example we used the letter `i`, you will see this
a lot in the Python documentation and online. Commonly, the `i` stands for
index.

But we can use any name we like. This is why in the second example we use
`number` to store each number as it iterates (loops over) through the
`range(10)`.

<details>
  <summary>:speech_balloon: What is <code>range(10)</code>?</summary>

  <hr>
  
  `range` is a function that returns a special data type called a range. You can
  imagine this as a list of the numbers starting from zero and ending just
  before the number you give it.

  So `range(5)` is a range including `0, 1, 2, 3, 4`.

  <hr>
</details>

Here is an example of a `for` loop that increments a number in a variable.

```python
>>> num = 10
>>> for i in range(5):
...     num = num + 5
...     print(num)
>>> # What do you think this will print?
```

The method `range()` can do even more. Take a look at this example:

``` python
>>> for i in range(0, 10, 2):
...     print(i)
... 
0
2
4
6
8
```

Here we are iterating over a range starting at zero, going up by steps of two,
stopping just before ten. 

The generic syntax for `range` is `range(start_at, stop_before, step_by)`.

With that in mind, try to print all of the odd numbers starting with one and
ending with 31.

``` python
>>> for i in range(???, ???, ???):
...     print(i)
...
```

### Iterating over strings

We can also use `for` loops to iterate over characters in a string. Take a look
at this example:

``` python
>>> name = "Eric"
>>> for char in name:
...     print("Give me a " + char + " !") 
>>> #???
```

Remember in the [methods](./04_methods.md) step where we mentioned that the
Python `string` data type is part of a family of data types called `sequence`s? 

Due to this fact we can also iterate through strings. This sort of iteration
will become much more handy when we begin to look at more complex data
structures like lists and dictionaries.


## Part Two: While Loops

For loops are very useful when we want to loop through something a *specific*
amount of times or when the length of a piece of data is known. 

But what about when we do not know how long it might take to find something, or
if we need to loop until a condition is met?

This is where `while` loops become useful.

Consider this example:

```python
>>> # This next line imports a function from a Python library.
>>> # Don't worry about it too much for now.
>>> from random import randint
>>> fav_number = 77
>>> guess_correct = False
>>>
>>> while not guess_correct:
...     guess = randint(0, 100)
...     if guess == fav_number:
...         print("You guessed right: 77!")
...         guess_correct = True
...     else:
...         print(f"{guess} is wrong! Try again.")
```

This program generates random guesses at my favourite number (`77`). It keeps
looping until it hits on the right one and then ends the loop.

Try running it and carefully examining it to see how it works.

### Infinite Loops

Let's imagine that I made a mistake in the program:

```python
>>> # This next line imports a function from a Python library.
>>> # Don't worry about it too much for now.
>>> from random import randint
>>> fav_number = 500 # !!!
>>> guess_correct = False
>>>
>>> while not guess_correct:
...     guess = randint(0, 100)
...     if guess == fav_number:
...         print("You guessed right: 500! But... how?")
...         guess_correct = True
...     else:
...         print(f"{guess} is wrong! Try again.")
```

If you run that program you will find that it never stops!

So is that it, we can never use our terminal again? Nope, you can always get out
of a program by hitting `Ctrl + C` on your keyboard.

Try it out with this program:

``` python
>>> while True:
...	    print("This will run foreverrrrrr!")
...     # Hit `ctrl + c` to stop this nonsense
...
```

## Reflect and Review

In this section we covered `for` loops and `while` loops and how they can be
used in a program. These will come in particularly useful when you learn about
lists and dictionaries.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
* What is meant by a loop?
* How the `for` and `while` loops differ? Why would you use one over the other?
* How to escape an infinite loop!
* How can you loop from 50 to 100 in steps of 3?


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=08_control_flow.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F09_executing_python_files.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F08_control_flow.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
