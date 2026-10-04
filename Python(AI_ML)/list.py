criket_instruments = ['Ball', 'Bat', 'Gloves', 'Guard']
print(criket_instruments)
print(type(criket_instruments))
print(criket_instruments[1]) # Accessing Element
print(criket_instruments[-1]) # list last element
criket_instruments[2] = 'Helmet'  # Modifying element
print(criket_instruments)
criket_instruments.append('Gloves')  # Adding element
print(criket_instruments)
criket_instruments.insert(2, 'Pads') # Insert any index elements
print(criket_instruments)
criket_instruments.pop() # last element remove 
print(criket_instruments)
criket_instruments.remove('Pads') # Remove any index element
print(criket_instruments) 
del criket_instruments[2] # Remove any index element
print(criket_instruments)

# length and loop
print(len(criket_instruments))

for instrument in criket_instruments:
    print(instrument) 

# List Slicing
print(criket_instruments[0:2])
print(criket_instruments[1:])
print(criket_instruments[:3])
print(criket_instruments[::-1]) # list reverse

# list Comperhension
ages = [5, 12, 15, 17, 19, 21, 23, 25]
print(ages)
next_5years = (f"After 5 years: {[age + 5 for age in ages]}")
print(next_5years)

matrix = [[9, 5], [16, 48]]
print(matrix[1] [1])

num = [2, 6, 3, 10, 9, 5]
num.sort()
print(num)
num.reverse()
print(num)