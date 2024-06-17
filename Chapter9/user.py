class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f"User name : {self.first_name.title()} {self.last_name.title()}\nAge : {self.age}\nGender : {self.gender.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, nice to meet you!!!")