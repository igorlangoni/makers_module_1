from lib.json_load import *

TEST_JSON_FILE_PATH = "./test.json"

def test_load_data_from_url():
    assert load_data_from_url("https://jsonplaceholder.typicode.com/users")[0]["username"] == "Bret"

def test_load_data_from_file():
    assert load_data_from_file(TEST_JSON_FILE_PATH)[0]["name"] == "The Shawshank Redemption"

def test_get_films_by_director():
    assert get_films_by_director(TEST_JSON_FILE_PATH, "Sidney Lumet") == ["12 Angry Men"]
    assert get_films_by_director(TEST_JSON_FILE_PATH, "Francis Ford Coppola") == ["The Godfather", "The Godfather: Part II"]
    assert get_films_by_director(TEST_JSON_FILE_PATH, "Quentin Tarantino") == []

def test_get_films_by_actor():
    assert get_films_by_actor(TEST_JSON_FILE_PATH, "Al Pacino") == ["The Godfather", "The Godfather: Part II"]
    assert get_films_by_actor(TEST_JSON_FILE_PATH, "Christian Bale") == ["The Dark Knight"]
    assert get_films_by_actor(TEST_JSON_FILE_PATH, "Adam Sandler") == []

def test_get_films_with_minimum_rating():
    assert get_films_with_minimum_rating(TEST_JSON_FILE_PATH, 9.3) == ["The Shawshank Redemption"]
    assert get_films_with_minimum_rating(TEST_JSON_FILE_PATH, 9.2) == ["The Shawshank Redemption", "The Godfather"]
    assert get_films_with_minimum_rating(TEST_JSON_FILE_PATH, 9.5) == []


def test_get_films_within_year_range():
    assert get_films_within_year_range(TEST_JSON_FILE_PATH, 2000, 2010) == ["The Dark Knight"]
    assert get_films_within_year_range(TEST_JSON_FILE_PATH, 1955, 1975) == ["The Godfather", "The Godfather: Part II", "12 Angry Men"]
    assert get_films_within_year_range(TEST_JSON_FILE_PATH, 1960, 1970) == []

def test_order_films_chronologically():
    assert order_films_chronologically(TEST_JSON_FILE_PATH) == ["12 Angry Men", "The Godfather", "The Godfather: Part II", "The Shawshank Redemption", "The Dark Knight"]

def test_order_films_most_recent_first():
    assert order_films_most_recent_first(TEST_JSON_FILE_PATH) == ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", "The Godfather", "12 Angry Men"]

def test_all_actors_starting_with_letter():
    assert all_actors_starting_with_letter(TEST_JSON_FILE_PATH, "a") == ["Aaron Eckhart", "Al Pacino"]
    assert all_actors_starting_with_letter(TEST_JSON_FILE_PATH, "l") == ["Lee J. Cobb"]
    assert all_actors_starting_with_letter(TEST_JSON_FILE_PATH, "g") == []