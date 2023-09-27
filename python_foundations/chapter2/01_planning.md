# Planning Your Next Project: Password Manager

In this section, we'll start to think about the next task, which will be to
build a password manager.

We'll then derive some learning objectives and work through them in the
following sections.

## Part One: Requirements

The password manager will need to:

* Allow a user add new passwords
* Allow a user to view a specific password
* Allow a user to see a list of all the services for which a password has been
  stored

**We're deliberately leaving out the ability to delete passwords.**

Take a moment to think about how you would code this out. One early question
will be: how do we store the passwords?

## Part Two: Learning Plan

It might be tempting to think that you already know everything you need to do
this project but beware the [Law of the
Instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument), which
describes the practice of using whatever tools one has to hand for accomplishing
any and all tasks.

- You'll store the passwords in a `Dictionary`, which is like a list of things
  where each item has a label. In this case, the label will be the name of a
  service, like MySpace, and the item will be the actual password.

- So you'll need to learn about how to create a `Dictionary` and how to add /
  remove things from a `Dictionary`.

- When we come to list out all the services, we'll use a `Dictionary` method
  which generates an `List` (sometimes referred to as an `Array`). Compared to
  Dictionary, Lists are, just like they sound, more basic lists of things. So
  we'll learn about how to make an `List` first, before learning about
  `Dictionary`s.

- Finally, to do a really great job of this, we'll need to learn about classes.
  Classes are used to contain, or _encapsulate_ related methods and variables.
  Used well, they provide another mechanism for programmers to break up the code
  into logical units that are easy to reason about and understand. This is very
  similar to the way in which we broke up the password validator into a number
  of short methods.


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=01_planning.md&repository=makersacademy%2Fpython_foundations&redirect=chapter2%2F02_introducing_lists.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F01_planning.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F01_planning.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F01_planning.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F01_planning.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter2%2F01_planning.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
