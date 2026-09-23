# Basic if, elif, else 

is_raining = False

if is_raining:
    print("Take Umbrella")
else:
    print("Wear Sunglass")


#  Zodiac Signs

name = input("What is your name: ")
month = int(input("Enter month (1-12): "))
day = int(input("Enter day(1-31): "))

print(f"\n{name}! Here your furtune.")

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = "Aries"

elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = "Taurus"

elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    zodiac = "Gemini"

elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    zodiac = "Cancer"

elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = "Leo"

elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = "Virgo"

elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    zodiac = "Libra"

elif (month == 10 and day >= 24) or (month == 11 and day <= 21):
    zodiac = "Scorpio"

elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac = "Sagittarius"

elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = "Capricorn"

elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = "Aquarius"

elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = "Pisces"

else:
    zodiac = "Invalid date"

print(zodiac)


# Nested of statments

grade= 92

if grade >= 90:
    if grade > 95: # 96-100
        print("Otstanding.")
    else: # 90-95
        print("Excellent.")
else: # 0-94
    print("Not enough")

# TERNARY condition (one linear if - else)

age = int(input("How old are you?\n"))
states = "you are a: Adult" if age >= 18 else "You are a: Minor"

print(states)

# Prectice PROBLEM

# Check if number positive, second or zero
num = float(input("Enter a number: "))

if num > 0:
    print("Number is Positive.") 
elif num < 0:
    print("Number is Negative.") 
else:
    print("Number is zero.")

# largest of 3 numbers

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a >= b and a >= c:
    print(f"a= {a}")
elif b >= a and b >= c:
    print(f"b= {b}")
else:
    print(f"c= {c}")


# Haunted Treasure door / Door of luck
import random

print("Wellcome to DOOR OD LUCK GAME")
print("There are three doors in front of you; choose the one that will allow you to return alive.")

correct_door_no = random.randint(1,3)
choice_door_no = int(input("Select any one door from 1 to 3: "))

if correct_door_no == choice_door_no:
    print("Congratulations! You've alive this time.")
elif choice_door_no == 1 or choice_door_no == 2 or choice_door_no == 3: 
    print("Sorry, you have to die now.")
else:
    print("Invalid Door.")