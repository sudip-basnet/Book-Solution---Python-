file_name = 'C:\\V\\Python Crash Course\\Chapter10\\python.txt'
with open(file_name) as file_obj:
    contents = file_obj.read()
    for line in file_obj:
        line.replace('python','C')
        print(line.rstrip())
    lines = file_obj.readlines()
print(contents)
print(lines)
#all of the file read operation doesn't work all at once because during the first read the file read pointer goes to the last of the line and it has empty thing to read.
contents.replace('python','C')
print(contents)

#I don't know why the replace method is not working???