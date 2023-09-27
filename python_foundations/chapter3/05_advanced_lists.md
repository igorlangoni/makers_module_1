# Advanced Lists

In chapter 2, you learned how to define and add elements to Python lists.

```python
>>> numbers = [1, 2, 3] # create a list and assign it to a variable
>>> numbers.append(4) # append a new item, the number 4, to the list
>>> numbers
[1, 2, 3, 4]
>>>
```

And in the previous section of this chapter, you wrote a `find_acebook` method
to help filter out specific passwords out of the full list of passwords.

```python
>>> passwords = [
...     {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
...     {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
... ]
>>> def find_acebook(passwords):
...     for password in passwords:
...         if password['service'] == 'acebook':
...             return password
...
>>> find_acebook(passwords)
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}
>>>
```

<!-- OMITTED -->


You might have thought this a bit verbose or clunky but there is one advantage
to it: because `for` loops and `if` statements exist in most of the programming
language you are likely to encounter in the field, you will easily be able to
translate this approach to a different language.

That's a significant advantage, because you'll very likely be required to
program in languages other than Python in your career.

That said, there are other, more concise ways to find a specific element in a
list in Python that are useful to know about because you're very likely to come
across them in Python code out there in the wild.

So let's call this first way of filtering a list using `for` loop **Version 1**.
In the following sections, we're going to be looking at 3 more ways of doing the
same thing in Python.

<!-- OMITTED -->

## Learning Objectives

In this section, you'll learn to:

- Search for elements in a list using `filter`
- Search for elements in a list using list comprehensions
- Transform elements in a list using `map`

## Version 2: Using `filter`

Python has a built-in function called `filter()`. The `filter` function can be
applied to a list to find specific elements that satisfy a condition of our
choosing.

Using filter, we can rewrite our solution above like this:

```python
>>> passwords = [
...   {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
...   {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
... ]
>>> def is_acebook(password):
...   return password['service'] == 'acebook'
>>> next(filter(is_acebook, passwords))
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}
>>>
```

As you can see, this version is already quite a bit shorter than Version 1 but
it also introduces a few new Python language features.

Let's look at it in more detail:

```python
# Picking an element out of a list -- Version 2

# This function represents the condition we want to filter by.
# It takes a dictionary representing a password and returns True if the
# the value for the 'service' key is 'acebook' and False otherwise.
def is_acebook(password):
  # This is the same condition we used in Version 1, but this time without
  # the for loop around it.
  return password['service'] == 'acebook'


# `filter` actually returns a something called an iterable,
# which acts very similarly to a list.
# To grab the first element of an iterable, we use `next()`.
next(
  # The filter function takes two arguments, a function and a list.
  # It applies the function to each element in the list to check whether they
  # should be included in the output of `filter`.
  filter(
    is_acebook,  # This is the function we want to filter based on.
                 # It takes a dictionary representing a password and returns
                 # True if the password is for the acebook service and False
                 # otherwise. 
    passwords   # This is the list we want to filter.
  )
)
```
<!-- OMITTED -->

Why were we able to simplify our `find_acebook` function down to this new
`is_acebook` in this way, completely getting rid of the `for` loop? Well,
`filter` iterates over (looks at every) element in the lists and passes each one
into our `is_acebook` function. We no longer need to write the `for` loop
ourselves!

Using a function like `filter` to search for a specific element in a list is a
bit more specific to Python but remains reasonably portable to other languages
as well, though a little less so than Version 1.


### Version 2.1: Using `filter` with a `lambda`

The next way of picking out an element from a list is a variation on Version 2,
which is why we've called it Version 2.1 here. In this version, we make our code
even more concise by introducing another new Python feature: lambda functions.

A Lambda is a small function with no name. We use the keyword `lambda` to define
one. In this version of the solution, we'll use a lambda to replace the
`is_acebook` function we used in Version 2.

