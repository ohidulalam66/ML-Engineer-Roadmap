age = input("Enter your age: ")

# age1 = age + 1  Error
new_age = int(age) + 1 # type casting

# type conversion
print(2.5 + 1) # implicit
print(int(3.5) + 1) # explicit

print(new_age)

# string operation

name = "Tony Strck"

print(name.upper())
print(name) # String is IMMTABLE

# find
print(name.find("T"))
print(name.find("x")) # output is -1

# replace
print(name.replace("Tony", "Iron"))

# check for presence
print('T' in name) # True

print('Y' in name)

# reserved words
# True, in, False, while, for, break, continue
