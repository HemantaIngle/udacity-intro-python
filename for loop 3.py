# Topic: Count the number of words in the dictionary
# Coded by Hemanta Ingle
if False:
    book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
    word_counter={}
    for word in book_title:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

    print(word_counter)
    # Thanks for watching

#Topic:Accessing the values as well as the keys in a for loop
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
if False:
    for actors in cast:
        print(actors)
    for actors, value in cast.items():# here we use .items method to access the values of the keys
        print("Actor: {}    Role: {}".format(actors, value))# here actors is the key and value is the value Ie. role in this case
    #Thanks for watching

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

type = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for items, value in basket_items.items():
    if items in fruits:
        type += value
    # Iterate through the dictionary

    print("items:{} value:{}".format(items, value))

# if the key is in the list of fruits, add the value (number of fruits) to result

print(type)
# Now we will try for different examples and see if our logic still works
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for items, value in basket_items.items():
    if items in fruits:
        type += value
    # Iterate through the dictionary

    print("items:{} value:{}".format(items, value))

# if the key is in the list of fruits, add the value (number of fruits) to result

print(type)




#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for items, value in basket_items.items():
    if items in fruits:
        type += value
    # Iterate through the dictionary

    print("items:{} value:{}".format(items, value))

# if the key is in the list of fruits, add the value (number of fruits) to result

print(type)





#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for items, value in basket_items.items():
    if items in fruits:
        type += value
    # Iterate through the dictionary

    print("items:{} value:{}".format(items, value))

# if the key is in the list of fruits, add the value (number of fruits) to result

print(type)






#Thanks for watching





