```python
>>> passwords = [
...   {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
...   {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
... ]
>>> next(filter(lambda password: password['service'] == 'acebook', passwords))
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}
>>>
```

Let's look at the lambda in more detail:

```python
# The `lambda` keyword tells Python that we're defining a small function with no name.
lambda 
  password: # Lambda functions take a single argument
            # We've chosen to call it `password`.
    password['service'] == 'acebook' # This is the body of the lambda. 
                                      # Note that there is no `return` keyword.
                                      # A lambda function will automatically
                                      # return the value of the expression
                                      # in its body.
                                      # In this case, it will return True if the
                                      # value for the key `service` in the 
                                      # passed in dictionary is 'acebook' and
                                      # False otherwise.
```

> **Note**: You will not be able to copy, paste and run the code below as is
> because Python doesn't allow lambdas to be broken up into separate lines in
> this way, but it helps for explaining them!

In terms of its "translateability", this way of searching through a list is
about the same as Version 2: while they might not call them lambdas, many common
programming languages have ways of creating functions without a name (often
referred to as anonymous functions).

## Version 3: using list comprehensions

This next approach to searching through a list is the most "pythonic" of them
all: using list comprehensions.

```python
>>> passwords = [
...   {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
...   {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
... ]
>>> [password for password in passwords if password['service'] == 'acebook']
[{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}]
>>>
```

Note that in this example, the result of the search operation is a list of
dictionaries, not a single dictionary.

<!-- OMITTED -->

Let's take this apart:

```python
passwords = [
  {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
  {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

[                                     # Create a list containing:
  password                              # the value of the `password` variable
  for password                          # For every item, which we'll call
                                        # `password`
  in passwords                          # In the list of dictionaries
                                        # called `passwords`
  if password['service'] == 'acebook'   # if and only if the dictionary contains 
                                        #'acebook' for the key 'service'
]
```

List comprehensions are very concise tool for operating on lists in Python.
However, depending on what you've previously been exposed to, they can take some
getting used to in terms readability.

Most other common programming languages don't provide anything similar to list
comprehensions, but they are very widely used in Python, so it's important you
can recognise them when you encounter them.


## Practice

Let's see how we can adapt these four different approaches to perform other
useful operations on our list of passwords:

- Check whether all passwords are at least 8 characters long
- Check whether any password(s) were added on 21/03/22 
- Return a list of all passwords added on 22/03/22

<!-- OMITTED -->

We'll do the first example together and apply it to the following list of
passwords:

```python
>>> passwords = [
...   {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
...   {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
...   {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
... ]
>>>
```

Let's write a function called `are_all_passwords_long_enough` that returns
`True` if all passwords in the passed in list are at least 8 characters long and
`False` otherwise. 

We can do it with a `for` loop (version 1):

```python
>>> def are_all_passwords_long_enough(passwords):
...   for password in passwords:
...     if len(password['password']) < 8:
...       return False
...   return True
>>> are_all_passwords_long_enough(passwords)
False
>>>
```

We can do it using `filter` (version 2) by searching for all the passwords that
are too short and checking that the resulting list is empty:

```python
>>> def is_too_short(password):
...   return len(password['password']) < 8
...
>>> def are_all_passwords_long_enough(passwords):
...   return len(
...     list(
...       filter(
...         is_too_short,
...         passwords
...       )
...     )
...   ) == 0
...
>>> are_all_passwords_long_enough(passwords)
False
>>>
```

We can get rid of the `is_too_short` function by using `filter` with a lambda
(version 2.1):

```python
>>> def are_all_passwords_long_enough(passwords):
...   return list(
...     filter(
...       lambda password: len(password['password']) < 8,
...       passwords
...     )
...   ) == []
...
>>> are_all_passwords_long_enough(passwords)
False
>>>
```
Or we could do it with a list comprehension (version 3):

```python
>>> def are_all_passwords_long_enough(passwords):
...   return len(
...     [ 
...       password
...       for password
...       in passwords
...       if len(password['password']) < 8
...     ]
...   ) == 0
...
>>> are_all_passwords_long_enough(passwords)
False
>>>
```

