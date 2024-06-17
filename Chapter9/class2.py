#9.4
class Restaurant:
    def __init__(self,restaurant_name,cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name} and the cuisine name is {self.cuisine_name}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,inc):
        self.number_served += inc

restraurant = Restaurant('Hotel Himalayan','Momo')
print(restraurant.number_served)

restraurant.set_number_served(40)
print(restraurant.number_served)

restraurant.increment_number_served(5)
print(restraurant.number_served)

#9.5

class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User name : {self.first_name.title()} {self.last_name.title()}\nAge : {self.age}\nGender : {self.gender.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}, nice to meet you!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('sudip','basnet',20,'male')
print(user.login_attempts)

user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
        
