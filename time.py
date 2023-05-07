class User:
    def __init__(self, name, password):
        if not name:
            raise ValueError('missing name')
        self.name = name
        self.password = password


    def __str__(self):
        return f"user name is {self.name}


name = input('the name ')
password = input('password ')
user = User(name, password)
