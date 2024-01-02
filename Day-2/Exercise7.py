#Calcute Left Weeks of Life

lifeLimit = 90
weeksOfTheYear = 52
lifelimitInWeeks = lifeLimit * weeksOfTheYear

print(f"Lifetime Calculator\nWe All spected to live {lifeLimit} Years or {lifelimitInWeeks} Weeks")

age = int(input("Tell me your age: "))

remainingLife = lifeLimit - age
remainingLifeInWeeks = remainingLife * weeksOfTheYear

print(f"You are about to live more {remainingLife} years, witch are {remainingLifeInWeeks} Weeks.")
