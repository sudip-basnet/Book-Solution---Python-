#7.4
active = True
print("Enter pizza topppings\n")
while active :
    message = input()
    if message == 'quit':
        active = False
    else:
        print("You will add that topping to the pizza")

#7.6
active = True
while active:
    age = int(input("Enter the age"))
    if age <3:
        print("The price is free.")
    elif age >=3 and age <=12:
        print("The price is $10.")
    elif age >12 :
        print("The price is $15.")
    else:
        exit