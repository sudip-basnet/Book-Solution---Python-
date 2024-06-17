#3.4
people = ['Adam','Harry','Sudip']
print(f"Hello {people[0]}, You are invited.")
print(f"Hello {people[1]}, You are invited.")
print(f"Hello {people[2]}, You are invited.")

#3.5
print(f"\n{people[1]} won't be able to come.\n")

people[1] = 'Roshan'
print(f"Hello {people[0]}, You are invited.")
print(f"Hello {people[1]}, You are invited.")
print(f"Hello {people[2]}, You are invited.")

#3.6
people.insert(0,'Rohan')
people.insert(2,'Subash')
people.append('Rishikesh')

print(f"\nHello {people[0]}, You are invited.")
print(f"Hello {people[1]}, You are invited.")
print(f"Hello {people[2]}, You are invited.")
print(f"Hello {people[3]}, You are invited.")
print(f"Hello {people[4]}, You are invited.")
print(f"Hello {people[5]}, You are invited.")

print("\n I can only invite two people for dinner.\n")

#3.7
removed_person = people.pop()
print(f"Sorry {removed_person}, you are not invited.\n")
removed_person = people.pop()
print(f"Sorry {removed_person}, you are not invited.\n")
removed_person = people.pop()
print(f"Sorry {removed_person}, you are not invited.\n")
removed_person = people.pop()
print(f"Sorry {removed_person}, you are not invited.\n")

print(f"{people[0]} and {people[1]}, you two are still invited.\n")

#3.9
number = len(people)
print(f"{number} people are invited.")

del people[0]
del people[0]

print(people)





