# Scope

The term _scope_ refers to the places in which program objects, such as
variables, can be used. In the previous exercise, you saw that the local
variables `first_name` and `surname` were only available within the `__init__()`
method.  I.e. Their _scope_ is limited to the `__init__()` method.

Instance variables, however, have a broader _scope_ – they are available
anywhere within the instance of a class. So you can assign them in the
initializer method and then use then in another method, without problem. They
are not, however, available outside the class.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn
- What scope is
- What instance variables are
- The scope of an instance variable
- The scope of a local variable

## An Example

Here's a reminder of the example we gave in the previous section

```python
>>> class Person():
>>>     def __init__(self, first_name, surname):
>>>         # note that we're not using instance variables here
>>>         first_name = first_name
>>>         surname = surname

>>>     def full_name(self):
>>>         # will this work without using instance variables above?
>>>         return f"{first_name} {surname}"

>>> alan_turing = Person("Alan", "Turing")
>>> alan_turing.full_name()
>>> # what gets returned here?
```

Here's how you could fix it, using instance variables

```python
>>> class Person():
>>>     def __init__(self, first_name, surname):
>>>         # note that we are using instance variables here
>>>         self.first_name = first_name
>>>         self.surname = surname

>>>     def full_name(self):
>>>         # will this work by using instance variables above?
>>>         return f"{self.first_name} {self.surname}"

>>> alan_turing = Person("Alan", "Turing")
>>> alan_turing.full_name()
"Alan Turing"
```

## An Analogy

Maybe you'd like an analogy at this point. You could compare instance and local
variables to local and national newspapers.

Local variables are like local newspapers in that they're only available, or in
scope, within a specific neighbourhood (of the codebase). Instance variables are
like national newspapers in that they're available anywhere in the class.

> Note that instance variables are not in scope (available) outside of a class.

## Reflect and Review

In this short section, we learned about scope – the areas of a codebase in which
a variable is available.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain, in writing or to a peer:
- What is the scope of a local variable?
- What is the scope of an instance variable?


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=05_scope.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F06_putting_chapter_2_into_practice.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F05_scope.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F05_scope.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F05_scope.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F05_scope.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F05_scope.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
