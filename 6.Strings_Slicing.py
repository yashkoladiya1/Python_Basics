"""
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string
"""

b = "Hello, World!"
print("B-----",b[2:5])

#Slice From the Start
#By leaving out the start index, the range will start at the first character:

c = "Hello, World!"
print("C----",c[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:

a = "Hello, World!"
print("a---",a[2:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:

g = "Hello, World!"
print("g----",g[-5:-2])
