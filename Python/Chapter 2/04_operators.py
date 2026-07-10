# Arithmeitic Operators
a = 8
b = 4
c = a + b
d = a - b

print(c, d)

# Assignment Operators
e = 7 - 5 # assign 7-5 in e
f = 0
f += 3 # Increment the value of f by 3 and then assign it f 
f -= 2 # Decrement the value of f by 2 and then assign it f
f *= 2 # Multiple the value of f by 2 and then assign it f
f /= 2 # Divide the value of f by 2 and then assign it f
f %= 1 # Remainder the value of f by 1 and then assign it f

print(e, f)

# Comparison Operators

g = 6 > 7
h = 6 < 7
i = 6 >= 7
j = 6 <= 7
k = 6 != 7
l = 6 == 7
print(g, h, i, j, k, l)

# Logical Operators

#  Turth table of 'or'
print("True or Flase is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or Flase is", False or False)

print("___________________________________")

#  Turth table of 'and'
print("True and Flase is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and Flase is", False and False)

print("___________________________________")

print(not(False))
print(not(True))
