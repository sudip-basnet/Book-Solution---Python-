#3.10
items =['nepal','sagarmatha','lumbini','bagmati','kathmandu','newari','rajesh Hamal']

print(items)
print(items[2].title())

items[1]='Manaslu'
print(items)

items.append('Nischal')
items.insert(2,'Kaji')
print(items)

del items[2]

popped = items.pop()
print(f"Popped item is {popped}.\n")
popped = items.pop(0)
print(f"The first item is {popped}.\n")
items.remove('bagmati')
print(items)
print(sorted(items))
print(sorted(items, reverse= True))

items.reverse()
print(items)

items.reverse()
print(items)

items.sort()
print(items)

items.sort(reverse = True)
print(items)

number = len(items)
print(items)
print(f"The number of elements in the list is {number}.\nThankyou!")