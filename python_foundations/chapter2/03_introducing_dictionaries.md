# Dictionaries

Dictionaries, like lists, store a collection of items.

However, they also allow you to associate a label with each item.

Let's look at this list:

```python
>>> my_friend = ["Pippa", 25, "orange"]
```

You probably think yeah, that's Pippa, she's 25 years old and her favourite
colour is orange.

But let's take a look at this in dictionary form...

```python
>>> my_friend = {
        "name": "Pippa",
        "horses": 25,
        "deadly_weapon": "orange" 
    }
```

Actually my friend Pippa has twenty-five horses at her command and if you see
her coming for you with an orange you had better run! And you'd better go fast
because she's riding multiple horses! Sprint!

Labels are important in programming, otherwise we or our colleagues may make
mistakes. Hence: dictionaries.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Explain what a dictionary is
* Create dictionaries
* Add key-value pairs to a dictionary
* Read values stored in a dictionary
* Use some methods on dictionaries

## Part One: Creating a Dictionary

Dictionaries are made up of key-value pairs. The _key_ is the label and the
_value_ is the piece of data that you wish to store.

They look like this:

``` python
>>> person = {
...   "name": "Guido van Rossum",
...   "nationality": "Dutch",
...   "favorite_programming_language": "Python"
... }
>>> person
{'name': 'Guido van Rossum', 'nationality': 'Dutch', 'favorite_programming_language': 'Python'}
```

**Note that for lists we use square brackets, but for dictionaries we use curly
braces.**

Open a Python REPL and create a few dictionaries of your own:

* A dictionary containing your name, age, and nationality (or one of them).
* A dictionary containing the capital city of the first five countries you can
  think of.

<details>
  <summary>:speech_balloon: Isn't it a bit inconsiderate of you to ask us to pick one nationality?</summary>

  <hr>
  
  That's fair. Try this:

``` python
  >>> person = {
  ...   "name": "Jim Carrey",
  ...   "nationality": ["Canadian", "American"],
  ...   "favorite_programming_language": "Java"
  ... }
  >>> person
  {'name': 'Jim Carrey', 'nationality': ['Canadian', 'American'], 'favorite_programming_language': 'Java'}
  ```

  <hr>
</details>

After you've created a few dictionaries, try using something other than a
string for the keys. What works? What doesn't work?

## Part Two: Reading Individual Values

Once you have a dictionary, you can read an individual _value_ using its _key_.

``` python
# First, create and assign the person dictionary as above. Then:
>>> person['name']
'Guido van Rossum'
>>> person['nationality']
'Dutch'
```

Do this a few times to get some practice.

## Part Three: Adding Key-Value Pairs

If you already have a dictionary and wish to add new key-value pairs, you can do
so using the `[]` syntax.

``` python
# First, create and assign the person dictionary as above. Then:
>>> person["birthday"] = "31 January"
>>> person["favourite_colour"] = "Purple"
>>> person
{'name': 'Guido van Rossum', 'nationality': 'Dutch', 'favorite_programming_language': 'Python', 'birthday': '31 January', 'favourite_colour': 'Purple'}
```

Now you do the same! Create a new dictionary and add some key-value pairs as
shown above. Better still, do that a few times so that you start to build some
familiarity with the `[]` syntax.

## Part Four: More Dictionary Methods

Let's learn some dictionary methods.

Here's a practice dictionary for you:

```python
>>> practice_dict = { "London": "England", "Edinburgh": "Scotland", "Cardiff": "Wales", "Belfast": "Northern Ireland" }
```

Try out each of the following methods on this list and try to work out what it
does.

* `keys()`
* `values()`
* `get(key)`
* `items()`
* `pop(key)`
* `clear()`
* `setdefault(key, default)`

You can find more [dictionary
methods](https://docs.python.org/3/library/stdtypes.html#typesmapping)
in the Python Docs.

## Reflect and Review

In this section, you learned about how to create and manipulate  Dictionaries.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain, in writing or to a peer:
* What a Dictionary is
* How to create a Dictionary
* How to add key-value pairs to a Dictionary
* How to retrieve a value from a Dictionary
* How to retrieve all the keys from a Dictionary


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=03_introducing_dictionaries.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F04_introducing_classes.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F03_introducing_dictionaries.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
