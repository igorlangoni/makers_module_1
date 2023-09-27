# Functions

In this section, you will learn about functions. This will get you a step closer
to being able to build the first challenge of this module, a password validator.


<!-- OMITTED -->

## Learning Objectives

In this section, you'll learn to:

* Explain what a function is
* Explain what a function's arguments are
* Explain why functions are useful
* Find more information about Python's built-in functions

## Part One: What are Functions?

Functions are like little machines that take inputs, called arguments, and
provide outputs, called return values.

Here are some analogies:
* A toaster, which takes bread as an input and returns toast.
* A blender, which takes fruit as an input and returns a smoothie.
* A printer, which takes paper and some text data as inputs and returns a
  document, with the text data printed on it.

We are going to start using some functions that are built in to Python. In a
later step you will create your own functions.

Here is the generic syntax for using ('calling') a function:

```python
functionName(argument1, argument2, ...)
```

In this case, you type out:

* The name of the function (`functionName`), then
* An opening parenthesis (`(`), then 
* A list of arguments (data to go into the function) separated by commas, then
* A closing parenthesis (`)`).

`len` is a function built in to Python that returns the length of a string you
give it as an argument. Here's how you use it:

```python
>>> len("This is a very very long string. How long, you ask? Let's find out!")
67
```

<details>
  <summary>:speech_balloon: I hate parentheses, what if I don't use them?</summary>

  <hr>
  
  If you don't add the parentheses, you just get the function returned back to
  you.

  ```python
  >>> len
  <built-in function len>
  ```

  Not very useful, for now...

  <hr>
</details>

The return value of `len`, an _integer_, which is a data type used to represent
whole numbers (not decimals). If you wanted to convert an integer intro a
string, for some reason, you could use the `str` function, like this.

```python
>>> str(67)
'67'
```

And if you wanted to convert it back to an integer you can do this.

```python
>>> int('67')
67
```

You can also assign the return value of a function to a variable.

```python
>>> word = 'hippopotamus'
>>> word
'hippopotamus'
>>> word_length = len(word)
>>> word_length
12
>>> word_length_as_string = str(word_length)
>>> word_length_as_string
'12'
```

## Exercises

Try the following functions in your Python REPL. The goal is to build some
muscle memory for executing functions. You don't need to memorise what each one
does.

* `type`, which takes anything as an argument and returns its _data type_. Try
  it with a string and then a number.
* `print`, which takes anything as an argument and prints it to the terminal.
  Try it with a string and then an integer. It'll seem useless at the moment but
  will soon become your best friend.
* `abs`, which takes a number as an argument and always returns a positive
  value. Try it with both positive and negative numbers.

[Here is a list of Python's built-in
functions](https://docs.python.org/3/library/functions.html). Many of them rely
on concepts we've not covered yet, and some of them are so specialist that won't
cover them at all. 

Try out a few now for fun and then bookmark the list for reference.

## Reflect and Review

In this section, you learned about functions and arguments.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

* What functions are
* What arguments are
* How to use a function
* Why functions are useful
* Where to learn about Python's built-in functions


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=03_functions.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F04_methods.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F03_functions.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
