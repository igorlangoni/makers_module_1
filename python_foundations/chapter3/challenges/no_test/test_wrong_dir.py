# Displays a message when learners run the tests in the wrong place

import pytest

MESSAGE = """
    You are running `pytest` in the wrong directory.
    If you are trying to run the drills tests, do this:
    ; cd drills
    ; pipenv run pytest -x
    If you are trying to run the program tests, do this:
    ; cd program
    ; pipenv run pytest -x
"""


def test_wrong_dir():
    pytest.fail(MESSAGE)

