# Choosing a Data Structure: Part One

To track the date on which a service was added to Password Manager, we'll need
to modify the data-structure that stores them.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Create a nested dictionary
* Create a list of dictionaries

## Some Options

As always, there are many options we could consider - here are a few of those
options, along with the current data structure.

```python
# The current data structure
{
  'acebook' : 'password123',
  'makersbnb' : 'qwerty789'
}

# Option 1: Add another key value pair for each service
{
  'acebook_password' : 'password123',
  'acebook_added' : '22/03/22',
  'makersbnb_password' : 'qwerty789',
  'makersbnb_added' : '22/03/22'
}

# Option 2: A nested dictionary
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

# Option 3: A list of dictionaries
[
  {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
  {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]
```

So, how do we decide which one to use? Consider what it would be like to
manipulate each one and we'll then think about this together in the next
section.

Try to describe, in plain English, the task of finding all the info about
Acebook, if we chose...
  - Option 1
  - Option 2
  - Option 3

## Reflect and Review

In this section, we considered three different data structures, some of which
may have been new to you.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain, in writing or to a peer:
* The structure of a nested Dictionary
* The structure of a List of Dictionaries



[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=02_choosing_a_data_structure_i.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F03_choosing_a_data_structure_ii.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F02_choosing_a_data_structure_i.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F02_choosing_a_data_structure_i.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F02_choosing_a_data_structure_i.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F02_choosing_a_data_structure_i.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F02_choosing_a_data_structure_i.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
