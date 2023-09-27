# Extension Challenge: Loading and saving files

Now that you have completed all of the core material for this module we are
going to give you an extra challenge.

In this challenge you will use Python to analyse some data about air quality.

In the process, you will learn about using Python to load and save files, and
you will use things you have learned in earlier challenges.

Being able to handle data files — loading, parsing, manipulating, summarising,
etc. — can be a useful skill. For example, perhaps you could be asked to analyse
some data from a system to determine whether it's performing acceptably under
load.

## Initial Steps

Before starting this challenge, you should familiarise yourself with the file
containing the data you will be using.

Some data has been downloaded from Kaggle, originally from
https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set, called
`AirQuality.csv` and in your `program/` directory in this repository. The data
is described as follows:

> This dataset contains the responses of a gas multisensor device deployed on
> the field in an Italian city. Hourly responses averages are recorded along
> with gas concentrations references from a certified analyser.

Don't worry — we're not going to quiz you on your knowledge about Italian air
nor units of gas concentration! We are however going to use this data in this
extended challenge. Take a moment now to open up the file and familiarise
yourself with the contents. Also of note, despite its ".csv" file extension, the
file doesn't contain "Comma-Separated Values" but uses ";" to separate the
different fields instead. For example:

```
Cell 1 data;Cell 2 data;etc.
```

If you've not met anything like this format before, you can think of the data in
the file as tabular data, with each row in the table converted into a row in the
file. You can read more about "separated value" data such as this in
https://en.wikipedia.org/wiki/Comma-separated_values, noting again the file from
Kaggle uses ";" to separate the data rather than ",".

## Programming Challenge

In this exercise you'll be using the previously downloaded data on air quality,
a number of Git/GitHub and Python skills from earlier challenges, as well as
finding out about some new things you can do in Python.

You might find this exercise more open-ended — there are many ways of achieving
what's being asked for — and this is by design, to allow you to practice your
skills, research new ways of doing things, as well as experiment.

### Getting Started

1. Open up `program/lib/data_manipulation.py` and read the instructions
2. Navigate to the `program` directory in your terminal and run `pipenv install`
3. Run `pipenv run pytest -x` to run all the tests until one fails
4. Work in small steps to complete the functions
5. Re-run your tests regularly to check your progress
6. Keep going until all the tests pass

## Submitting Your Work

1. Contact your coach(es) and/or others in your cohort who have also done this
   challenge and talk through your solution.

## Extra Tasks

Some optional ideas, if you'd like to spend more time practising parsing and
manipulating data:

* Browse Kaggle for other datasets of interest, download them, and write a
  Python script that uses the files. For example:
  * Open them
  * Extracts certain parts
  * Uses the data (for instance by averaging)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F01_files%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F01_files%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F01_files%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F01_files%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F01_files%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
