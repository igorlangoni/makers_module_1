from lib._1_lists_and_dictionaries import *


def test_first_element():
    assert first_element([1, 2, 3]) == 1
    assert first_element([5, 6, 7]) == 5


def test_second_element():
    assert second_element([1, 2, 3]) == 2
    assert second_element([5, 6, 7]) == 6


def test_last_element():
    assert last_element([1, 2, 3]) == 3
    assert last_element([5, 6, 7]) == 7


def test_first_two_elements():
    assert first_two_elements([1, 2, 3]) == [1, 2]
    assert first_two_elements([5, 6, 7]) == [5, 6]


def test_first_three_elements():
    assert first_three_elements([1, 2, 3, 4]) == [1, 2, 3]
    assert first_three_elements([5, 6, 7, 8]) == [5, 6, 7]


def test_total():
    assert total([1, 2, 3, 4]) == 10
    assert total([5, 6, 7, 8]) == 26


def test_lowest_number():
    assert lowest_number([2, 5, 3, 1, 4]) == 1
    assert lowest_number([22, 66, 33, 11, 44, 11]) == 11


def test_highest_number():
    assert highest_number([2, 5, 3, 1, 4]) == 5
    assert highest_number([22, 66, 33, 77, 44, 77]) == 77


def test_the_beatles():
    assert the_beatles() == ['john', 'paul', 'george', 'ringo']


def test_i_joined_the_beatles():
    assert i_joined_the_beatles("xavier") == [
        'john', 'paul', 'george', 'ringo', 'xavier']
    assert i_joined_the_beatles("sandra") == [
        'john', 'paul', 'george', 'ringo', 'sandra']


def test_we_joined_the_beatles():
    assert we_joined_the_beatles(["xavier", "sandra"]) == [
        'john', 'paul', 'george', 'ringo', 'xavier', 'sandra']
    assert we_joined_the_beatles(["james"]) == [
        'john', 'paul', 'george', 'ringo', 'james']


def test_remove_nones_from_list():
    assert remove_nones_from_list([None, 3, 2, 6, None, 7]) == [3, 2, 6, 7]
    assert remove_nones_from_list([None, None, None, None, None]) == []


def test_double_list():
    assert double_list([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
    assert double_list([5, 6, 7, 5]) == [5, 6, 7, 5, 5, 6, 7, 5]


def test_unique_elements():
    assert sorted(unique_elements([1, 1, 2, 2, 3, 3])) == [1, 2, 3]
    assert sorted(unique_elements([1, 2, 6, 6, 2, 2, 3, 3])) == [1, 2, 3, 6]


def test_add_to_list():
    assert add_to_list(['one', 'two', 'three'], 'four') == [
        'one', 'two', 'three', 'four']
    assert add_to_list([1, 1, 1], 2) == [1, 1, 1, 2]


def test_new_band_member():
    assert new_band_member({'drummer': 'kermit'}) == {
        'vocalist': 'miss piggy', 'lead_guitar': 'scooter', 'drummer': 'kermit'}
    assert new_band_member({'grawgwa': 'gwa'}) == {
        'vocalist': 'miss piggy', 'lead_guitar': 'scooter', 'grawgwa': 'gwa'}


def test_all_values():
    assert list(all_values({'one': 1, 'two': 2, 'three': 3})) == [1, 2, 3]
    assert list(all_values({'cat': 'meow', 'dog': 'woof', 'cow': 'moo'})) == [
        'meow', 'woof', 'moo']


def test_all_keys():
    assert list(all_keys({'one': 1, 'two': 2, 'three': 3})) == [
        'one', 'two', 'three']
    assert list(all_keys({'cat': 'meow', 'dog': 'woof', 'cow': 'moo'})) == [
        'cat', 'dog', 'cow']


def test_remove_nones_from_dictionary():
    assert remove_nones_from_dictionary(
        {'one': None, 'two': 2, 'three': 3}) == ({'two': 2, 'three': 3})
    assert remove_nones_from_dictionary(
        {'cat': 'meow', 'dog': None, 'cow': 'moo'}) == ({'cat': 'meow', 'cow': 'moo'})


def test_touch_in():
    assert touch_in('Aldgate East', '2022/01/30 11:12') == (
        {'entrypoint': 'Aldgate East', 'time': '2022/01/30 11:12'})
    assert touch_in('Liverpool Street', '2023/02/27 10:01') == (
        {'entrypoint': 'Liverpool Street', 'time': '2023/02/27 10:01'})
