# How to debug any problem stress-free

So you're stuck on a problem. Something in your code doesn't work, and you can't for the life of you work out what it is or how to fix it. Don't worry, we've been there thousands of times before - after all, debugging is a core part of being a Web Developer. Fortunately we've discovered a systematic process which when followed step-by-step can pretty much guarantee you'll track down a bug in no time at all - it can even be enjoyable!

## The steps

The steps are:

1. Take a break
2. Rubber duck
3. Check your assumptions
4. Follow the flow and get visibility
5. Repeat

## 1 - Take a Break

As soon as you've become aware that you have a difficult bug and you're stuck the most important thing you can do is take a break at that point. There's been many times when we've been stuck for a long time on something and reluctantly taken a break, only to come back five minutes later and instantly see the solution to the problem.

## 2 - Rubber Duck

Explaining a bug out loud is can really help with clarifying a bug or thinking of possible reasons the bug is happening.  It's surprising how often you'll get half way thorough your explanation and suddenly say "Of course! I should try [blank]".

If you're pairing, talk the bug thorough together.  If you're not pairing, ask someone to let you explain the problem to them.  If there's no one else around, explain your bug to a yellow rubber duck (or other inanimate object).  (It really does work!)

![Rubber Duck](https://hattonsimages.blob.core.windows.net/products/RubberDuck_3170853_Qty1_1.jpg)

So let's say at this point you turn to your pair and describe the problem as "whenever I try and save my user to the database in Rails, no error is thrown but the user does not get saved into the database"

## 3 - Check your assumptions

List your assumptions about what happens when your code runs.  Actually write them down! Prove to yourself that each assumption is correct by following the flow and getting visibility.  Start with the assumptions that are most likely to be incorrect.

Some example assumptions:

* The data is being passed correctly through to the user model.
* The method used to save the user model to the DB is working.
* The data is not reaching the DB.
* An error should be thrown when the user is saved.

## 4 - Follow the flow and get visibility

As you try to understand your program, there are two basic things you'll want to find out:

**Which parts of your program are running, and what order are they running in?**

**What are the values of relevant variables, and are they what you expected?**

Here are some techniques:

* Print out a variable or a "hello we reached this point in the code!" string
  * Ruby: `p`
  * Python: `print`
  * JavaScript: `console.log`

* Read the error description and stack trace.

* Look at the Network tab of the Chrome developer tools to see request and response data.

* Look at the Elements tab of the Chrome developer tools to see the content and styling of web pages.

* Pause and step through your code, line by line:
  * Ruby: `binding.irb`
  * Python: The VS Code debugger (see [Debugging 2 in Golden
    Square](https://github.com/makersacademy/golden-square-in-python/blob/main/challenges/07_intermezzo_debugging_2.md))
    or, for the advanced user [`pdb`](https://docs.python.org/3/library/pdb.html)
  * JavaScript: `debugger` (JavaScript)

* Write yourself small, self-contained examples of language features or methods you're trying to understand:
  * Ruby: `irb`.
  * Python: `python`
  * JavaScript: the Chrome developer tools console, or `node`.

For further tips, see our blog post by Sam Morgan [How I solve hard problems](https://blog.makersacademy.com/how-i-solve-problems-a6a84d167598)

## 5 - Repeat

Once you've reached some conclusions based on your experiments, if you still haven't
fixed the problem then you'll need to run the steps again - at least you have ruled out one train of investigation.

## Further tips

* It doesn't matter what debugging tools you are using, but you should *always*
  be using some sort of tool - if you're using nothing you're going to have a
  really hard time conducting your experiments and fixing the bug.
* When trying to understand your code, run lots of little experiments (often
  this is simply putting a load of print statements in your code), generally the
  sign of an experienced debugger is someone who uses a large number of tests
  like this to analyse/experiment on the problem
* Keep things simple, changing too much at once is likely to introduce further
  bugs
* Make sure you're checking the against the actual data your system is receiving
  when running tests
* Don't forget to take out all of your debugging statements when you're done fixing the problem!

## Some further reading:

   * [The StackOverflow founder on Rubber Duck Debugging](http://blog.codinghorror.com/rubber-duck-problem-solving/)
   * [Zen of debugging](http://webadvent.org/2012/debugging-zen-by-ben-ramsey)
   * [JavaScript debugging](https://developer.chrome.com/devtools/docs/javascript-debugging)
   * [JavaScript debugging workshop](https://github.com/makersacademy/skills-workshops/tree/main/javascript_fundamentals/ES6_following_the_flow_and_getting_visibility_in_javascript) Includes some specific tactics for following the flow and getting visibility in JavaScript.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fdebugging.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fdebugging.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fdebugging.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fdebugging.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=pills%2Fdebugging.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
