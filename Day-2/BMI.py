#Calculate BMI

import math


print("BMI Calculator\n")
weight = float(input("Insert your Weight (kg): "))
height = float(input("Insert your Height (m): "))

bmi = weight / height**2

print()
print("Your BMI is ", int(bmi))