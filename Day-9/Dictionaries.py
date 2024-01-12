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