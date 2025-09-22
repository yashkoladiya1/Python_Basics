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
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("clear--->",thislist)

#Loop Through a List

looplist = ["apple", "banana", "cherry"]
for x in looplist:
  print(x)

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1