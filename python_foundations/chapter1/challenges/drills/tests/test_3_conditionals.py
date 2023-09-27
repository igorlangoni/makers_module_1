from lib._3_conditionals import *

def test_fizz_buzz():
    assert fizz_buzz(7) == 7
    assert fizz_buzz(6) == "fizz"
    assert fizz_buzz(10) == "buzz"
    assert fizz_buzz(30) == "fizzbuzz"


def test_reply_to():
    assert reply_to("hello") == "hi"
    assert reply_to("good morning") == "good morning to you too"
    assert reply_to("howdy") == "howdy"
    assert reply_to("bonjour") == "bonjour"


def test_deduct_10_if_possible():
    assert deduct_10_if_possible(10) == 0
    assert deduct_10_if_possible(11) == 1
    assert deduct_10_if_possible(9) == 9


def test_top_up_to_100():
    assert top_up_to_100(99) == 100
    assert top_up_to_100(100) == 100
    assert top_up_to_100(101) == 101
