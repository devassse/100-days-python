#Prime Number
#is the Number that can be DEVIDE by ITSELF or by ONE only

print("Prime Number Finder!")
n = int(input("Please inform the Number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Yes, it is a Prime Number!")
    else:
        print("It is not a Prime Number")


prime_checker(number = n)