### Your turn

Now it's your turn. Using at least one of the four approaches to working with
lists you've seen so far:

- Write a function that checks whether any passwords were added on 21/03/22 
- Write a function that returns a list of all passwords added on 22/03/22

At this point in your learning journey, the important thing is to be comfortable
using Version 1, the `for` loop approach, because it's going to be the most
transferable to other programming languages.

If you find it interesting to play with the other versions a bit as well, go for
it. If not, don't worry :)

### One more useful list operation

So far we've mainly seen different ways of searching for elements in a list
given different conditions.

But there is one more common operation that programmers often find themselves
needing to perform on lists. Python has a built-in method for it called `map`.

Like `filter`, it takes a function (which may be a lambda) and list as arguments
and returns a new list[^1]. And just like was the case for `filter`, equivalent
methods to `map` exist in many other programming languages and they work in very
similar ways.

But, crucially, `map` returns a different result.

[^1]: As noted earlier, `filter` actually returns an iterable, which is very
    similar to a list. The same is the case for `map`.

Try using `map` now by running the following example:

```python
>>> result = map(lambda number: number * 2, [1, 2, 3, 4])
>>> list(result)
```

What do you think `map` does? How is its result different from the `filter`
function you already know?

<details>
<summary>Click here to check your answer</summary>
<p>

`map` is similar to `filter` in that it takes as input a function and a list and
then iterates through a list, passing every element into the given function and
finally returns a new list[^1].

The difference is that the result of `map` is a new list of the same length as
the original, containing the result of applying the given function to every
element in the original list. In this case, this means that it applies the
operation `number * 2` to every number in the original list. This process of
applying the same function to every item in a list is often referred to as
"mapping" over a list.

In contrast, `filter` needs to be passed a function that returns `True` or
`False`, and will only place those items in the returned list for which the
function returns `True`.
</p>
</details>

### Another way 

As you might have started to notice, Python likes to have more than one way of
doing the same thing. Instead of using `map`, we can also use list
comprehensions to apply a function to all elements of a list.

Here's an example to try out:

```python
>>> [number * 2 for number in [1, 2, 3, 4]]
```

Can you explain to yourself how it achieves the same result as the `map` example
above?

### One more task

Now, to finish off, try to write a piece of code that achieves the same result
as the two examples above, but using only a `for`loop!

<!-- OMITTED -->

<details>
<summary>Click here to compare your code to a sample solution</summary>
<p>

Here's one possible solution:

```python
>>> numbers = [1, 2, 3, 4]
>>> doubled_numbers = []
>>> for number in numbers:
...   doubled_numbers.append(number * 2)
>>> doubled_numbers
[2, 4, 6, 8]
>>>
```
</p>
</details>

## Making a Decision

Ultimately, it's your choice which of the different approaches presented you
choose to use going forward.

While using `filter`, `map`, lambdas and list comprehensions may allow writing
more concise and perhaps neater looking code, knowledge of these approaches also
get increasingly specific to Python and thus less of transferable to other
languages. 

So if you find that you feel most comfortable sticking to `for` loops and `if`
statements for now, don't worry. That's okay. The important thing is that you're
able to recognise and make sense of the other approaches when you encounter
them.


## Reflect and Review

In this section, we dug a bit deeper into lists.

**Please pause at this point to reflect and review your learning...**

This time, you're also going to reflect on some things from previous chapters
...

Make some notes, or talk to a peer, about:
- How to use `for` loops and if statements to search through a list
- How to use `for` loops to create a new list from an existing list
- How `filter` and `map` can be an alternative to using `for` loops
- The difference between printing to the terminal and returning something
- What scope is


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=05_advanced_lists.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F06_advanced_dictionaries.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F05_advanced_lists.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F05_advanced_lists.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F05_advanced_lists.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F05_advanced_lists.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F05_advanced_lists.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
