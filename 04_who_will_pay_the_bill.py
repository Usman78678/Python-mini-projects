import random
friends = ["Affan Saifi", "Hamza Malik", "Usman Abdullah", "Saif Ali", "Farhan"]
bill = random.randint(0, 4)
if bill == 1:
    print(friends[0])
elif bill == 2:
    print(friends[1])
elif bill == 3:
    print(friends[2])
elif bill == 4:
    print(friends[3])
else:
    print(friends[4])

    #or
print(random.choice(friends))

#or
print(friends[bill])