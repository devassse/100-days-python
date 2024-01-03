#Find if a YEAR is LEAP or NOT

#Receive a Year from User
year = int(input("Tell me the Year you want: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yes it is LEAP Year")
        else:
            print("Not a LEAP Year")
    else:
        print(f"Yes it is a LEAP Year")
else:
    print("This is not a LEAP Year")

