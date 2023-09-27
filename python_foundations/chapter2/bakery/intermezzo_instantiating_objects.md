# Intermezzo: Instantiating Objects from Classes

## Introduction

We have had a look at Classes, how to define them, what they're used for and how we can put them to use. 

In this intermezzo section, we are going to look a little deeper at classes, objects, and how to use them all with a bit more confidence. 

## Repeatable Execution

Why do we use classes in Software Development? Why do we use methods? Functions? If you've got to this stage in Python Foundations, you've undoubtedly had a go at making your own in the drills - but what is the point?

The entire idea of learning increasingly complex object creation, from variables to functions, to hashes, to classes; is to make our lives easier. 

And storing executable code, or information, or instructions, in these code blocks, does make our lives a lot easier because it allows us to write something once, and then repeat it as many times s we wish.

For the variable, we need only invoke it's name:

``` python
variable_one = 10

variable_one += 15

variable_one *= 4
variable_one /= 50

print(variable_one)
```

For the function we need only make the function call:

``` python
def greeting(name):
    print(f"Hello there, {name}!")

greeting("Will")

greeting("Arthur")

greeting("Maggie")
```

For the class, we should instantiate it:

``` python
class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} sized slice. \n There is {self.size} percent cake remaining.")

gateau = Cake()
gateau.set_flavour = "Double Chocolate"
gateau.take_slice(40)

```

Notice the difference between regular function calls `some_function(argument)` and instance method calls `new_obj.method_name(argument)`?

## Exercise 1

Set a timer for 10 minutes.

Your challenge is to copy the following code out into a new Python file or use
the one from [here](./lib/bakery.py), load the file into a Python REPL with
`python3` to enter the REPL, and then `from bakery import *` on your first line
in the REPL.

Then build out your bakery with instantiation, and taste as many cakes as you can!

Don't fill up on too much of one cake, or your bakery isn't going to make it!

```python
class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} percent sized slice. \n There is {self.size} percent cake remaining.")

class Baker():
    def __init__(self):
        self.stomach_space_remaining = 100
        # You can only eat up to 100 sections of cake in one sitting.
        self.cakes_sampled = []
        # You must sample at least 5 cakes in order to ensure quality!
    
    def eat_cake(self, cake, slice):
        cake.take_slice(slice)
        if cake in self.cakes_sampled:
            print("You've tried this one already!")
        else:
            self.cakes_sampled.append(cake)
            self.stomach_space_remaining -= slice


    def check_space(self):
        print(f"You have eaten {len(self.cakes_sampled)} cakes. \n You have {self.stomach_space_remaining} percent space remaining in your belly!")
        if len(self.cakes_sampled) > 4:
            print("You have sampled more than enough cake. Time to open the shop!")
            exit()
        elif self.stomach_space_remaining < 0:
            print("You have filled up on too much cake. You pass out. The shop makes no business this day.")
            exit()
        
        return self.stomach_space_remaining

    def cakes(self):
        for cake in self.cakes_sampled:
            print(str(self.cakes_sampled.index(cake)+1) + ": " + cake.flavour)


    def choose_favourite(self):
        print("Which was your favourite cake?")
        self.cakes()
        print("Pick the number as it appears in the list.")
        choice = int(input("Which cake?: \n")) - 1
        return f"{self.cakes_sampled[choice].flavour} was your favourite!"
```

### REPL Experimentation

It is a good idea to experiment with these object in a REPL. Run `python3` and use `from bakery import *` to load these classes into the REPL.

This is how it might go:

``` python
    # Intended input/output in the Python REPL:
    
    >>> cake = Cake()
    >>> cake
    <bakery.Cake object at 0x100f7d840>
    >>> cake = Cake()
    >>> cake
    <bakery.Cake object at 0x100f7d840>
    >>> cake.flavour
    ''
    >>> cake.set_flavour("Vanilla")
    >>> cake.flavour
    'Vanilla'
    >>> will = Baker()
    >>> will
    <bakery.Baker object at 0x100f7d750>
    >>> will.eat_cake(cake, 20)
    You have taken a 20 percent sized slice.
    There is 80 percent cake remaining.
    >>> will.check_space()
    You have eaten 1 cakes.
    You have 80 percent space remaining in your belly!
    80
    >>> cake2 = Cake()
    >>> cake2.set_flavour("Strawberry")
    >>> will.eat_cake(cake2, 40)
    You have taken a 40 percent sized slice.
    There is 60 percent cake remaining.
    >>> will.check_space()
    You have eaten 2 cakes. 
    You have 40 percent space remaining in your belly!
    40
```

## Exercise 2

The next exercise requires you to either copy, or clone the bakery_2.py file.

You must load the 'bakery_2.py' file into the REPL, and do your best to satisfy the orders being placed at your Cake Bakery!

You can find a link to it [here](./lib/bakery_2.py).


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2Fbakery%2Fintermezzo_instantiating_objects.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2Fbakery%2Fintermezzo_instantiating_objects.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2Fbakery%2Fintermezzo_instantiating_objects.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2Fbakery%2Fintermezzo_instantiating_objects.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2Fbakery%2Fintermezzo_instantiating_objects.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
