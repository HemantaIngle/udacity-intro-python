'''def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 3)
print(cylinder_volume)'''

'''#This is a demo program for showing use of functions
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)    # Here printing is done in the function itself
# this returns something
def add_ten(num):    # here the function returns the value of the modified number
    return (num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5) # here we call the function which already prints the value whereas
print('Done calling')
print('This function returned: {}'.format(return_value_1))# This print statement is returning nothing

print('\nCalling add_ten...')
return_value_2 = add_ten(5)# Here the function returns the value , printing is your task
print('Done calling')
print('This function returned: {}'.format(return_value_2)) # this return value actually returns and we print out the value
# Thanks for watching'''

'''#Write a function named population_density that takes two arguments, population and land_area,
# and returns a population density calculated from those values. I've included two test cases that
# you can use to verify that your function works correctly. Once you've written your function.

def population_density(population,landarea): # here i  define a function that returns population density
    return population/landarea
test1 = population_density(10, 1)# calling the function
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
#our expected and actual results match , thanks for watching'''

# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string
# that says how many weeks and days that is. For example, calling the function and printing the result like this:
# print(readable_timedelta(10))
# 1 week(s) and 3 day(s).
# write your function here
Weeks = 0
days1 = 0
def readable_timedelta(days):
    Weeks =days // 7
    days1=days % 7
    return "Number of weeks are {} and days are {}".format(Weeks, days1)

print(readable_timedelta(21))
# Thanks foor watching