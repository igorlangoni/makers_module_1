# Advanced Dictionaries

In chapter 2, you learned how to create and manipulate dictionaries.

```python
>>> # create a dictionary and assign it to the person variable
>>> person = {'name' : 'jo', 'age' : 42, 'height' : 170}
>>> # add a new key-value pair
>>> person['pet'] = 'cat'
>>> # add a new key-value pair
>>> person['job'] = 'software engineer'
>>> person
{'name' : 'jo', 'age' : 42, 'height' : 170, 'pet' : 'cat', 'job' : 'software engineer'}
```

You also know how to get a list of all the keys or all the values using `person.keys()` and `person.values()`. Now it's time to take things a little further.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Manipulate dictionaries using functions and comprehensions

## More Comprehension

We can always rely on our trusty `for` loops to iterate through something if need be.

But as we saw in the previous section, `list comprehensions` take that trusty for loop and compact it down into a neat single line. It may come as little surprise that we can do the same thing with Dictionaries.

Let's take this example:

``` python
>>> square_dict = {}
>>> for num in range(1, 11):
...     square_dict[num] = num*num
... 
>>> print(square_dict)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

And refactor it down with a dictionary comprehension:

``` python
>>> square_dict = {num: num*num for num in range(1, 11)}
>>> print(square_dict)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>> for i in square_dict.items():
...     print(i)
... 
(1, 1)
(2, 4)
(3, 9)
(4, 16)
(5, 25)
(6, 36)
(7, 49)
(8, 64)
(9, 81)
(10, 100)
```

```python
>>> person = {'name' : 'jo', 'age' : 42, 'height' : 170}
>>> for item in person:
...     print(f"key value pair: {item} -> {person[item]}")
... 
key value pair: name -> jo
key value pair: age -> 42
key value pair: height -> 170
>>> 
```

When you iterate over a dictionary, you're iterating over all the key-value pairs and it is important to use the appropriate syntax to target the key and the value separately.

Dictionary comprehensions are a good way to create dictionaries quickly and assign values to a pre-existing set of keys. Let's look at an example:

``` python
>>> friends = ["Will", "Bernie", "Garth", "Suze"]
>>> card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
>>> import random
>>> random_dict = {friend:random.choice(card_suit) for friend in friends}
>>> random_dict
{'Will': 'Clubs', 'Bernie': 'Diamonds', 'Garth': 'Diamonds', 'Suze': 'Hearts'}
```

Or in a different way, to make sure there are no overlaps in card suit, we can use `zip()` to put the two lists together:

``` python
>>> friends = ["Will", "Bernie", "Garth", "Suze"]
>>> card_suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
>>> from random import shuffle
>>> shuffle(card_suit)
>>> card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}
>>> card_friends
{'Will': 'Hearts', 'Bernie': 'Spades', 'Garth': 'Diamonds', 'Suze': 'Clubs'}
>>> shuffle(card_suit)
>>> card_friends = {friend:card for (friend, card) in zip(friends, card_suit)}
>>> card_friends
{'Will': 'Diamonds', 'Bernie': 'Spades', 'Garth': 'Hearts', 'Suze': 'Clubs'}
```


## Dictionary Methods & Advanced Iteration

There are plenty of methods to help us manipulate our dictionaries and the data we store in them. Let's take a look at some helpful examples.

Let's say we are keeping score in a tournament, we may want to add some scores to a running score keeping object. 

``` python
>>> tourny_dict = {"Dan":2, "Wolfgang":14, "June":43, "Tany":32, "Sharon": 8}
>>> scores = [1, 3, 4, 3, 5]
>>> count = 0
>>> for x in tourny_dict:
...     tourny_dict[x] += scores[count]
...     count += 1
... 
>>> tourny_dict
{'Dan': 3, 'Wolfgang': 17, 'June': 47, 'Tanya': 35, 'Sharon': 13}
```

Instead of using standard loops we could use `dictionary comprehension`, which is very similar to a `list comprehension`, but it is hugely over complicated and not very `pythonic`:

``` python
>>> tourny_dict
{'Dan': 3, 'Wolfgang': 17, 'June': 47, 'Tany': 35, 'Sharon': 13}
>>> scores = [7, 3, 6, 2, 1]
>>>
>>> update_dict_comp = {key: value + scores[list(tourny_dict.keys()).index(key)] for (key, value) in tourny_dict.items()}
>>>
>>> tourny_dict.update(update_dict_comp)
>>> tourny_dict
{'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14}
```

It is often far easier, more readable and preferable to use standard `for` loops, and then call the `.update()` method on the dictionary. Let's imagine we want to add in a new player to the tournament:

``` python
>>> tourny_dict
{'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14}
>>> new_player = {"Will":0}
>>> tourny_dict.update(new_player)
>>> tourny_dict
{'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}
>>> 
```

If we need to eliminate players from our tournament based on certain conditions, we could do this with a regular `for` loop, or we could use the more advanced `filter()` function. Which do you think is more appropriate in most settings:

``` python
>>> tourny_dict
{'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}
>>> next_round = {}
>>> for player, score in tourny_dict.items():
...     if score > 20:
...             next_round[player] = score
... 
>>> next_round
{'June': 53, 'Tany': 37}
>>> 
>>> # And now using filter()
>>> next_round = {}
>>> next_round = dict(filter(lambda player: player[1] > 20, tourny_dict.items()))
>>> next_round
{'June': 53, 'Tany': 37}
>>> 
```


We could even use a Dictionary Comprehension here:

``` python
>>> tourny_dict = {'Dan': 10, 'Wolfgang': 20, 'June': 53, 'Tany': 37, 'Sharon': 14, 'Will': 0}
>>>
>>> next_round = { key:value for (key, value) in tourny_dict.items() if value > 20 }
>>> next_round
{'June': 53, 'Tany': 37}
>>> 
```
## Reflect and Review

In this section, we dug a bit deeper into Dictionaries.

**Please pause at this point to reflect and review your learning...**

Write some short notes, or talk to a peer, about:

* What dictionaries are
* How dictionaries can be manipulated
* How this differs from list manipulation
* What is more "pythonic", advanced methods or simple loops?


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=06_advanced_dictionaries.md&repository=makersacademy%2Fpython_foundations&redirect=chapter3%2F07_putting_chapter_3_into_practice.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F06_advanced_dictionaries.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F06_advanced_dictionaries.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F06_advanced_dictionaries.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F06_advanced_dictionaries.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter3%2F06_advanced_dictionaries.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
