#Pizza Delivery System

print("Welcome to your Pizza House Kichen")
pizza_size = input("What size of Pizza do you Want? S, M or L? ").upper()

bill = 0
if pizza_size:
    if pizza_size == 'S':
        bill = 5
        print(f"Pay Small Pizza bill of ${bill}")
    elif pizza_size == "M":
        bill = 7
        print(f"Pay Medium Pizza bill of ${bill}")
    elif pizza_size == "L":
        bill = 12
        print(f"Pay Large Pizza bill of ${bill}")
    else:
        print("Wrong option Selected")

    delivery = input("Do you wanna Delivery? pay extra $2 (Y or N): ").upper()
    if delivery == "Y":
        bill += 2

    print(f"You Total bill is ${bill}")
else:
    print("Please select Valide Option")


    