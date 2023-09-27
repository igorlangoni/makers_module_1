from urllib.request import urlopen
import json

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
def load_data_from_url(url):
    my_url = urlopen(url)
    response = my_url.read().decode('UTF-8')
    json_data = json.loads(response)
    return json_data

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):
    file = open(filename)
    json_data = json.load(file)
    return json_data

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    file = open(filename)
    json_data = json.load(file)
    movie_list = [movie['name'] for movie in json_data if movie['director'] == director]
    return movie_list

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    file = open(filename)
    json_file = json.load(file)
    actor_movie_list = [movie['name'] for movie in json_file if desired_actor in movie['stars']]
    return actor_movie_list

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]

def get_films_with_minimum_rating(filename, rating):
    file = open(filename)
    json_file = json.load(file)
    movie_above_rating = [movie['name'] for movie in json_file if rating <= movie['imdb_rating']] 
    return movie_above_rating

# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    file = open(filename)
    json_file = json.load(file)
    movie_from_year_range = [movie['name'] for movie in json_file if start_year < movie['year'] and end_year > movie['year']]
    return movie_from_year_range

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    json_file = load_data_from_file(filename)
    sorted_list = sorted(json_file, key=lambda movie: movie['year'])
    movie_chrono_list = [movie['name'] for movie in sorted_list]
    return movie_chrono_list


# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    json_file = load_data_from_file(filename)
    sorted_list = sorted(json_file, key=lambda movie: movie['year'], reverse=True)
    movie_rev_chrono_list = [movie['name'] for movie in sorted_list]
    return movie_rev_chrono_list

# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    json_file = load_data_from_file(filename)
    full_actors_list = [movie['stars'] for movie in json_file if movie['stars']]
    actors_by_first_letter = []
    for stars in full_actors_list:
        for star in stars:
            if star[0] == letter.upper():
                actors_by_first_letter.append(star)
    return sorted(set(actors_by_first_letter))