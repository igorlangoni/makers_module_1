# Breaking Down Problems

Programs, as you have discovered, are made of small operations. Addition,
interpolation, an `if`, a loop, and many more you've yet to learn.

But we have big problems: in this case, validate that a password is over eight
characters and contains at least one from a list of special characters.

One of the programmer's jobs is to express the big problem using the small
pieces. To put it another way, coding is the art of combining small operations
to solve big problems.

**This may be hard at first.** Don't worry that you're not cut out for this just
because you are finding it challenging. It may take you some time to develop
this skill, and very likely years to become a confident practitioner.

There are many ways to go about breaking down problems. We'll give you three
"thinking tools" for now. Pick one and try it. If it doesn't work, try another
one.

- [The Good Friend Strategy](#the-good-friend-strategy)
- [The Lazy Mechanic Strategy](#the-lazy-mechanic-strategy)
- [The Baby Robot Strategy](#the-baby-robot-strategy)

## The Good Friend Strategy

Let's say your friend came to you and said "I'm really stressed! I have to move
house next week and I haven't done anything! I don't even know where to begin!".

You might first help them to calm down so they can think clearly. Then you might
have a conversation like this:

> You: What rooms do you have in your flat then?  
> Friend: There's the living room, the bedroom, the bathroom, and the hallway.  
> You: OK. Which is the smallest?  
> Friend: Uhh... the hallway.  
> You: OK, well let's start with that one then.  
> Friend: But! I don't have any boxes yet!!  
> You: That's OK! In that case let's make a list.  
> You: First we'll get boxes. Then we'll pack up the hallway. Then the bathroom,
> bedroom, and then the living room.  
> Friend: Ugh the living room has so much stuff in it though. It's got the
> kitchenette.  
> You: OK, let's break that up then.

Eventually you come to a final list.

> 1. Go to the hardware store.
> 2. Buy boxes and tape.
> 3. Go to the flat.
> 4. Pack up the hallway.
> 5. Pack up the bathroom.
> 6. Pack up the bedroom.
> 7. Pack up the kitchenette.
> 8. Pack up the living room.

As you're packing you realise you'll need somewhere to sleep on the day of the
move, but because you have a good plan you can just shift packing up the bedroom
til the end of the list.

That mental process of taking a big complex problem, figuring out what needs to
happen first, making a list, and then executing the plan, is the same mindset to
bring to this problem.

Bringing our attention back to programming, here are some questions to ask
yourself:

1. What needs to happen _first?_ Write it down in a list.
2. Do you know how to do that in code? If not, look it up and try it out in the
   REPL.
3. Is it too complicated still? If so, go back to step one and pick a smaller
   thing to do first.
4. What needs to happen _next?_ Write that down in your list.
5. Keep going until your list solves the whole problem and you know how to do it
   start to finish.
6. Write this out in the form of a program.

## The Lazy Mechanic Strategy

In this strategy, you don't even think about the problem. It does rely on having
some tests, but handily we've provided those.

Let's take a look at one of the drills.

```python
# Method name: truncate_string
# Purpose: truncates (shortens) a string to 10 characters
# Arguments: one string
# Rules:
#   If the string is longer than 10 characters
#   return the first 10 characters followed by '...'
#   If the string is 10 characters or less
#   return the whole string
# Example:
#   Call:    truncate_string("This is a long string")
#   Returns: "This is a..."
#   Call:    truncate_string("Short")
#   Returns: "Short"
```

Let's imagine you are the Lazy Mechanic. You look at this and you feel tired.
You don't want to deal with this. You hope by some chance it will work already.

You run the tests.

```
; pipenv run pytest -x
========================= test session starts ==========================
platform darwin -- Python 3.8.9, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/kaylack/Code/slug/materials/universe/foundations/python/chapter1/challenges/drills
collected 1 item

tests/test_4_defining_functions.py F                             [100%]

=============================== FAILURES ===============================
______________ test_truncate_string_longer_than_10_chars _______________

    def test_truncate_string_longer_than_10_chars():
>       assert truncate_string(
            "Oh what a joy to be alive!") == "Oh what a ..."
E       NameError: name 'truncate_string' is not defined

tests/test_4_defining_functions.py:72: NameError
======================= short test summary info ========================
FAILED tests/test_4_defining_functions.py::test_truncate_string_longer_than_10_chars
!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!
========================== 1 failed in 0.04s ===========================
```

UGH fine. OK what does the error say?

```
NameError: name 'truncate_string' is not defined
```

"Fine, OK," you think, "it wants me to define a method. We'll I'll just do that,
hopefully it's enough to stop this complaining."

You do the absolute minimum necessary. This is the key to the genius of the Lazy
Mechanic.

```python
def truncate_string():
    pass # UGH I guess you can't have totally empty methods in Python
```

```
; pipenv run pytest -x
========================= test session starts ==========================
platform darwin -- Python 3.8.9, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/kaylack/Code/slug/materials/universe/foundations/python/chapter1/challenges/drills
collected 1 item

tests/test_4_defining_functions.py F                             [100%]

=============================== FAILURES ===============================
______________ test_truncate_string_longer_than_10_chars _______________

    def test_truncate_string_longer_than_10_chars():
>       assert truncate_string(
            "Oh what a joy to be alive!") == "Oh what a ..."
E       TypeError: truncate_string() takes 0 positional arguments but 1 was given

tests/test_4_defining_functions.py:72: TypeError
======================= short test summary info ========================
FAILED tests/test_4_defining_functions.py::test_truncate_string_longer_than_10_chars
!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!
========================== 1 failed in 0.03s ===========================
```

"Won't you shut up!" you think, "What is it this time?"

```
TypeError: truncate_string() takes 0 positional arguments but 1 was given
```

"Right. It needs to take an argument. I'll add that then."

```python
def truncate_string(string):
    pass
```

The next error is:

```
assert truncate_string("Oh what a joy to be alive!") == "Oh what a ..."
AssertionError: assert None == 'Oh what a ...'
 +  where None = truncate_string('Oh what a joy to be alive!')
```

The Lazy Mechanic once again does the bare minimum and simply returns whatever
the test is asking for.

```python
def truncate_string(string):
    return "Oh what a ..."
```

And so:

```
assert truncate_string("Oh what a joy to be alive!") == "Oh what a ..."
assert truncate_string("Raise up the banners, let them fly, all. From Birnham wood to Dunsinane I cannot tint with fear!") == "Raise up t..."
AssertionError: assert 'Oh what a ...' == 'Raise up t...'
    - Raise up t...
    + Oh what a ...
```

"Ugh! I guess I have to do some work now," you think, "Seems it wants me to chop
off the first 10 characters and then add three dots on the end. FINE."

```python
def truncate_string(string):
    return string[0:10] + "..."
```

"Surely this is it," you, the Lazy Mechanic, think as you run the tests.

```
assert truncate_string("Help me!") == "Help me!"
AssertionError: assert 'Help me!...' == 'Help me!'
  - Help me!
  + Help me!...
  ?         +++
```

Like a dagger to the heart, you realise that yet more work is required. Glancing
back at the requirements you realise that if the string is ten or fewer
characters long you mustn't add the `...`.

So you once more undertake the horrible task of programming:

```python
def truncate_string(string):
    if len(string) >= 10:
        return string[0:10] + "..."
    else:
        return string
```

You run the tests again. Finally, they pass, and you can rest your eyes once
more.

It's easy to see the laziness of the mechanic as their weakness. But their
colleagues know better — the laziness is their greatest strength. By doing only
the absolute minimum necessary to fix the error in front of them, they naturally
break down the problem as they go.

## The Baby Robot Strategy

In the Baby Robot strategy we imagine a baby robot.

Like all robots, this baby robot will take instructions. However it is a very
annoying robot. It only does two things. If you give it an instruction it will
say "how?" and if you give it some code it will be silent.

Let's imagine if we asked the baby robot to do the above task:

> You: Baby Robot, please shorten a string to ten characters and put a `...` on
> the end, or if it's ten or fewer characters just give it back to me.  
> Baby Robot: How?  
> You: Well, first you'll need to define a function.  
> Baby Robot: How?  
> You: ...  
> You: `def truncate_string(string):`  
> Baby Robot: *Happy Silence*  
> You: OK. Now check if it is ten or fewer characters.  
> Baby Robot: How?  
> You: `if len(string) <= 10:`  
> Baby Robot: *Happy Silence*  
> You: ... alright.  
> You: Then return it.  
> Baby Robot: How?  
> You: `return string`  
> Baby Robot: *Happy Silence*  
> You: Then otherwise take the first ten characters and put a `...` on the end.  
> Baby Robot: How?  
> You: Well, you'll need to use an else first.  
> Baby Robot: How?  
> You: `else:`  
> Baby Robot: *Innocent Joy*  
> You: Right... next get the first ten characters.
> Baby Robot: How?  
> You: I don't know!! Can't you help at all?  
> Baby Robot: How?  
> You: ... *googles 'Python get first ten characters of string'*  
> You: `string[:10]`  
> Baby Robot: *Charming Look*  
> You: OK then stick a `...` on the end  
> Baby Robot: How?  
> You: `+ "..."`
> Baby Robot: *Stares*  
> You: Then return it.  
> Baby Robot: How?  
> You: Put `return` on the start.  
> Baby Robot: How?  
> You: ...  
> You: `return string[:10] + "..."`  
> Baby Robot: *Silence*  
> Baby Robot: Done!  
> You: ... you didn't do anything!  
> Baby Robot: How?

Here's what you get:

```python
def truncate_string(string):
    if len(string) <= 10:
        return string
    else:
        return string[:10] + "..."
```

The secret inside the Baby Robot strategy is that the question 'how' is a
breaking down question. It requires you to articulate the steps necessary to
perform a task. By articulating the problem and then repeatedly questioning
'how?' you develop a process in very small steps.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fbreaking_down_problems.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fbreaking_down_problems.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fbreaking_down_problems.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fbreaking_down_problems.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fbreaking_down_problems.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
