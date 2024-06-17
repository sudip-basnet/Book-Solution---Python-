from random import randint,choice

class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def set_sides(self,value):
        self.sides = value

    def roll_die(self):
        print(randint(1,self.sides))
    
die = Die()
#rolling a 6 sided die 10 times
for i in range(0,21,10):
    if i>1:
        die.set_sides(i)
        for j in range(0,10):
            die.roll_die()
    else:
        for j in range(0,10):
            die.roll_die()


numbers = [5,'a',10,'b',30,'h',34,98,'f',49,'j']
my_numbers = [10,'f']
num =0
print("Any ticket matching these four numbers or letters wins a prize.")
for i in range(0,5):
    num+=1
    character=choice(numbers)
    if character in my_numbers:
        print(f"I have finally won in {num} attempts.")
        break
    else:
        print(character)
    
