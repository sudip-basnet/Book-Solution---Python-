file_name ='cats.txt'
#file_name ='dog.txt'

try:
    with open(file_name,'r') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file doesn't exist!!!")
    pass
else:
    #makes the seperate list of the words in the file
    words = contents.split()
    print(words)
    print(len(words))
    print(contents)
    