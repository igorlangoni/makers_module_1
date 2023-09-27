# Executing Python Files

Most engineers build programs in an iterative way. They start by writing
something small, then tweak it or add to it. They execute the code after every
small change to get feedback from the computer, perhaps in the form of error
messages.

If they had to write in the whole program every time it would get very tiresome.

Let's learn how to save programs in files and execute them from there.

<!-- OMITTED -->
## Learning Objectives

In this section, you will learn to:

* Execute Python code from a `.py` file

## Creating a Python file

Open your terminal and navigate to the documents directory like so:

```shell
; cd ~/Documents
```

Then create a new directory called `my_python_code` and create a file inside.

```shell
; mkdir my_python_code
; cd my_python_code
; touch hello_world.py
```

<details>
  <summary>:speech_balloon: I want to put my code somewhere else.</summary>

  <hr>
  
  If you're confident to do so, please go ahead!

  <hr>
</details>

Now open up Visual Studio Code and open the file. You can use `File -> Open...`
for this, then navigate to Documents and you should find the directory you
created. 

Type this code into the file:

``` python
# File: hello_world.py
print("Hello, world!")
```

<details>
  <summary>:speech_balloon: What is that <code># File</code> line for?</summary>

  <hr>
  
  Just for us to tell you what file this code is for. You don't actually have to
  type it in. 
  
  Also, just so you know, in Python lines starting with `#` are comments and
  aren't executed as code.

  <hr>
</details>

Now you can execute the code in that file like this

```shell
# In case you're not already in the right directory, let's go there
; cd ~/Documents/my_python_code

# Now let's run the code!
; python3 hello_world.py
```

You should see `Hello, World!` printed to the terminal. 

If so, mission accomplished. The `python3` command invokes the Python
_interpreter_, which is the program that runs your Python code.

<details>
  <summary>:speech_balloon: I see 'No such file or directory'</summary>

  <hr>
  
  You might be in the wrong place. Try running `pwd` to see what directory
  you are in. And then `ls` to verify that `hello_world.py` is really there.

  If you get really stuck here, reach out to your coach.

  <hr>
</details>

Use this as a chance to practice some of the things you have learned. Be sure to
`print()` anything that you would like to see printed to the terminal.

### Creating a Cheat Sheet (Optional)

You might want to create a series of files that contain notes or snippets for
yourself. Why not create your own cheat sheet?

```shell
; touch cheatsheet.py
```

Then you can write some notes in from earlier sections. Try adding some of the
string methods from before. Be sure to `print` them to see the results.

Then you can execute the code using `python3 cheatsheet.py` to check it is
right. Or, if you'd like to interact with it, you can run `python3 -i
cheatsheet.py` to load it into a REPL.

### Visualising Indentation

Now that you are using VS Code, you can make use of some extensions to make
your life easier.

We recommend installing [Indent
Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow).
This will help you visualise the all-important indentation in your Python code.

Feel free to spend a bit of time searching around for useful VS Code extensions.
Don't let it take over your life, but since you are an engineer it is your
privilege to customise your tools to the point they are just how you like them!

## Reflect and Review

In this section, you learned a second way of executing Python code – this time
from a file.

**Please pause at this point to reflect and review your learning...**

In a few sentences, explain:
* How to execute Python code that is written in a file
* What happens when you try to execute code from a file that doesn't exist
* The pros and cons of this new approach to code execution


[Log your progress and go to the next challenge](https://makers-event-logger.herokuapp.com/?event=09_executing_python_files.md&repository=makersacademy%2Fpython_foundations&redirect=chapter1%2F10_defining_functions.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2F09_executing_python_files.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
