# Dictionary 
student = {
    "name": "ohid",
    "age": 27,
    "course": "AI/ML"
}

print(student)

# Create empty dictionary
dict = {}

# Accessing value
print(student["course"])
print(student.get("name"))

# Avoid KeyError
print(student.get("university"))
print(student.get("university", "Not Found"))
# print(student["university"])

# Add new key
student["blood_group"] = "AB+"
print(student)

# update key
student["course"] = "AI/ML Automation"
print(student)

# Remove by key
student.pop("age")
print(student)

del student["course"]
print(student)

# all items clear
student.clear()
print(student)

# Dictinary Method

person = {"hobby": "Cooking", "city": "Chattogram", "university": "ABC", "color": "Blue"}

# dict key
print(person.keys())

# dict values
print(person.values())

# dict items
print(person.items())

# loop for dict
for key, value in person.items():
    print(key, "=", value)

# Nested Dictionary
students_data = {
    "101": {"name": "Robin", "age": 19, "college": "EFD", "hobby": "Biking"},
    "102": {"name": "Ovi", "age": 20, "college": "HDS", "hobby": "Chilling"},
    "103": {"name": "Tahia", "age": 13, "college": "SAC", "hobby": "Borring"},
}
print(students_data)
print(students_data["103"])
print(students_data["102"]["name"])

# squares of numbers
squares = {x**2 for x in range(6)}
print(squares)

# Merging Dictionary
d1 = {"a": 4, "b": 9, "c": 3}
d2 = {"b": 5, "c": 2, "d": 10}

merged = {**d1, **d2}
print(merged)

# counter of frequancy

from collections import Counter

data = ["bottle", "table", "chair", "earpod", "phone", "bottle"]

print(Counter(data))