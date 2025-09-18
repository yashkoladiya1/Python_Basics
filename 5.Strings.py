"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
"""

#Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("Multiline Strings-",a)


#Strings are Arrays

c = "YASH"
print("string array-",c[1])

#Looping Through a String
for i in c:
    print("loop-",i)

#String Length

sw = "Hello, World!"
print(len(sw))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Check if NOT
txt2 = "The best things in life are free!"
print("expensive" not in txt2)