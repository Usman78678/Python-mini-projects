weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))  

bmi = weight / height ** 2


if bmi < 18.5:
    print("underweight", bmi)
elif bmi < 25:
    print ("normal weight", bmi)
else:
    print ("overweight", bmi)
