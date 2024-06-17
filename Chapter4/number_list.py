#4.3
for value in range(1,21):
    print(value) 

#4.4 and 4.5
one_million = list(range(1,1000000))
print(one_million)
print(min(one_million))
print(max(one_million))
print(sum(one_million))

#4.6
odd_numbers = []
for i in range(1,20,2):
    odd_numbers.append(i)
for i in odd_numbers:
    print(i)

#4.7
three_multiple = list(range(3,31,3))
for i in three_multiple:
    print(i)

#4.8
cube = [value**3 for value in range(1,11)]
for value in cube:
    print(value)

#4.9
print(cube)