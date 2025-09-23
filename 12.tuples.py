"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Unchangeable

#Tuple Length
print("length---->",len(thistuple))

#Create Tuple With One Item
thistuple2 = ("apple",)
print(type(thistuple2))

#Access Tuple Items
thistuple3 = ("apple", "banana", "cherry")
print("Access Tuple--->",thistuple3[1])

#Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)

print("change the value----->",x)

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)

#Loop Tuples
thistuple3 = ("apple", "banana", "cherry")
for x in thistuple3:
  print(x)

#Loop Through the Index Numbers
thistuple4 = ("apple", "banana", "cherry")
for i in range(len(thistuple4)):
  print(thistuple4[i])

#Using a While Loop
thistuple5 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple5):
  print(thistuple5[i])
  i = i + 1

#Join Two Tuples
tuple6 = ("a", "b" , "c")
tuple7 = (1, 2, 3)

tuple8 = tuple6+ tuple7
print(tuple8)