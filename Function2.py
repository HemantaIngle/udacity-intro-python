
'''#hello we will have a look at the accessibility of a variable in an program

# This will result in an error
def some_function():
    word = "hello" # here the word is accessible in the scope of the function some_function only

print(word) # printing this word outside a function will cause an error, lets see how
# so we have  an error "NameError: name 'word' is not defined"

#  now lets try to make the program work by properly calling the function
def some_function():
    word = "hello" #
    return word

print(some_function()) # here we call a function which returns a value none as we missed to return in the function

# thanks for watching'''
from typing import List

'''# lets look into an another concept of scopes
str1 = 'Functions are important programming concepts.'# it printed out this as str1 was no longer restricted withen the function
def print_fn():
   # str1 = 'Variable scope is an important concept.'
    print(str1)
# Notice here that we dont return the value , but it will still print out
print_fn()

# Now we have a another concept about scopes we try to comment out the str1 from the function
#thanks for watching'''
#The below code will give a type error print_fn takes 0 arguments but one was given
'''def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn(str1)

# Similarly the below code will also give the same error
str1 = 'Functions are important programming concepts.'

def print_fn():
    print(str1)

print_fn(str1)'''

#map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable.
# The code below uses map() to find the mean of each list in numbers to create the list averages.
numbers: List[List[int]] = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):  # Define the function
    return sum(num_list) / len(num_list) # return the average
averages = list(map(mean, numbers)) # the map function iterates the function over the iterable
print(averages)

#Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

averages = list(map(lambda x: sum(x) / len(x), numbers))# the list in this line specifies the numbers list, map takes
# the formula of average and iterates over list of numbers
print(averages)

#Lambda with filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
