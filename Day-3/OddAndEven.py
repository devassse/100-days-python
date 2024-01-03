#Check if Number is ODD or EVEN

#Receive a number from Console and convert it to INTEGER
number = int(input("Please inform the NUMBER: "))

#Verify ODD or EVEN
if number % 2 == 0:
    print(f"The Number {number} is ODD")
else:
    print(f"The Number {number} is EVEN")