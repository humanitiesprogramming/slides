# let's annotate some code together.


class User:
    def __init__(self, some_name="anonymous", some_email="none"):
        self.name = some_name
        self.email = some_email

    def display_name(self):
        print(self.name)

    def display_email(self):
        print(self.email)

    def change_email(self, new_email):
        self.email = new_email

    def change_name(self, new_name):
        self.name = new_name


brandon = User("brandon", "bmw9t@virginia.edu")

brandon.display_name()

brandon.display_email()

brandon.change_email("echreed@gmail.com")

brandon.display_email()

brandon.change_name("Ethan 'Boss Man' Reed")

brandon.display_name()
