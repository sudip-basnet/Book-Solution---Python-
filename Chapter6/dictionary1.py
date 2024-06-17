#6.1
details = {'first_name':'Albert','last_name':'Einstien','age':57, 'city':'Berlin'}
print(details['first_name'])
print(details['last_name'])
print(details['age'])
print(details['city'])

#6.2
favourite_numbers = {'Aashish':4,'Rohan':7,'Saugat':57,'Sudip':9}
for person in favourite_numbers:
    print(f"The favourite number of {person} is {favourite_numbers[person]}")

#6.3
words = {'list':'a collection of items in an order.',
         'if-else':'a conditional statement.',
         'for-loop':'a loop statement to perform repetitive tasks.',
         'del':'deleting an item from a list.',
         'append':'adding an item to a list.',
         'variable':'an entity whose value can change during the execution of the program.'
        }
#6.4
for word,meaning in words.items():
    print(f"The meaning of {word} is {meaning}\n ")   

#6.5
rivers ={'nile':'egypt','bagmati':'nepal','ganga':'india'}  
for river in rivers:
    print(f"The {river.title()} lies in {rivers[river].title()}")
    print(f"The name of rivers are {river.title()}")

for river in rivers.keys():
    print(river.title())

for river in rivers.values():
    print(river.title())
