"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""



#Creating Variables

age = 22
name = "Yash"
is_student = True
height = 5.10

print("age-",age)
print("name-",name)
print("Is student-",is_student)
print("height-",height)

# Casting
y = float(age)
q = int(height)

print("age after casting-",y)
print("height after casting-",q)

# Get the Type

print(type(age))
print(type(name))
print(type(is_student))
print(type(height))