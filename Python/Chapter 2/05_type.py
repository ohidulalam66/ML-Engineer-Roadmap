a = 23
b = 7.556
c = 'Ohid'
d = "65.87"

x = type(a) # <class 'int'>
y = type(b) # <class 'float'>
z = type(c) # <class 'str'>

m = float(d) # d but the type should be float
n = type(m)

print(x, y, z, m)