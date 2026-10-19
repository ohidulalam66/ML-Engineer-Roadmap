tuple1 = ("laptop", "mouse", "keyboard") # collection of tuple
print(type(tuple1)) # this call tuple
print(tuple1)

tuple2 = ("Pendrive") # single collection of not tuple
print(type(tuple2)) # this call string
print(tuple2)

# Tuples and lists are not the same, because the elements of a tuple cannot be used like a list.
list = ['laptop', 'mouse', 'keyboard']
print(list[1])
list[1] = "pendirve"
print(list)

# tuple1[1] = "pendrive"
# print(tuple1) # error

# Slicing   

numbering = (10, 20, 30, 40, 50, 60, 70)

# output: (20, 30, 40, 50) from index 1 to 
print(numbering[1:4]) # But Output: (20, 30, 40)
print(numbering[1:5]) # Output: (20, 30, 40, 50)

# Start from Beginning
print(numbering[ : 4])
# Start from index 4
print(numbering[4 : ])
# skip one element
print(numbering[ :: 2])
# Reverse order
print(numbering[ :: -1])

# loop
for item in numbering:
    print(item)

# packing and unpacking of tuple
packed_tuple = ('apple', 'orange', 'cherry')
print(packed_tuple)

apple, orange, cherry = packed_tuple
print(apple, orange, cherry)

# Method
tuple3 = ('chair', 'table', 'book', 'table', 'book', 'pen')
print(len(tuple3))
print(tuple3.count("table"))
print(tuple3.index("table"))

# Convert tuple to list
colors = ('white', 'black', 'blue', 'red')
colors_list = [*colors]
print(colors_list)

colors_list.append('green')
print(colors_list)

# Convert list to tuple
color_tuple = tuple(colors_list)
print(color_tuple)

# Sorting
pairs = [(3, 4), (0, 10), (1, 2, 3), (2, 9)]
print(sorted(pairs))

# find the topper
def topper(students):
    highest_avg = 0
    name = ""

    for name, marks in students:
        avg = sum(marks)/len(marks)

        if avg > highest_avg:
            highest_avg = avg
            topper_name = name
    return topper_name, highest_avg

# Example
students = [
    ("coyon", [67, 98, 43, 65]),
    ("ovi", [65, 80, 77, 62]),
    ("tahia", [54, 53, 85, 83]),
    ("robin", [89, 63, 45, 71]),
    ("sumiya", [79, 43, 75, 51])
            ] 
print(f"The Topper student: {topper(students)}")