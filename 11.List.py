"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

"""

thislist = ["apple", "banana", "cherry"]
print("List---->",thislist)

#  Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 

# Allow Duplicates 
# Since lists are indexed, lists can have items with the same value:

thislist2 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist2)
print("Length---->",len(thislist2))

# Access Items
#List items are indexed and you can access them by referring to the index number:

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("access items---->",thislist3[2:5])


#Change Item Value
thislist4 = ["apple", "banana", "cherry"]
thislist4[1] = "blackcurrant"
print("Change the values---->",thislist4)

#Insert Items
thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(2, "watermelon")
print("Insert---->",thislist5)

#Append Items
thislist6 = ["apple", "banana", "cherry"]
thislist6.append("orange")
print("Append--->",thislist6)

#Extend List
thislist7 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist7.extend(tropical)
print("extend--->",thislist7)

#Remove Specified Item
thislist8 = ["apple", "banana", "cherry"]
thislist8.remove("banana")
print("Remove--->",thislist8)
#If there are more than one item with the specified value, the remove() method removes the first occurrence:

#Remove Specified Index
#The pop() method removes the specified index.
thislist9 = ["apple", "banana", "cherry"]
thislist9.pop(1)
print("Pop--->",thislist9)

#The del keyword also removes the specified index:
thislist10 = ["apple", "banana", "cherry"]
del thislist10[0]
print("del--->",thislist10)

#The clear() method empties the list.
thislist11 = ["apple", "banana", "cherry"]
thislist11.clear()
print("clear--->",thislist11)

#Loop Through a List

looplist12 = ["apple", "banana", "cherry"]
for x in looplist12:
  print(x)

#Using a While Loop
thislist13 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist13):
  print(thislist13[i])
  i = i + 1

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#The Syntax
#newlist = [expression for item in iterable if condition == True]

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits2 if x != "banana"]
print("newlist--->",newlist2)

#Python sort lists
thislist14 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist14.sort()
print(thislist14)

#Sort Descending

thislist15 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist15.sort(reverse = True)
print(thislist15)

#Use the copy() method

copylist = ["apple", "banana", "cherry"]
newcopy = copylist.copy()
print(newcopy)

#Join Two Lists
list30 = ["a", "b", "c"]
list31 = [1, 2, 3]

list33 = list30 + list31
print(list33)