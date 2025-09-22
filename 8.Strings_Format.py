"""
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
GIVES ERROR
"""

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Escape Character

txtt = "We are the so-called \"Vikings\" from the north."
print(txtt)