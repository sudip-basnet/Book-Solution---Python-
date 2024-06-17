favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people = ['jacob','phil','rohan','jen','sujan','sarah','edward']

for person in people:
    if person in favorite_languages:
        print(f"Thanks {person.title()} for responding...")
    else :
        print(f"Hey {person.title()}, I would like to invite you for the poll....")