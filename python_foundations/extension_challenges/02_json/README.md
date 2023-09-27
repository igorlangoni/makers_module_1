# Extended Challenge: Parsing JSON content

## What is JSON?

JSON stands for JavaScript Object Notation, but don't be fooled - it's a popular format for transmitting structured data, 
regardless of which underlying language you're working with. It's also the format which is the backbone for most APIs - you'll 
hear much more about them in the coming modules.

While JSON structures are often very complex, they're easy for a machine to handle, and aren't too difficult for the human eye 
either. Consider this fictional list of pets:

```json
[
  {
    "name": "Poochie",
    "animal": "dog",
    "owner": {
        "name": "Ollie Owner",
        "address": {
            "house_number": 12,
            "street_name": "High Street",
            "town_or_city": "London"
        }
    },
    "age": 4
  },
  {
    "name": "Tiddles",
    "animal": "cat",
    "owner": {
        "name": "Cara Carer",
        "address": {
            "house_number": 4,
            "street_name": "Kings Road",
            "town_or_city": "London"
        }
    },
    "age": 8    
  }
]
```

This is a relatively straightforward example - so straightforward that you might wonder why we don't store it in a CSV. This will 
become clearer when you work with more complex data examples, where data can have a "one-to-many" relationship. (For example, imagine 
if an animal has two owners; this would be very easy to modify within a JSON data structure, whereas in a CSV you'd have to create an "owner2" 
column.) 

## Loading data from a file

Sometimes, similar to the previous exercise, you'll load static JSON data from a file. Opening and closing a file is just the same as in 
the previous exercise, but when you're dealing with JSON, you'll utilise an additional `import` statement to convert the file's contents into 
a JSON object:

```python
import json

# Open the file as normal
file = open("myfile.json")

# Convert the file's contents to a JSON object
json_data = json.load(file)

# Now, json_data is a Python dictionary
# containing all of the data from the file.

# Once you are finished...
file.close()

```

There are many reasons why you might wish to load data dynamically in such a manner. You could use it, for example, as an abstraction layer 
for your test data: you could put all of the data which drives your test scenarios into a JSON file. This would allow anybody to maintain and 
modify your test data, regardless of whether they have any knowledge of the Python code which drives the tests.

## Loading data from a URL

It's equally likely that you might find yourself wanting to load JSON from a URL (for instance, to import data from another website).

Thankfully, Python has a built-in library called [urllib](https://docs.python.org/3/library/urllib.html) which makes this 
into an easy task. While it has many advanced configuration options (for instance, to allow for usernames, passwords, 
proxies and other authentication challenges), the basics of retrieving data from a URL are straightforward:

```python
from urllib.request import urlopen

url = urlopen("https://api.open-meteo.com/v1/forecast?latitude=51.5002&longitude=-0.1262&current_weather=true")
response = url.read().decode('UTF-8')
print(response)
```

If you run this code, you should see something similar to the below (depending on the current temperature, and the latitude/longitude that you enter):

```
{"latitude":51.5,"longitude":-0.120000124,"generationtime_ms":0.2340078353881836,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":6.0,"current_weather":{"temperature":14.4,"windspeed":21.7,"winddirection":212.0,"weathercode":3,"time":"2022-11-02T11:00"}}
```

Great! That _looks_ like JSON data. Unfortunately, at the moment, it's not; technically, it's still just a string. If you try to print 
`response['current_weather']`, you'll get an error `TypeError: string indices must be integers` as the data is not ready to be interrogated 
in such a fashion just yet.

We need to instruct Python to change the datatype to JSON, for which we need to add an extra `import` at the top of our script:

```
import json
```

Now, we can utilise the JSON library to convert our data, and iterate over it just like a real object:

```
json_data = json.loads(response)
print(json_data['current_weather'])
```

**IMPORTANT NOTE:** Note that the method here is named `json.loads()` - this is the name of the method in the JSON library which takes a `String` as input, 
and converts it to a JSON object. In the file example above, it uses `json.load()` - that's what you use if your input parameter is a `File` object. (Don't look at 
us like that - we're just telling you, we didn't name the darn things.)

It should output today's temperature. Hooray!

## Programming Challenge

In this exercise you'll be connecting to another real-world data source, loading its data in real-time, and writing functions to handle the 
response. We've kept the instructions light, to encourage you to investigate more about how to work with JSON for yourself.

### Getting Started

1. Open up `program/lib/json_load.py` and read the instructions
2. Navigate to the `program` directory in your terminal and run `pipenv install`
3. Run `pipenv run pytest -x` to run all the tests until one fails
4. Work in small steps to complete the functions
5. Re-run your tests regularly to check your progress
6. Keep going until all the tests pass

## Submitting Your Work

1. Contact your coach(es) and/or others in your cohort who have also done this
   challenge and talk through your solution.

## Extra Tasks

Some optional ideas, if you'd like to spend more time practising parsing JSON data from file or URL:

* Browse [this list of public APIs](https://github.com/toddmotto/public-apis), and load/manipulate data from some interesting-sounding endpoints.
* For an extra challenge, pick an API which requires simple authorisation, and work out how to authenticate using Python's URL 
library (e.g. by sending a username and password in the request).
* Try combining this with the previous exercise: Load some data from JSON (URL or file), loop through it in your code, and save the data to a CSV file.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F02_json%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F02_json%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F02_json%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F02_json%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=extension_challenges%2F02_json%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
