from lib.password_manager import PasswordManager


class TestPasswordManager():

    def test_initialize(self):
        subject = PasswordManager()
        assert isinstance(subject, PasswordManager)

    def test_add_and_get_valid_passwords(self):
        subject = PasswordManager()
        subject.add('aceplay', '12345678!')
        subject.add("willslazerpalace", "12345678@")
        subject.add("makerbnb", "12345$678")
        subject.add("discgolfuk", "12345678%")
        subject.add("deathmetalforcats", "12345678&")

        assert subject.get_for_service('aceplay') == '12345678!'
        assert subject.get_for_service('willslazerpalace') == '12345678@'
        assert subject.get_for_service('makerbnb') == '12345$678'
        assert subject.get_for_service('discgolfuk') == '12345678%'
        assert subject.get_for_service('deathmetalforcats') == '12345678&'

    def test_list_services_with_valid_passwords(self):
        subject = PasswordManager()
        subject.add('aceplay', '12345678!')
        subject.add("willslazerpalace", "12345678@")
        subject.add("makerbnb", "12345$678")
        subject.add("discgolfuk", "12345678%")
        subject.add("deathmetalforcats", "12345678&")
        assert list(subject.list_services()) == [
            'aceplay', 'willslazerpalace', 'makerbnb', 'discgolfuk', 'deathmetalforcats']

    def test_ignores_invalid_paswords(self):
        subject = PasswordManager()
        subject.add('service_1', '1234567')
        assert list(subject.list_services()) == []
        assert subject.get_for_service('service_1') == None
        subject.add('service_2', '1234567!')
        assert list(subject.list_services()) == ['service_2']
        assert subject.get_for_service('service_2') == '1234567!'
        subject.add('service_3', '12345678')
        subject.add('service_4', '!@$%&')
        assert list(subject.list_services()) == ['service_2']
