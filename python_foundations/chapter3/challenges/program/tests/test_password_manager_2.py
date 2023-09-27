from lib.password_manager_2 import PasswordManager2


class TestPasswordManager2():

    def test_add_and_list_services(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')
        assert password_manager.list_services() == [
            'acebook', 'makersbnb'], 'added when the password and service name are unique'

    def test_add_of_invalid_password(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '123456789')
        password_manager.add('baidu', '!@$%&')
        assert password_manager.list_services() == [
            'acebook'], 'added only when the password is valid'

    def test_not_adding(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '$12345678')
        assert password_manager.list_services() == [
            'acebook'], 'not added when the password is not unique'

    def test_not_adding_not_unique(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.add('acebook', '@12345678')
        assert password_manager.list_services() == [
            'acebook'], 'not added when the service name is not unique'

    def test_remove(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.remove('acebook')
        assert password_manager.list_services() == [], "removes a service"

    def test_update(self):
        password_manager = PasswordManager2()
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')
        password_manager.update('acebook', '!12345678')
        assert password_manager.get_for_service(
            'acebook') == '!12345678', 'updates when password is unique'

    def test_update_not_unique(self):
        password_manager = PasswordManager2()
        password_manager.add('willslazeremporium', '$12345678')
        password_manager.add('metalfistrecords', '@12345678')
        password_manager.update('willslazeremporium', '@12345678')
        assert password_manager.get_for_service(
            'willslazeremporium') == '$12345678', 'does not update when password is not unique'

    def test_update_of_invalid_password(self):
        password_manager = PasswordManager2()
        password_manager.add('willslazeremporium', '$12345678')
        password_manager.add('metalfistrecords', '@12345678')
        password_manager.update('willslazeremporium', '12345')
        assert password_manager.get_for_service(
            'willslazeremporium') == '$12345678', 'updated only when password is valid'

    def test_get_for_service_returns_none(self):
        password_manager = PasswordManager2()
        assert password_manager.get_for_service("acebook") == None

    def test_sort_by_alphabetically(self):
        password_manager = PasswordManager2()
        password_manager.add('baidu', '%12345678')
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')
        assert password_manager.sort_services_by('service') == [
            'acebook',
            'baidu',
            'makersbnb'
        ]

    def test_sort_reverse_alphabetically(self):
        password_manager = PasswordManager2()
        password_manager.add('baidu', '%12345678')
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')
        assert password_manager.sort_services_by('service', 'reverse') == [
            'makersbnb',
            'baidu',
            'acebook'
        ]

    def test_sort_chronologically(self):
        password_manager = PasswordManager2()
        password_manager.add('baidu', '%12345678')
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')

        assert password_manager.sort_services_by('added_on') == [
            'baidu',
            'acebook',
            'makersbnb',
        ]

    def test_sort_reverse_chronologically(self):
        password_manager = PasswordManager2()
        password_manager.add('baidu', '%12345678')
        password_manager.add('acebook', '$12345678')
        password_manager.add('makersbnb', '@12345678')

        assert password_manager.sort_services_by('added_on', 'reverse') == [
            'makersbnb',
            'acebook',
            'baidu'
        ]
