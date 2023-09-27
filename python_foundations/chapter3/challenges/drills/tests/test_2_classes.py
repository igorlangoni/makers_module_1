from lib._2_classes import *


class TestGreeter():

    def test_hello(self):
        subject = Greeter()
        assert subject.hello('Azrael') == 'Hello, Azrael!'

    def test_goodbye(self):
        subject = Greeter()
        assert subject.goodbye('Morticius') == 'Goodbye, Morticius!'

    def test_good_night(self):
        subject = Greeter()
        assert subject.good_night('Jo') == 'Good night, Jo!'

    def test_good_morning(self):
        subject = Greeter()
        assert subject.good_morning('Jo') == 'Good morning, Jo!'


class TestBasket():

    def test_add_items_then_list(self):
        subject = Basket()
        subject.add('eggs')
        subject.add('milk')
        subject.add('bread')
        assert subject.list_items() == ['eggs', 'milk', 'bread']


class TestCalculator():

    def test_add(self):
        subject = Calculator()
        assert subject.add(1, 1) == 2

    def test_multiply(self):
        subject = Calculator()
        assert subject.multiply(2, 17) == 34

    def test_subtract(self):
        subject = Calculator()
        assert subject.subtract(2, 17) == -15

    def test_divide(self):
        subject = Calculator()
        assert subject.divide(30, 3) == 10

    def test_list_history(self):
        subject = Calculator()
        subject.add(1, 2)
        subject.multiply(3, 4)
        subject.subtract(5, 6)
        subject.divide(7, 8)
        assert subject.list_history() == [3, 12, -1, 0.875]


class TestCohort():

    def test_add_students_then_list(self):
        subject = Cohort()
        subject.add_student(
            {'name': 'Gene', 'employer': 'Atlantis Digital'})
        subject.add_student(
            {'name': 'Petra', 'employer': 'Atlantis Digital'})
        subject.add_student(
            {'name': 'Jaspal', 'employer': 'Mercia Digital'})

        assert subject.list_students() == ([
            {'name': 'Gene', 'employer': 'Atlantis Digital'},
            {'name': 'Petra', 'employer': 'Atlantis Digital'},
            {'name': 'Jaspal', 'employer': 'Mercia Digital'}
        ])

    def test_list_employed_by(self):
        subject = Cohort()
        subject.add_student(
            {'name': 'Gene', 'employer': 'Atlantis Digital'})
        subject.add_student(
            {'name': 'Petra', 'employer': 'Atlantis Digital'})
        subject.add_student(
            {'name': 'Jaspal', 'employer': 'Mercia Digital'})

        assert subject.list_employed_by('Atlantis Digital') == [
            {'name': 'Gene', 'employer': 'Atlantis Digital'},
            {'name': 'Petra', 'employer': 'Atlantis Digital'}
        ]


class TestPerson():

    def test_get_work_address(self):
        subject = Person({
            'name': 'Jo',
            'pets': [
                {'name': 'Paulo', 'animal': 'cat'},
                {'name': 'Edith', 'animal': 'dog'},
                {'name': 'Pawel', 'animal': 'goldfish'}
            ],
            'addresses': [
                {'name': 'work', 'building': '12', 'street': 'Whitehall'},
                {'name': 'home', 'building': '1', 'street': 'North Lane'}
            ]
        })
        assert subject.get_work_address() == '12 Whitehall'

    def test_get_home_address(self):
        subject = Person({
            'name': 'Jo',
            'pets': [
                {'name': 'Paulo', 'animal': 'cat'},
                {'name': 'Edith', 'animal': 'dog'},
                {'name': 'Pawel', 'animal': 'goldfish'}
            ],
            'addresses': [
                {'name': 'work', 'building': '12', 'street': 'Whitehall'},
                {'name': 'home', 'building': '1', 'street': 'North Lane'}
            ]
        })
        assert subject.get_home_address() == '1 North Lane'

    def test_get_pets(self):
        subject = Person({
            'name': 'Jo',
            'pets': [
                {'name': 'Paulo', 'animal': 'cat'},
                {'name': 'Edith', 'animal': 'dog'},
                {'name': 'Pawel', 'animal': 'goldfish'}
            ],
            'addresses': [
                {'name': 'work', 'building': '12', 'street': 'Whitehall'},
                {'name': 'home', 'building': '1', 'street': 'North Lane'}
            ]
        })
        assert subject.get_pets(
        ) == "Jo has 3 pets: a cat called Paulo, a dog called Edith, a goldfish called Pawel"
