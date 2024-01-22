#Documenting the Code

"""Take a first and Last name and format it"""
def format_names(f_name, l_name):
    return f"Your name correctly spelled is {f_name.title()} {l_name.title()}"

first_name = input("Insert your first Name: ")
last_name = input("Insert your last Name: ")

print(format_names(first_name, last_name))