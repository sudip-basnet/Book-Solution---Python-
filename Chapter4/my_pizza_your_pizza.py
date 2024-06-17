#4.11
pizzas = ['cheese', 'pepperoni', 'veggie']
friend_pizzas = pizzas[:]

pizzas.append('meat')
friend_pizzas.append('hawaiin')

print("My favourite pizzas are")
for i in pizzas:
    print(i)

print("My friend's favourite pizzas are")
for i in friend_pizzas:
    print(i)