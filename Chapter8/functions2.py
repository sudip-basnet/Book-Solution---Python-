#8.3
def make_shirt1(size,message):
    print(f"{message} is printed on the tshirt of size {size}.")

make_shirt1('L','Sudip')
make_shirt1(message='Sudip',size='L')

#8.4
def make_shirt2(size='L',message='I love Python'):
    print(f"{message} is printed on the tshirt of size {size}.")

make_shirt2()

def make_shirt3(size,message='I love programming'):
    print(f"{message} is printed on the tshirt of size {size}.")

make_shirt3('M')

def describe_city(city,country='Nepal'):
    print(f"{city.title()} is in {country.title()}.")

city=input("Enter the city name.")
country=input("Enter the country name.")
describe_city(city,country)
describe_city(city)






