# Chapter 1 Challenges

Well done for reaching the chapter 1 challenges! Here, you'll find two types of
exercise: drills and a programming challenge. Do the drills first and then move
onto the programming challenge. You must complete both before going
[back](../11_putting_chapter_1_into_practice.md) to reflect on your progress.

## Initial Setup

### Getting the Code

To get the exercises onto your machine, you'll need to fork and then clone this
repo.

<!-- OMITTED -->

### Installing Dependencies

Before starting either the drills or the programming challenge, you need to
install some dependencies — programs upon which these exercises depend.

In Python, dependencies are managed using tools called package managers. Python
has a few. 

We're going to use `pipenv`. Here's how to install it:

```shell
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version
pipenv, version ...
```

If you have trouble with this, contact your coach.

## Setting up the tests

[Pytest](https://docs.pytest.org/) is a tool used to run tests that ensure
your program does what it needs to do. In the near future you'll be writing your
own tests but, for now, you'll use the tests that we wrote for you.

Your goal is to make all the tests pass.

To run the tests, make sure you're in either the `drills` or `program` directory
and then run `pytest`. This will execute all the tests inside the `tests`
directory.

Here's how to start:

```shell
; cd path/to/python_foundations
; cd chapter1/challenges/drills

# This will install the dependencies (pytest)
; pipenv install

# This will run all of the tests
; pipenv run pytest
# Very noisy right! Lots of stuff to read.

# BUT, there is a better way.
# This will run all of the tests until one fails, then show you the error
; pipenv run pytest -x
# You should probably run this one!
```

<details>
  <summary>:confused: I see an error about `python_full_version`?</summary>

  ---

  Your `pipenv` may be outdated and subject to a bug with newer `Pipfile`s.

  ```shell
  ; pipenv --version
  2022.9.24 # If you see something in September 2022, try this
  ; pip3 install "pipenv>=2022.11.5" -U
  # pip3 will update pipenv for you

  # Then try running `pipenv install` again
  ; pipenv install
  ```

  If that works, great! If not, contact your coach.

  ---
</details>

**Important note:** until now you have used the command `python3` to run your
code. You should not do this when using a `pipenv` environment because it will
not pick up your dependencies.

Get into the habit now of running this whenever using `pipenv`:

```shell
; pipenv run python my_file.py
```

You will probably forget and sometimes this will cause errors. That's OK, just
treat it as a reminder.

## Drills

Drills are short, tightly focused exercises which get harder as you progress.
Leave alone any files with `test` at the start of them.

Open `drills/lib/_1_calling_methods.py` in VS Code to begin! Remember to run
`pipenv run pytest -x` often when you're in the `drills` folder! 

You will notice an `IMPORT ERROR` if you try and run `pipenv run pytest -x` in
the wrong directory.

### Getting Started

1. Find the first set of drills
    * For chapter 1, that's `drills/lib/_1_calling_methods.py`
    * You'll find further instructions there
2. Work on the first challenge
3. Run `pipenv run pytest -x` to check your answer
4. Keep going until all the tests for that set of drills are passing
5. Move on to the next set
6. Keep going until all the tests for all the sets are passing
7. :warning: [Zip up](../../pills/creating_zipfiles.md) your code so that you're
   ready to share it later
8. Move on to the programming challenge

## Programming Challenge

In this exercise you'll bring together several different concepts to build a
password validator.

:warning: Please do a [screen recording](../../pills/screen_recordings.md) of
yourself working on this exercise so that your coach can see how you're getting
on. You can upload it, along with your code, using the form at the end of this
file.

### Getting Started

1. [Start recording](../../pills/screen_recordings.md) 🎥
2. Open up `program/lib/password_validator.py` and read the instructions
3. Navigate to the `program` directory in your terminal and run `pipenv run
   pytest -x`
4. Work in small steps to complete the `is_valid()` method.
5. Run `pipenv run pytest -x` regularly to check your progress.
6. Keep going until all the tests pass

If you get stuck, consult the [Breaking Down
Problems](../../pills/breaking_down_problems.md) guide.

## Submitting Your Work

Use [this form](https://airtable.com/shrvo9ePjlwnaiLv5?prefill_Item=pyf_ch1) to
submit your code and screen recording

## What Next?

Go back [here](../11_putting_chapter_1_into_practice.md#reflect-and-review)
to reflect on your progress before moving on.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
