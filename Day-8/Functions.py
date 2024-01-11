#Working with functions
print("Greating Project!!")

name = input("Hello, tell me your name please: ")

def my_function():
    if name.endswith("a"):
        print(f"Hello Madame {name}")
    elif name.endswith("o"):
        print(f"Hello Sir {name}")
    else:
        print(f"Hello {name}, be welcome")
my_function()

def get_names(username):
    print(f"Greatings from {username}")

get_names(name)

def great_with_positions(secondname = "Devson", firstname = "Joao"):
    print(f"Hi, my Fist Name is {firstname} and Second is {secondname}")

great_with_positions()