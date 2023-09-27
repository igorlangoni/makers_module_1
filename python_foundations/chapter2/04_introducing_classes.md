# Classes

Classes are used to _encapsulate_, or contain, state (variables) and behaviour
(methods). Used well, they can help you to organise your code in a way that
makes it easier to understand and maintain. They do, however, take a little bit
of getting used to. This section is intended to be a gentle introduction to
classes and how they work.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Explain what classes and instances are
* Create a class with methods and variables
* Create instances of a class

## Part One: Defining a Class

Defining a class in Python is pretty straightforward — you need one new keyword,
`class`. Let's see how that works.

```Python
class Greeter():
    pass
```

That's it! Now we have a class called `Greeter`, though it's not very useful.
Let's add some methods.

```Python
class Greeter():
    def hello(self):
        return "Hello!"

    def good_bye(self):
        return "Good bye!"

```

Notice that argument there in the methods - `self`, this is a parameter that is
used as a reference to the current instance of a class. It doesn't have to be
called `self`, it just has to be the first argument of any of your class
methods, but it's common practice to use `self` as it is referring back to the
class (and this is what your will most likely see online in your research too.)

It, `self`, allows us to refer to the variables, or state, within the class when
it is instantiated - but more on that in just a moment. For now, try to define a
class method without it, and when you come to call the method from an
instantiation you might get an error - try it:

``` python
>>> class Greeter():
>>>     def hello():
>>>         return "Hello"
>>> greeter = Greeter()
>>> greeter.hello()
>>> # ???
```



## Part Two: Instantiating a Class

Great, but what can you do with this? How do you actually execute those methods?
First, you need to create an instance of a class. What _is_ an instance?

If the class itself is like a blueprint, an _instance_ of a class is the actual
thing that gets built, based on that blueprint. For a real world analogy think
of the blueprint for a house and the many houses which could get built, based on
that single blueprint. The actual houses are analogous to instances.

Let's create an instance of the class `Greeter` and then execute the `hello()`
and `good_bye()` methods.

``` Python
>>> greeter = Greeter()
```

We can return an instance of the class simply by declaring a variable to the
class name with parenthesis, which is what we do here on the first line; create
an instance of `Greeter()` assigned to the `greeter` variable. 

``` python
>>> greeter = Greeter()
>>> print(greeter)
<__main__.Greeter object at 0x102b19750>
```

We can also see the value of the object we have just created by passing it into
a `print()` function, the long number is a reference to where the instance we
just created is stored in our memory. In your case, the value after `#<Greeter:`
will be different, but that's fine :) Do it all again and you'll see another
value. This is because every time you make an instance of a class it creates a
new, and entirely separate object from that class; just like a cookie and a
cookie-cutter!

``` python 
>>> greeter.hello()
'Hello!'
>>> greeter.good_bye()
'Good bye!'
```

Next, we call `hello()` and `good_bye()` are called on the instance, which
return the Strings `"Hello!"` and `"Good bye!"`, respectively.

You'll need to put this new stuff into practice, if you want it to stick. So do
that now by building the following classes.

The next two parts rely on one another to make sense, so they won't really make
complete sense until you've read them both. Hang in there!

## Part Three: the `__init__()` Method (The Constructor)

If you want something to happen automatically, when a new instance of a class is
created, you can put that code inside a special method called `__init__()`. Give
it a try!

``` Python
>>> class Greeter():
...     def __init__(self):
...         print("Hello!")
... 
>>> new = Greeter()
Hello!
```

Above, we see that `print("Hello!")` is executed when you create an instance of
`Greeter` using `new = Greeter()` – we didn't need to call `__init__()`
ourselves, for that to happen as it was called automatically.

Now define some of your own classes and play with the `__init__()` method.

Generally, you'll want to do something more useful that execute `print()` in
your `__init__()` method. Read on to find out what that might be.

## Part Four: Instance Variables

