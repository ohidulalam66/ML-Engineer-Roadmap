# Introduction ro Stings 

a = "Hello"
b = "Ohid"
c = '''Yo are so 
genius'''

print(a)
print(b)
print(c)

# Concatination and Repetition

name = "Mohammad Ohidul "
surename = "Alam"

print(name + surename)

# Methods
# strip()- removes spaces from begining to end
text = "      Python is easy to learn, powerful to use, and one of the most popular programming languages for software development.      "

cleaned_text = text.strip()
print(cleaned_text)

# replace(old, new) - Replace part of strings
text = "Python is Easy"
new_text = text.replace("Easy", "Awesome")
print(new_text)

# split(delimiter) - splits strings into list
text = "MLops, Docker, RAG"
tools = text.split(",")
print(tools)

# join(iterable) - joins list elements into a string
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)

# upper(), lower() convert case
word = "Python"
print("UpperCase: ", word.upper())
print("LowerrCase: ", word.lower())

# title(), Capitalize() - capitalization
text1 = "python is powerfull language."
print(text1.title())
print(text1.capitalize())

# find() not found = -1, index() not found = error

text2 = "python is powerfull language."
print(text2.find("is"))
print(text2.find("java")) # => -1
print(text2.index("powerfull"))
print(text2.index("java")) # => error

# Count()
fruit = "Apple"
print(fruit.count("p"))

# startswith() and endswith() - Check string Prefix and Suffix
text3 = "Hello wolrd, Python"
print(text3.startswith("Hello"))
print(text3.endswith("Python"))


# String Indexing and slicing slice syntex : s[start:end step]
s = "Python is Fun"
print(s[5])
print(s[-1])
print(s[0 : 6]) # end point +1 count or s[ : 6] or s[0 : ]
print(s[:: 2]) # middle one word gap

# String formatting techniques
language = input("Enter a favourite language: ")
print(f"I love {language} language.")

# Advance string manipulation ASCII value: ord(), chr()

print(ord("@"))
print(chr(67))

# Lambda use
flowers = ["rose", "tulip", "jasmine", "sunflower"]
capitalized = list(map (lambda flower : flower.capitalize(), flowers))
print(capitalized)

# Reverse string or Palindrome

name = "Ohid"
print(name[:: -1])
words = input("Enter a word: ")
if words == words[:: -1]:
    print("It is Palindrome.")
else:
    print("It is not palindrome.")

# animate String

import sys
import time

animate_sentence = "Python is magic."

for char in animate_sentence:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

# strong Password Check

while True:
    password = input("Enter a Password: ")

    length_password = len(password) >= 8
    upper_case = any(char.isupper() for char in password)
    digit_case = any(char.isdigit() for char in password)
    special_case = any(char in "/@*$%#" for char in password)

    if length_password and upper_case and digit_case and special_case:
        print("Strong Pasword.")
        break
    elif length_password and (upper_case or digit_case or special_case):
        print("Moderate Password.")
    else:
        print("Weak Password.")
