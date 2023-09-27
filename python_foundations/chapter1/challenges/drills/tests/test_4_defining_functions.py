from lib._4_defining_functions import *


def test_say_hello():
    assert say_hello() == 'hello'


def test_say_goodbye():
    assert say_goodbye() == 'goodbye'


def test_say_hello_to():
    assert say_hello_to("Amy") == "Hello, Amy!"


def test_say_goodbye_to():
    assert say_goodbye_to("Will") == "Goodbye, Will!"


def test_square():
    assert square(5) == 25
    assert square(3) == 9
    assert square(8) == 64
    assert square(0) == 0


def test_divisible_by_three():
    assert divisible_by_three(99) == True
    assert divisible_by_three(98) == False


def test_add():
    assert add(5, 5) == 10


def test_multiply():
    assert multiply(5, 2) == 10


def test_add_number_strings():
    assert add_number_strings("4", "5") == 9


def test_multiply_number_strings():
    assert multiply_number_strings("4", "5") == 20


def test_both_odd():
    assert both_odd(1, 3) == True
    assert both_odd(1, 2) == False
    assert both_odd(4, 7) == False
    assert both_odd(4, 8) == False


def test_both_even():
    assert both_even(2, 8) == True
    assert both_even(1, 2) == False
    assert both_even(4, 7) == False
    assert both_even(1, 7) == False


def test_one_odd():
    assert one_odd(3, 6) == True
    assert one_odd(6, 3) == True
    assert one_odd(8, 6) == False
    assert one_odd(3, 9) == True


def test_one_even():
    assert one_even(3, 6) == True
    assert one_even(7, 7) == False
    assert one_even(4, 9) == True
    assert one_even(4, 6) == True


def test_truncate_string_longer_than_10_chars():
    assert truncate_string(
        "Oh what a joy to be alive!") == "Oh what a ..."
    assert truncate_string(
        "Raise up the banners, let them fly, all. From Birnham wood to Dunsinane I cannot tint with fear!") == "Raise up t..."
    assert truncate_string("Help me!") == "Help me!"