To really leverage the benefit of classes, we need the ability to give instances
of a class unique properties. Imagine, for example, that we wanted to replace
the `person` dictionary from section 3 with a `Person()` class. Instances of the
`Person()` class would each need their own name, birthday and favourite
programming language. We achieve this using instance variables, which are
variables that are unique to each instance of a class.

They are declared by using the `self` parameter before the instance variable
name. Here's an example. Note that the instance variables are declared inside of
the `__init__()` method, because that means they will be assigned automatically
when the instance is created.

```Python
>>> class Person():
>>>     def __init__(self):
>>>         self.name = "Alan Turing"
>>>         self.birthday = "June 23, 1912"
>>>         self.favourite_language = "C"
```

But wait! As things stand, every instance of the Person class will have the same
name, birthday and favourite language. How can we make sure that each instance
has its own name, birthday and favourite language?

To achieve that, we need the ability to pass arguments into the `__init__()`
method, but if it's getting called automatically, how do we do that? Here's an
example.


```Python
>>> class Person():
...     def __init__(self, name, birthday, favourite_language):
...         self.name = name
...         self.birthday = birthday
...         self.favourite_language = favourite_language
...
>>> person1 = Person("Alan Turing", "June 23, 1912", "Standard Description")
```

All the arguments which we provide when assigned to a variable will be passed
into the `__init__()` method, automatically! Now we can create lots of people,
each with their own name, birthday and favourite language.

```Python
>>> person1 = Person("Alan Turing", "June 23", "Standard Description")
>>> person2 = Person("Ada Lovelace", "December 10", "n/a")
>>> person3 = Person("Grace Hopper", "December 9", "COBOL")
>>> person4 = Person("John von Neumann", "December 28", "C")
>>> person5 = Person("Claude Shannon", "April 30", "C")
```

This is why the `__init__()` method is often called the constructor method, as
it is the method responsible for constructing the relevant state of the instance
from the class.

Here's a challenge for you – how might you go about retrieving some of the
information, such as a `name` from your `Person()` class. The solution is below.

<details>
  <summary>Solution</summary>

  ```python
  >>> class Person():
  ...     def __init__(self, name, birthday, favourite_language):
  ...         self.name = name
  ...         self.birthday = birthday
  ...         self.favourite_language = favourite_language
  ...
  >>> person.name
  'Alan Turing'
  >>> person.birthday
  'June 23, 1912'
  >>> person.favourite_language
  'Standard Description'
  ```

</details>

Now try creating your own classes with their own instance variables. If you're
not sure what classes to create try these:

- `Animal`
- `Plant`
- `Car`
- `SuperHero`
- `SuperVillain`

## Putting it All Together

Classes can have multiple methods, including the `__init__()` method. Instance
variables can be assigned when the class instance is created then used by the
other class methods. Here's an example that brings those things together.

```Python
>>> class Greeter():
...     def __init__(self, name):
...         self.name = name
...
...     def hello(self):
...         return f"Hello, {self.name}"
...
>>> greeter = Greeter("Alan")
>>> greeter.hello()
'Hello, Alan'
```

## Time to Break Things

Now try this...

```Python
>>> class Person():
>>>     def __init__(self, first_name, surname):
>>>         # note that we're not using instance variables here
>>>         first_name = first_name
>>>         surname = surname
>>>
>>>     def full_name(self):
>>>         # will this work without using instance variables above?
>>>         return f"{first_name} {surname}"

>>> alan_turing = Person("Alan", "Turing")
>>> alan_turing.full_name()
# what gets returned here?
```

What happens when you run this? Try to explain what you observe – you'll find
our explanation in the next section.

## Reflect and Review

In this section, we learned how to define and instantiate a class, how to pass
arguments into the `__init__()` method and how to create instance variables.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain, in writing or to a peer:

- What is a class?
- How is a class defined?
- What is an instance of a class?
- How is a class instantiated?
- What is an instance variable?
- How are instance variables assigned?



[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=04_introducing_classes.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F05_scope.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F04_introducing_classes.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F04_introducing_classes.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F04_introducing_classes.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F04_introducing_classes.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F04_introducing_classes.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
