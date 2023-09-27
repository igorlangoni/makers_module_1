# Methods

In the previous section, you learned that Python comes with a range of useful
built-in functions. In this section, you'll learn about methods.

Methods are functions that are closely tied to a particular piece of data.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Explain what a method is
* Explain the difference between a method and a function
* Use methods to operate on pieces of data
* Find more information about Python methods

## Part One: What is a Method?

Methods are like functions, except that they are closely tied to a particular
piece of data. Let's look at an example:

```python
>>> word = "Hello"
>>> word.upper()
'HELLO'
```

In this case we are calling the `upper` method on the string `"Hello"`. This
returns `"HELLO"`.

Note the dot `.` between `word` and `upper`, and the parentheses on the end.
These are required elements of the syntax for calling a method.

Here's another example using `lower` on the string `"PYTHON"`.

```python
>>> word = "PYTHON"
>>> word.lower()
'python'
```

As you can see, the original string is not changed by `lower`:

```python
>>> word = "PYTHON"
>>> word.lower()
'python'
>>> word
"PYTHON"
```

### Now Try This

* Does `upper` change the original string or does it work like `lower`?

* What happens when you call `upper()` without its parenthesis?
``` python
>>> 'welcome to python'.upper
>>> # ???
```

## Part Two: String Methods

In Python there are a lot of string methods but, don't worry, you won't have to
learn all of them! In fact, you're only likely to remember a handful and, for
the rest, you'll use the Python docs (which you'll see very soon).

### Time to Play in the Python REPL

Open up the Python REPL and try out each of the methods listed below.

Note that one of them is an impostor — we've made it up! You'll get an
error message, so be ready to work out what it's telling you. One of the others
might appear to do nothing at first — try looking it up on a search engine to
see what it does.

* `capitalize`
* `lower`
* `isascii`
* `invert`
* `isalpha`
* `title`
* `strip` 

For example:

```python
>>> "hello world".capitalize()
'Hello world'
```

As you try out each one, take a guess at what it does.

## Part Three: Method Chaining

If you wanted to use both `strip` and `upper` to transform `"  hello "` into
`"HELLO"`, you could do this in two steps, using a variable (called
`stripped_greeting`) to hold the intermediate result.

```python
>>> greeting = "  hello "
>>> stripped_greeting = greeting.strip()
>>> stripped_greeting.upper()
'HELLO'
```

You can also do this in one line, using method chaining.

```python
>>> greeting = "  hello "
>>> greeting.strip().upper()
'HELLO'
```

This works, because `strip` returns a string `"hello"`, which we then call
`upper` on to get the final return value of `"HELLO"`.

You can think of this a bit like brackets in mathematics: `(2 + 3) * 6`. First
you add `2 + 3` to get `5`, then you multiply that `5` by `6` to get `30`. 

For Python, first it runs `greeting.strip()` to get `"hello"`, then runs
`.upper()` to get `"HELLO"`.

### Exercise

Here are some lines of code. Note down what you think each one will do. When you
have noted down all of the answers, run them in the Python REPL to find out.

```python
# Don't run these until you've said what you think will happen

# Example 1
>>> len("hello")

# Example 2
>>> 5.lower()

# Example 3
>>> "heLLo ".lower().strip()

# Example 4
>>> len("hello").upper()

# Example 5 - pay attention!
>>> str(len(" hello ")).strip()
```

<details>
  <summary>:speech_balloon: I don't understand why Python works that way (Click here for an explanation)</summary>

  <hr>
  
  **Example 1:** `len("hello")` returns `5` — an integer representing the number of characters in `"hello"`.

  **Example 2:** `5.lower()` throws an error because `lower` is a string method and cannot be used on an integer.
  
  **Example 3:** `"heLLo ".lower().strip()` returns `"hello"` because `"heLLo ".lower()` returns the String `"hello "` on which we then call `strip` to remove spaces at the start and end.

  **Example 4:** `len("hello").upper()` throws an error because `len("hello")` returns `5` on which we then call `upper`, a method that can only be called on strings.</div>
  
  **Example 5:** `str(len(" hello ")).strip()` returns `"7"` because we call the function `len` on `" hello "` making `7`. We then convert this to a string using `str` and finally call `strip` on that string (which doesn't change the string `"7"` because it has no spaces on the beginning or end).

  <hr>
</details>

## Part Five: the Python Docs

The Python docs catalogue all the methods which are contained within the Python
standard library. So, for example, you can find [all the `String`-specific
methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).

Python strings actually belong to a family of data types called `sequences`.
This means that for some string features you'll need to look at the [sequence
docs](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

In each case, there's an explanation of what the method does and, if you're
lucky, a clear example of the method in action –
[`strip`](https://docs.python.org/3/library/stdtypes.html#str.strip) is a good
example of that.

In section one you found a list of some other Python data types. Find the
Python docs page for one of those now.

## Reflect and Review

In this section, you learned about string methods and method chaining.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

* What methods are
* How to use `String` methods
* How method chaining works
* Where to learn about Python's string methods


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=04_methods.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F05_further_string_manipulation.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F04_methods.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
