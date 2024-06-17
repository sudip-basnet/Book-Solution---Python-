while True:
    m=input("Enter the first number.")
    if m=='q':
        break
    n=input("Enter the second number.")
    if n == 'q':
        break
    try:
        a = int(m)
        b = int(n)
    except ValueError:
        print("Only numbers can be added!!!")
    else:
        print(f"The sum is {a+b}.")