# -> Mini Project REPL Calculator: (REPL within)

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

print(f"SUM is: {num1+num2}")
print(f"MUL is: {num1*num2}")
print(f"SUB is: {num1-num2}")
print(f"DIV is: {num1/num2}")
print(f"DIVS is: {num1%num2}")
print(f"AVG is: {num1+num2/2}")

# -> ASCII code
print(ord('😁'))
print(chr(128523))

# -> Lucky Number
name = input("Enter your name: ")
day = int(input("Favourite day Number: "))

luckynumber = ord(name[0]) + ord(name[-1]) + day

print(luckynumber)
print(ord('o'))
print(ord('d'))


# -> walrus operator (:=) in REPL only
# Assign + print only one line (print(name := "ohid"))

# color text output in terminal (without extarnal libraries)
# Red text
print("\033[91mThis is red color.\033[0m")

# Golden text
print("\033[93mThis is golden color.\033[0m")

# Green text
print("\033[92mThis is green color.\033[0m")

# use with variable
name = "Ohid"
print("\033[92mHello", name, "Good Morning.\033[0m")

# Minimath with pow(), round(), divmod()
print(pow(12, 6))
print(round(3.9074834636, 2))
print(divmod(13, 3))

# opens in cartoon in browser
import antigravity

# using built-in datetime module
from datetime import date
user_birthyear = int(input("Enter your Bithyear: "))
age = date.today().year - user_birthyear
print(age)


