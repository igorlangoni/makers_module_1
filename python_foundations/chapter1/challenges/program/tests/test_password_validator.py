from lib.password_validator import is_valid


# Authors: These tests are carefully ordered, please pay attention to the
# learner's experience when adding any new tests to this.
def test_whether_the_program_validates():
    assert is_valid("1234567") == False, "returns false when the password is less than 8 chars"
    assert is_valid("123456789") == False, "returns false when the password does not contain a special character"

    assert is_valid("567!") == False, "returns false when the password contains less than eight characters but includes '!'"
    assert is_valid("567@") == False, "returns false when the password contains less than eight characters but includes '@'"
    assert is_valid("567$") == False, "returns false when the password contains less than eight characters but includes '$'"
    assert is_valid("567&") == False, "returns false when the password contains less than eight characters but includes '&'"
    assert is_valid("567%") == False, "returns false when the password contains less than eight characters but includes '%'"
    assert is_valid("12!@$&%") == False, "returns false when the password is 7 chars but includes special characters"

    assert is_valid("12345678") == False, "returns false when the password does not contain any special characters"

    assert is_valid("1234567!") == True, "returns true when the password is 8 characters long and includes '!'"
    assert is_valid("123@4567") == True, "returns true when the password is 8 characters long and includes '@'"
    assert is_valid("$1234567") == True, "returns true when the password is 8 characters long and includes '$'"
    assert is_valid("123456%7") == True, "returns true when the password is 8 characters long and includes '%'"
    assert is_valid("1234&567") == True, "returns true when the password is 8 characters long and includes '&'"

    assert is_valid("!@$%&!@$") == True, "returns true with all special characters"
    assert is_valid("123456789!") == True, "returns true if special character is after 8th character"
    assert is_valid("1234567^") == False, "returns false if special character is not one of the five specified"
