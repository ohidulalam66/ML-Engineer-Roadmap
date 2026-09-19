# Arithmetic Operators
x = 10
y = 3

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y) # floor divsion
# print(x % y)
# print(x ** y)

# Assignment Operators

m = 10 # 10
m += 5 # 15
m -= 5 # 10
m *= 3 # 30
m /= 3 # 10
# print(m)

# Comparison (Relational) Operators
p = 7
q = 8

# print(p > q)
# print(p < q)
# print(p == q)
# print(p != q)
# print(p >= q)
# print(p <= q)

# logical Operators
s = True
t = False

# and
# print(s and t)

# or
# print(s or t)

# not
# print(not t)

# Membership Operators

list = [1, 3, 6, 9, 12, 15]

# print(10 in list) # in

# print(0 not in list) # not in

# Identity Operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Check if two variables point to the list
# print(a is c)

# Check if two variables do not  point to the list
# print(a  is not b)

# Even though a and b ave same content, they are differnt objects
# print(a == b)
# print(a is b)

# sow an image in browser using webbroswer

# import webbrowser

# webbrowser.open("https://www.youtube.com/shorts/EJR3TlSUOV8")
# webbrowser.open("D:\ML Engineer Roadmap\Python(AI_ML)\icons\python.png")

# Text to speech  
# import pyttsx3
# engine = pyttsx3.init()

# engine.say("If you tell me whether you want normal Python auto complete or AI" \
# " generation like Copilot, I can give you the exact VS Code setup.")
# engine.runAndWait()


# Q1 Check if number is between 10 to 50

# num = int(input("Enter a Number: "))

# if num >= 10 and 50 >= num:
#     print("This number is between 10 to 50.")
# else:
#     print("This number don't exsits between 10 to 50.")


# Q2 Compare two number

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter sec Number: "))

print(f"Is {num1} gater then {num2}: ", num1 > num2)
print(f"Are they equal: ", num1 == num2)
print(f"Is {num1} not equal then {num2}: ", num1 != num2)