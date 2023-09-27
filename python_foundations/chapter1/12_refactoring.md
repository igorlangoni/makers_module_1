# Refactoring

Right after all your tests go green, you should pause for a moment to consider
how you got there and whether you could change your code to make it better in
some way – this is the art of refactoring.

Whilst refactoring, we don't add any new features (such as new rules about what
makes a valid password) but we might add new methods. Through refactoring, we
try to end up with code that is:

* Correct, meaning that your tests still pass
* Clear, so that its easy to read
* Concise, with little or no repetition

The ultimate goal of refactoring is to make the code easy to change in the
future. If you can be sure of one thing in software engineering is that change
will be necessary! It might be that your client changes their mind, or there was
a misunderstanding, a new user need is discovered or maybe the application just
continues to grow as planned. All of these scenarios involve changing, or
building upon, the code that you already have.

<!-- OMITTED -->

## Learning Objectives

In this section, you will learn to:

* Explain what refactoring is.
* Explain when to refactor
* Describe the benefits of refactoring
* Refactor your password validator solution

## Part One: A Potential Solution

We can't know exactly what code you wrote, but it might be something like this:

```python
def is_valid(password):
  if len(password) < 8:
    return False
  elif "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False
```

If so, bravo! You solved the problem perfectly well and now it's time to
refactor.

# Part Two: Refactor

We're now going to do three things that will make this code a little easier to
work with.

1. We'll create a new method that checks the length of the password
2. We'll create a new method that looks for the special characters
3. We'll use those two methods in our `if` statement

Along the way, we'll encounter a new thing: calling methods from inside other
methods.

The first method will look like this and it will return either `True`, when the
password is longer than 7 characters, or `False`, when it is shorter.

```python
def is_sufficient_length(password):
  # len(password) > 7 will evaluate to True or False
  return len(password) > 7
```

The second method will look like this. It will return either `True` or `False`
depending on whether the password contains the special characters.

```python
def are_special_chars_included(password):
  if "!" in password:
    return True
  elif "@" in password:
    return True
  elif "$" in password:
    return True
  elif "%" in password:
    return True
  elif "&" in password:
    return True
  else:
    return False
```

And our `is_valid()` method would look like this.

```python
def is_valid(password):
  if is_sufficient_length(password) and are_special_chars_included(password):
    return True
  else:
    return False
```

This is an improvement because our rules are now contained within methods which
have descriptive names.

You may have noticed that since the condition evaluates to `True` or `False` we
could also further refactor it to this:

```python
def is_valid(password):
  return is_sufficient_length(password) and are_special_chars_included(password)
```

## Reflect and Review

In this section, we introduced the practice of refactoring. From now on, we'll
expect you to refactor your code, as you go along, with a strong focus on
readability and ease of change.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:

* Which of the two above password validator solutions you prefer
* What refactoring is
* When you should do it
* The benefit of refactoring



[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=12_refactoring.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F13_review_learning.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F12_refactoring.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
