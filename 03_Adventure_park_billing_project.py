print("Welcome to Adventure Island")
height = int(input("Enter your height in CM:"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("you need to pay $",bill)
    elif age <=18:
        bill = 7
        print("You need to pay $",bill)
    elif age <= 55 and age >=45:
        bill = 0
        print("you dont need to pay anything, your ticket is free")
    else:
        bill = 12
        print("you need to pay $",bill)
    photo = input("do you want to add a photo ride? type y for yes type n for no: ")
    if photo == "y" or photo == "Y" or photo == "yes" or photo == "YES":
        bill = bill + 3
        print(f"your total bill is ${bill}")
    else:
        print(f"your total bill is ${bill}")
else:
    print("you cannot ride the roller coaster")    
