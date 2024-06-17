#9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
    
    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name} and the cuisine name is {self.cuisine_name}.")

    def open_restaurant(self):
        print("The restaurant is open.")
    
restaurant1 = Restaurant('Himalayan Corner','Momo')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_name)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#9.2
restaurant2 = Restaurant('Sherpas Restro','Burger')
restaurant3 = Restaurant('Kalinchowk Cafe','Pizza')
restaurant4 = Restaurant('Sumnima Store','Chowmein')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

#9.3

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

user = User('sudip','basnet',20,'male')
user.describe_user()
user.greet_user()