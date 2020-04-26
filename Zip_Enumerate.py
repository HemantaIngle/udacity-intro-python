# This is the code for using zip
# coded by-Hemanta Ingle
"""letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# The code below     """
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends i
# t to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate
# should be F: 23, 677, 4.
from typing import List, Callable

'''x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
for label, x, y, z in zip(labels, x_coord, y_coord,z_coord):
    print(label, x, y, z)
# Thanks for Watching'''

# Use zip to create a dictionary cast that uses names as keys and heights as values.

'''cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

for cast,heights in zip(cast_names,cast_heights):
    print("{}:{}".format(cast,heights))'''

'''letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)'''
'''# Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names,heights= zip(*cast)
print(names)
print(heights)
#Thus we are able to form two seperate lists from a single touple, thanks for watching.'''

# A a Matrix named data is provided we need to find out its transpose , ie a 4*3 matrix will be converted to a 3*4 matrix

'''data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)) # Given MAtrix 4*3
data_transpose = tuple(zip(*data))
print(data_transpose)
# we have  successfully converted a 4*3 matrix  to a 3*4 matrix, thanks for watching
'''

'''
#Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding
# height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i,names  in enumerate(cast):
    print(names, ":",heights[i])'''

'''# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split()[0].lower() for name in names]
print(first_names)
# Note comphrension elimenates the need of creating an empty list and iterting it over the iterable'''

'''#create  a list of multiples of 3 in the range of 21
mul=[3*i for i in range(21)]
print(mul)'''

# if the scores from the Dictionary >= 65 then pass and print the list
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
