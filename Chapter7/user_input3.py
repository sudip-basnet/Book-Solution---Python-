#7.9
sandwich_orders = ['cheese','pastrami','chicken','pastrami', 'buff','pastrami','pork']
finished_sandwich = []
print("We have run out of 'pastrami'.")

while sandwich_orders:
    order = sandwich_orders.pop()
    if order == 'pastrami':
        print("No 'pastrami' is left.")
        continue
    else:
        print(f"I made you {order} sandwich.")
        finished_sandwich.append(order)

for sandwich in finished_sandwich:
    print(sandwich)

#7.10

users ={}
active = True

while active:
    prompt = "Enter the name or type 'quit' to exit"
    name = input("Enter the name")
    if name == 'quit':
        break
    else:
        users[name] = input("Enter the name of place you would like to visit.")

for key,value in users.items():
    print(f"{key.title()} would like to visit {value.title()}.")

    
