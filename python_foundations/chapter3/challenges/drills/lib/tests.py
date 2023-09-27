
class PasswordManager2():
    def __init__(self):
        self.password_list = []
        self.pwd = {}

    def add(self, service, password):
        if password_validator(password):
            self.service = service
            self.password = password
            self.pwd[self.service] = [self.password]
            self.password_list.append(self.pwd) 
    
    def remove(self, service):
        removed = next(filter(lambda pwd: self.pwd['service'] == service, self.password_list))
    


def is_long_enough(password):
    return len(password) > 7

def are_there_special_char(password):
    counter = 0
    spec_char = ['!', '@', '$', '%', '&']
    ind = 0
    for pwd in password:
        if pwd in spec_char:
            counter += 1
        ind += 1
    return counter > 0

def password_validator(password):
    return is_long_enough(password) and are_there_special_char(password)
