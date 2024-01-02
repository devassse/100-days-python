#Calculator of bills
print("Welcome to Tip Calculator\n")

totalBill = int(input("What was the Total bill? $"))
percentage = int(input("What percentage to Pay each one? (10, 12 or 15) "))
people = int(input("How many Peolple divide the bill? "))

#Give a Line space
print()

if percentage == 10:
    print("Paying 10%")
    payedBill = totalBill * 0.10 / people
    print(f"Each must pay ${round(payedBill, 2)}")
if percentage == 12:
    print("Paying 12%")
    payedBill = totalBill * 0.12 / people
    print(f"Each must pay ${round(payedBill, 2)}")
if percentage == 15:
    print("Paying 15%")
    payedBill = totalBill * 0.15 / people
    print(f"Each must pay ${round(payedBill, 2)}")