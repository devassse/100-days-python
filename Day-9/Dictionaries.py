#Working with Dictionaries

person = {
    "name": "Joao Devson",
    "birthdate": "09/06/1992"
}

print(person["name"])

person["sirname"] = "Mucavel"

print(person)

#Loop 
for key in person:
    print(person[key])


#Nested Dictionaries and Dictionares

travel_log = {
    "France": {
        "visited_cities": ["Paris", "Dujon"],
        "food": ["Melon","Guis"],
        "spaces": {
             "pleasure"   
        }
    }
}


start_dictionary = {
    "a":2,
    "b":3
}
start_dictionary[3] = 7
final_dictionary = start_dictionary

print(start_dictionary)