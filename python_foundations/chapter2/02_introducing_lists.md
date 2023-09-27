# Lists

A list is just that — a list of items.

In Python they are a kind of _sequence_. This is similar to strings, in that
they can have length, you can slice them, and so on.

<details>
  <summary>:speech_balloon: I've heard of arrays, are they the same?</summary>

  <hr>
  
  The short story is that people often use the terms interchangeably and
  typically you can assume that they are the same thing.
  
  The long story is that technically there is a difference. We won't go into
  this here but feel free to look it up if you are interested.

  <hr>
</details>

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

- Create lists in Python
- Add items to a list
- Retrieve a single item in a List

## Part One: Creating a List

Let's create a list of my favourite numbers.

``` python
>>> [77, 23, 46, 1337]
[77, 23, 46, 1337]
```

We could also create a list of strings.

```python
>>> ["Will", "Simo", "Alex", "Eddie", "Kay"]
['Will', 'Simo', 'Alex', 'Eddie', 'Kay']
```

Try creating a list of your favourite films in the Python REPL.

Python lists can contain any data type — strings, integers, floats, booleans, or
even lists of other lists.

## Part Two: Adding Items to a List

If you want to add things to a list, you can use the `.append()` method.

```python
>>> my_list = []
>>> my_list.append("hello")
>>> my_list
['hello']
>>> my_list.append("world")
>>> my_list
['hello', 'world']
```

## Part Three: Accessing Items in a List

You can access elements in lists based on their position. To do that, use the
`[]` method, combined with the item's index. Remember that the index of the
first item in a Python list is 0, not 1.

```python
>>> my_list = ["hello", "world"]
>>> my_list[0] # Get the first element
'hello'
>>> my_list[1] # Get the second element
'world'
```

:question: What happens if you create a list of two items called `my_list` and
then do `my_list[3]`? Try it now.

:question:  What happens if you try to do `my_list[-1]`? Try that as well!

Remember slicing strings? We can do that on lists too.

```python
>>> track_list = ["Sympathy For The Devil", "Leech", "Dragonaut", "Green Machine", "Sound & Vision"]
>>> track_list[0]
'Sympathy For The Devil'
>>> track_list[0:2]
['Sympathy For The Devil', 'Leech']
>>> track_list[1:4]
['Leech', 'Dragonaut', 'Green Machine']
```

## Part Four: List Methods

In Chapter 1, you learned about String methods. Let's learn about List methods.

Here's a practice list for you:

```python
>>> practice_list = [1, 17, 10, 1, 20, 22]
```

Try out each of the following methods on this list and try to work out what it
does. 

Note that some of these methods will modify the original `practice_list` (called
_mutating_ or modifying _in place_) and some will return a new list. See if you
can work out which is which by checking the original list after each call.

* `clear()`
* `reverse()`
* `pop()`
* `index(item)`
* `sort()`

As you now know, you can have lists of strings too. Which poses a question:

```python
>>> string_list = ["bear", "anaconda", "cat", "ZEBRAAAAA", "dog", "elephant"]
>>> string_list.sort()
>>> string_list
# ???
```

How will Python sort that?

You can find more [list
methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
in the Python Docs.

## Part Five: A List of Passwords?

Let's imagine the most basic list of passwords. If we had a notebook, we might
keep them in a table like this:

| **Password** |
| ------------ |
| password     |
| 123456       |
| qwerty       |

And then in code we could keep them like this:

```python
>>> passwords = ["password", "123456", "qwerty"]
['password', '123456', 'qwerty']
```

Very nice. Smart. But how are you going to remember what website the password is
for?

Let's add another column to our table.

| **Service** | **Password** |
| ----------- | ------------ |
| acebook     | password     |
| makersbnb   | 123456       |
| chitter     | qwerty       |

But how do we store this in a list? Here's a few ways we could try:

```python
>>> passwords = ["acebook", "password", "makersbnb", "123456", "chitter", "qwerty"]
```

That's not very satisfying. How do we tell which is which? We could say that
evens are the service and odds are the password, but we might well make
mistakes. It would be nice to have a better structure.

We could put lists inside lists:

```python
>>> passwords = [["acebook", "password"], ["makersbnb", "123456"], ["chitter", "qwerty"]]
>>> passwords[0][0]
'acebook'
>>> passwords[0][1]
'password'
```

A little better, but not great. Take a look at how much work we need to do in
order to find a password by the name of its service:

```python
# Let's say we have a service 'chitter' and we want to find its password
>>> service = 'chitter'
>>> for pair in passwords:
...     if pair[0] == service:
...         password = pair[1]
...  
>>> password
'qwerty'
```

Quite arduous. We've shown you this so that you can see how lists of lists work,
but there is a better alternative to storing this sort of multi-column data:
dictionaries. You'll read about this in the next step.

## Reflect and Review

In this section, we introduced the concept of a list and how to use it. We also
learned how to create lists, add items to lists, and access items in lists.
They're very useful but they are not the solution to every problem, just like
the hammer is not the right tool for every job.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
* What a list is
* How to create a list
* How to add items to a list
* How to access items in a list


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=02_introducing_lists.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F03_introducing_dictionaries.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F02_introducing_lists.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
