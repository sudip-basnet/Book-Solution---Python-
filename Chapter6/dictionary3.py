#6.7
person1= {'first_name':'Albert','last_name':'Einstien','age':57, 'city':'Berlin'}
person2 = {'first_name':'Isaac','last_name':'Newton','age':92, 'city':'London'}
person3 = {'first_name':'Stephan','last_name':'Hawking','age':47, 'city':'New York'}

people =[person1, person2, person3]

for person in people:
    for man in person.values():
        print(man)

#6.8
pet1 = {'kind':'dog','owner':'rahul'}
pet2 = {'kind':'cat','owner':'rohan'}
pet3 = {'kind':'hare','owner':'sunil'}
pet4 = {'kind':'parrot','owner':'rusana'}

pets = [pet1,pet2,pet3,pet4]

for animal in pets:
        print(f"Pet : {animal['kind']} = Owner : {animal['owner']}")
#6.9

favorite_places = {'mohan':['hyderabad','kohalpur'],'sneha':['kathmandu','bhaktapur'],'sohan':['Dhankuta','Darchula']}

for name, places in favorite_places.items():
     print(f"Name: {name.title()}\nFavorite Places:") 
     for place in places:
          print(place) 


