import time


class User:
    def __init__(self, name, password):
        if not name:
            raise ValueError('missing name')
        if not password:
            raise ValueError('missing password')
        self.name = name
        self.password = password


    def __str__(self):
        return f"user name is {self.name}"

    def timer(self, time):
        if not time:
            raise ValueError('invalid time')
        return self.time = time

name = input('the name ')
password = input('password ')
try:
    user = User(name, password)
except ValueError:
    print('you missed an input')
else:
    print(user)

    now = time.time()
    in_time = user.timer(now)
    print(in_time)

