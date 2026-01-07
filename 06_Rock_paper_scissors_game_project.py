import random
choice = int(input("What do you want to choose? type 0 for rock 1 for paper 2 for scissors:\n"))
paper = """Paper\n    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
Rock = """Rock\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
Scissors = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_Image = [Rock,paper, Scissors]
if choice <=2 and choice >= 0:
    print(game_Image[choice])
game = random.randint(0,2)
if choice == 0 and game == 0:
    print("""\nComputer Chose\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\nDraw""")
elif choice == 0 and game == 1:
    print("""Computer Chose\n    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\nyou lose""")
elif choice == 0 and game ==2:
    print("""Computer Chose\n    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\nyou Win""")
elif choice == 1 and game == 0:
    print("""Computer Chose\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\nYou Win""")
elif choice == 1 and game == 1:
    print("""Computer Chose\n    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\nDraw""")
elif choice == 1 and game == 2:
    print ("""Computer Chose\n    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\nYou Lose""") 
elif choice == 2 and game == 0:
    print("""Computer Chose\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\nYou Lose""")
elif choice == 2 and game == 1:
    print("""Computer Chose\n    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\nYou Win""")
elif choice == 2 and game == 2:
    print("""Computer Chose\n    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\nDraw""")
else:
    print("Please Enter correct input")
