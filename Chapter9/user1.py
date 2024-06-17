from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(f"The privilages of admin are:")
        for work in self.privileges:
            print(work.title())


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()