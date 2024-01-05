#Generate Safer Password
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))


password = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
    # print(random_char)

for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
    # print(random_number)

for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
    # print(random_number)

#Eazy Level
print(f"Your EASY Mode Password is {password}")

#Hard Level
hard_password = ''.join(random.sample(password,len(password)))
print(f"The hard level is {hard_password}")