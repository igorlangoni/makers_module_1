# Error Messages Are Your Friends

We ended the previous section on a cliffhanger, trying to decipher the meaning
of an error message. In this short section, you'll see how to break it down and
extract useful information.

<!-- OMITTED -->
## Learning Objectives

In this section, you'll learn to:

* Explain the purpose of error messages
* Extract useful information from a straightforward error message

## Dissecting Your First Error Message

You probably got something a lot like this at the end of the last section. Did
you figure out what it means?

```python
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> 
```

Because we didn't use quotation marks, Python doesn't recognise `hello` as a
`string`. Instead, `hello` is interpreted as the name of a variable or something
else Python should know about. But Python can see we haven't defined a variable
called `hello` and so it responds with an error. To put it simply: Python
doesn't know what that `hello` thing is.

Let's break this error message down.

```python
  File "<stdin>", line 1, in <module>
```

We're going to ignore that line for now — it will make more sense later when we
write Python code in files.

<details>
  <summary>:speech_balloon: But I really do want to know now — I can handle it!</summary>

  <hr>
  
  OK — if you insist!

  This line is telling us the location that the error occurred.
  
  It's telling us that the `File` is `<stdin>`. `<stdin>` is a special imaginary
  file used to describe something called 'standard input'. 'standard input'
  means whatever you're typing into the terminal. 

  `line 1` is referring to the first line of the code we typed in. There's only
  one line that we typed in, so it has to be the first.

  `in <module>` is telling us about the location of the code causing the error
  in the structure of the program. In this case, it says `<module>` which refers
  to the overall 'main area' of the program.

  If that's not clear — it's OK. It's not important just yet.

  <hr>
</details>

Let's instead look at the last line. This tells us what the error is:

```python
NameError: name 'hello' is not defined
```

In plain English, Python is referring to `hello` as a `name` because, without
the quotation marks, it looks like the name of a variable and we're being told
that there is nothing with that name.

Try it out: if we do the same thing, but say goodbye instead, what changes?

## Another Error

Now do this to generate one more error message.

```python
>>> 1 + 1     # This will work
>>> "a" + "b" # This will work
>>> 1 + "a"   # This will error
```

Try to figure out what this means. Some of the language will seem cryptic, but
you may be able to make a good guess.

## Reflect and Review

In this section, we picked apart an error message to find the useful
information. Hopefully, you'll welcome the next one you see as a helpful old
friend.

**Please pause at this point to reflect and review your learning...**

* How much of each error message was actually useful to you?
* What is your natural reaction to seeing an error message?
* How might a confident professional engineer react to an error message?


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=02_error_messages.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F03_functions.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F02_error_messages.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
