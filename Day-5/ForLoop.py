#Loops

fruits = ["Apple", "Strawberry", "Mango", "Pineapple"]

for f in fruits:
    print("My Favorite", f)


#Avarage Height
students_height = [1.43, 2.10, 1.87, 1.67, 1.55]
sum = 0
avg = 0
for height in students_height:
    sum += height

print(f"All Summed Heights: {sum}")

avg = sum/len(students_height)

print(f"And the AVG is {avg}")


