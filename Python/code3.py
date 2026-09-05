# arithetic operator
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3) # floting point break-down
print(5 % 3) # module -> reminder
print(5 ** 3) # power 

# Assignment operator
x = 10
x -= 5 # x = x(10) - 5 = 5
x *= 3 # x = x(5) * 3 = 15

print(x)

# Operator Precedence

ans = 5 + 2 * 7 # () > */ > +-
ans2 = (5 + 2) * 7

print(ans, ans2)

# Comparison  -> ==, !=, >, <, >=, <=, !>, !<

print( 3 == 6) # False
print( 3 > 6) # False
print( 9 > 6) # True
print( 9 != 6) # True
print( 6 >= 5) # True

# Logical Operators -> or, and, not

stt1 = 3 > 4 # False
stt2 = 3 < 4 # True

print( stt1 or stt2) # True
print( stt1 and stt2) # False
print(not True)

# Conditional Statmant

num = input("Enter your Math Marks: ")
marks = int(num)

if marks <= 100 and marks >= 80:
    print("A+")
elif marks < 80 and marks >= 60:
    print("A")
else:
    print("C")


