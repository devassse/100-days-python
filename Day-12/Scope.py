#Namespacings - Global VS Local

name = "Joao"

def namings():
    name = "Devson"
    print(name)

namings()
print(name)

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)


i = 50
def foo():
    i = 100
    return i
 
foo()
print(i + foo())