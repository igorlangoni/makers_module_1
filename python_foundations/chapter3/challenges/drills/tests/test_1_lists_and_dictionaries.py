from lib._1_lists_and_dictionaries import *


class TestArrays():

    def test_fourth_element(self):
        assert fourth_element([1, 2, 3, 4, 5]) == 4
        assert fourth_element([3, 1, 44, 1]) == 1

    def test_average(self):
        assert average([1, 2, 3, 4, 5]) == 3
        assert average([1, 2, 3, 4, 5, 6]) == 3.5

    def test_lowest_squared(self):
        assert lowest_squared([2, 3, 4, 5]) == 4
        assert lowest_squared([5, 3, 4, 3]) == 9

    def test_highest_squared(self):
        assert highest_squared([2, 3, 4, 5]) == 25
        assert highest_squared([77, 3, 4, 3]) == 5929

    def test_starts_with_a(self):
        assert starts_with_a(
            ['aardvark', 'apple', 'zebra', 'zinc']) == ['aardvark', 'apple']
        assert starts_with_a(
            ['banana', 'apple', 'orange', 'avocado']) == ['apple', 'avocado']

    def test_starts_with_a_vowel(self):
        assert starts_with_a_vowel(
            ['apple', 'pear', 'orange', 'egg', 'indigo', 'uncle']) == ['apple', 'orange', 'egg', 'indigo', 'uncle']
        assert starts_with_a_vowel(
            ['cat', 'dog', 'zebra', 'zinc']) == []

    def test_reverse_each_element(self):
        assert reverse_each_element(
            ['one', 'two']) == ['eno', 'owt']
        assert reverse_each_element(
            ['one', 'two', 'three']) == ['eno', 'owt', 'eerht']

    def test_sort_by_last_letter(self):
        assert sort_by_last_letter(
            ['apple', 'pear', 'satsuma']) == ['satsuma', 'apple', 'pear']
        assert sort_by_last_letter(
            ['banana', 'apple', 'carrot', 'avocado']) == ['banana', 'apple', 'avocado', 'carrot']

    def test_greater_than_5(self):
        assert greater_than_5(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [6, 7, 8, 9, 10]
        assert greater_than_5(
            [9, 3, 44, 7]) == [9, 44, 7]

    def test_greater_than(self):
        assert greater_than(
            [1, 2, 3, 4, 5], 3) == [4, 5]
        assert greater_than(
            [9, 3, 44, 7], 10) == [44]

    def test_less_than(self):
        assert less_than([1, 2, 3, 4, 5], 3) == [1, 2]
        assert less_than([9, 3, 44, 7], 10) == [9, 3, 7]

    def test_words_shorter_than(self):
        assert words_shorter_than(
            ['tree', 'rainbow', 'desk', 'computer'], 5) == ['tree', 'desk']
        assert words_shorter_than(
            ['banana', 'apple', 'orange', 'nut', 'avocado'], 6) == ['apple', 'nut']

    def test_all_above(self):
        assert all_above([2, 3, 4, 5], 1) == True
        assert all_above([2, 3, 4, 5], 2) == False

    def test_all_below(self):
        assert all_below([2, 3, 4, 5], 6) == True
        assert all_below([2, 3, 4, 5], 5) == False

    def test_multiply_each_by(self):
        assert multiply_each_by(
            [1, 2, 3, 4, 5], 2) == [2, 4, 6, 8, 10]
        assert multiply_each_by(
            [1, 2, 3, 3, 5], 3) == [3, 6, 9, 9, 15]


class TestDictionaries():

    def test_values_summed(self):
        assert values_summed({'one': 1, 'two': 2, 'three': 3}) == 6
        assert values_summed({'one': 1, 'two': 2, 'three': 3, 'four': 4}) == 10

    def test_add_key_value_pair(self):
        assert add_key_value_pair(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'beans', 2.0
        ) == (
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0, 'beans': 2.0}
        )
        assert add_key_value_pair(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'onion rings', 3.0
        ) == (
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0, 'onion rings': 3.0}
        )

    def test_remove_key_value_pair(self):
        assert remove_key_value_pair(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'slaw'
        ) == (
            {'chips': 2.5, 'burger': 10, 'salad': 3.0}
        )
        assert remove_key_value_pair(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'burger'
        ) == (
            {'chips': 2.5, 'slaw': 2.0, 'salad': 3.0}
        )

    def test_where_value_below(self):
        assert where_value_below(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 5
        ) == (
            {'chips': 2.5, 'slaw': 2.0, 'salad': 3.0}
        )
        assert where_value_below(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 3
        ) == (
            {'chips': 2.5, 'slaw': 2.0}
        )

    def test_where_key_starts_with(self):
        assert where_key_starts_with(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 's'
        ) == (
            {'slaw': 2.0, 'salad': 3.0}
        )
        assert where_key_starts_with(
            {'chips': 2.5, 'burger': 10, 'slaw': 2.0, 'salad': 3.0}, 'b'
        ) == (
            {'burger': 10}
        )


