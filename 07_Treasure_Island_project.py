import pyttsx3 # pip install pyttsx3
engine = pyttsx3.init() # object creation

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
gate1 = input("your are at the mid of the island. there is a jungle ahead of you.\nwhere do you want to go?\ntype 'left' or 'right' ")
if gate1 == "left":
    print("congratulations! you have reached the lake.")

    gate2 = input("there is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across. ")
    if gate2 == "wait":
        print("Congratulations! you have reached the island safely." )
        gate3 = input("there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose? ")
        if gate3 == "yellow":
            print("congratulations! you found the treasure! you win!")
        elif gate3 == "red":
            print("it's a room full of fire. Game Over.")
        elif gate3 == "blue":
            print("you enter a room of beasts. Game Over.")
        else:
            print("you chose a door that doesn't exist. Game Over.")
    elif gate2 == "swim":
        print("you were attacked by an angry crocodile. Game Over.")
elif gate1 == "right":
    print("you fell into a hole. Game Over.")
else:
    print ("you chose a door that doesn't exist. Game Over.")
    

