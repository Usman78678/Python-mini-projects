# Pizza Bill Calculator
# This program calculates the total bill for a pizza order based on size and additional toppings.
# Prompt the user for pizza size and toppings, then compute the final bill.


print("hello i am pizza bill calculator")
size = (input("what size you want S, M, L: "))
papperoni = input("do you want pepperoni Y or N: ")
cheese = input("do you want extra cheese Y or N: ")
bill = 0
if size == "s" or size == "S": 
    bill += 15
elif size == "m" or size == "M":
    bill += 20 
elif size == "l" or size == "L":
    bill += 25
else:
     print ("please choose the correct option")
    
if papperoni == "Y" or papperoni == "y":
    if size == "s" or size == "S":
        bill += 2
    elif size == "m" or size == "l":
        bill += 3
elif papperoni == "N" or papperoni == "n":
    bill = bill
else :
    print("Please choose the correct option")

if cheese == "y":
    if size == "s" or size == "m" or size == "l":
        bill += 1
        print(f"this is your bill ${bill} sir")
elif cheese == "n":
    bill = bill
    print(f"Here is your {bill} sir")
else:
    print ("Please choose the correct option")
    



