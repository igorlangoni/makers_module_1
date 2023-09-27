# Choosing a Data Structure: Part Two

In the previous section you considered what it would be like to use each of
these data structures. In this section, we'll help you make a decision.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Compare and contrast two different data structures

## A Reminder of the Options

```python
# Option 1: Add another key value pair for each service
{
  'acebook_password' : 'password123',
  'acebook_added' : '22/03/22',
  'makersbnb_password' : 'qwerty789',
  'makersbnb_added' : '22/03/22'
}

# Option 2: Convert to a nested dictionary
{
  'acebook' : {
    'password' : 'password123',
    'added_on' : '22/03/22',
  },
  'makersbnb' : {
    'password' : 'qwerty789',
    'added_on' : '22/03/22',
  }
}

# Option 3: Convert to a list of dictionaries
[
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]
```

You might now have a strong preference for one of them. Let's consider them all
once more, together. Maybe you'll change your mind... or maybe you won't.

## Using Option 1

To get all the details about Acebook, we'd need to do two things.

```python
>>> passwords = {
>>>  'acebook_password' : 'password123',
>>>  'acebook_added' : '22/03/22',
>>>  'makersbnb_password' : 'qwerty789',
>>>  'makersbnb_added' : '22/03/22'
>>> }
>>> # first we get the password
>>> passwords['acebook_password']
'password123'
>>> # then we get the date on which it was added
>>> passwords['acebook_added']
'22/03/22'
```

We might also consider what it's like, for us humans, to read the data.

## Using Option 2

To get all the details about Acebook, we need to do one thing.

```python
>>> passwords = {
...   'acebook' : {
...     'password' : 'password123',
...     'added_on' : '22/03/22',
...   },
...   'makersbnb' : {
...     'password' : 'qwerty789',
...     'added_on' : '22/03/22',
...   }
...  }
> passwords['acebook']
: {'password' : 'password123', 'added_on' : '22/03/22'}
```

And how is it to read the above? Does its hierarchical nature make it easier, or
harder, to parse?

## Using Option 3

To get all the details about Acebook, we'd need to search for the corresponding
dictionary. We'll dig into how this works later, in Lists Part II.

```python
>>> passwords = [  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'} ]
>>> def find(service):
...     for pwd in passwords:
...             if pwd['service'] == service:
...                     return pwd
... 
>>> find("acebook")
{'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}
```

## Making a Decision

Ultimately, it's your choice. Personally, I think it comes down to a choice
between option 2 or option 3. Both of those options do a better job than option
1 when it comes to communicating which pieces of data belong together and they
both allow you to retrieve all the information for a service in one step. This
might not seem like a big deal right now, but imagine how messy things could
get, with option 1, if you were to add more properties for each service.

If you're interested, you could try to find out whether finding values in a
dictionary (option 2) is more or less computationally efficient than finding
elements in an array (option 3).

## Reflect and Review

In this section, we compared three different data structures for their
readability and ease of use.

**Please pause at this point to reflect and review your learning...**

Write a few short notes, or chat with a peer, about...
* The structure of a nested dictionary
* The structure of a list of dictionaries
* The readability of each option
* The ease of use for each option
* Which option you've chosen and why


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=03_choosing_a_data_structure_ii.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F04_functions_as_arguments.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F03_choosing_a_data_structure_ii.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F03_choosing_a_data_structure_ii.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F03_choosing_a_data_structure_ii.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F03_choosing_a_data_structure_ii.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F03_choosing_a_data_structure_ii.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
