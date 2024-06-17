#9.6
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name):
        super().__init__(restaurant_name, cuisine_name)
        self.flavor = ['Vanilla','Chocolate','Strawberry']

    def icecream_flavor(self):
        print(f"The flavor of icecream is {self.flavor}.")

icecream = IceCreamStand('Himalayan Cafe','Burger')
icecream.icecream_flavor()
print(icecream.restaurant_name)
print(icecream.cuisine_name)

#9.7
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

#9.8
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


admin = Admin('sudip','basnet',20,'male')
admin.privileges.show_privileges()

#9.9
class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_reading(self):
        print(f"{self.make} {self.model} {self.year}")

    def read_odometer(self):
        print(f"This car had the odometer reading of {self.odometer}")

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You cannot roll back odometer.")

    def increment_odometer(self,value):
        self.odometer+=value

class Battery():
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The size of battery is {self.battery_size}.")

    def get_range (self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} in full capacity.")

    def upgrade_battery (self):
        if self.battery_size < 100:
            self.battery_size = 100

class Electric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

electric = Electric('Tesle','X',2020)
electric.battery.get_range()
electric.battery.upgrade_battery()
electric.battery.get_range()
