from lib._2_classes import *
from datetime import date


class TestInstances():

    def test_animal(self):
        new_animal = Animal()
        assert isinstance(new_animal, Animal)

    def test_vehicle(self):
        vw_golf = Vehicle()
        assert isinstance(vw_golf, Vehicle)


class TestAnimalsSpeak():

    def test_cat(self):
        azrael = Cat()
        assert azrael.speak() == 'miaow'

    def test_dog(self):
        white_fang = Dog()
        assert white_fang.speak() == 'woof'


class TestStringFormatter():

    def test_block_caps(self):
        subject = StringFormatter()
        assert subject.block_caps('hello') == "HELLO"

    def test_lower_case(self):
        subject = StringFormatter()
        assert subject.lower_case('HELLO') == 'hello'


class TestCalculator():

    def test_add(self):
        subject = Calculator()
        assert subject.add(2, 2) == 4

    def test_multiply(self):
        subject = Calculator()
        assert subject.multiply(2, 17) == 34

    def test_subtract(self):
        subject = Calculator()
        assert subject.subtract(2, 17) == -15

    def test_divide(self):
        subject = Calculator()
        assert subject.divide(30, 3) == 10


class TestApprentice():

    def test_name(self):
        subject = Apprentice('Jude', 'August 2045')
        assert subject.name == 'Jude'

    def test_cohort(self):
        subject = Apprentice('Jude', 'August 2045')
        assert subject.cohort == 'August 2045'

    def test_full_details(self):
        subject = Apprentice('Jude', 'August 2045')
        assert subject.format_details() == 'Jude, August 2045'


class TestCohort():

    def test_name(self):
        subject = Cohort('January 2060', '2060-01-01', '2060-01-08')
        assert subject.name == "January 2060"

    def test_start_date(self):
        subject = Cohort('January 2060', '2060-01-01', '2060-01-08')
        assert subject.start_date == date(2060, 1, 1)

    def test_end_date(self):
        subject = Cohort('January 2060', '2060-01-01', '2060-01-08')
        assert subject.end_date == date(2060, 1, 8)

    def test_duration(self):
        subject = Cohort('January 2060', '2060-01-01', '2060-01-08')
        assert subject.calculate_duration() == 7
