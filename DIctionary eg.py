#Topic- Do operations on dictionary  provided
#Coded by- Hemanta Ingle
#Discription- verse_dict is the dictionary that hold values and  keys , perform the operations given
#1) Display  the contents of the dictionary
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

#2)find number of unique keys in the dictionary- 51
num_keys = len(verse_dict)
print(num_keys)

#3) find whether 'breathe' is a key in the dictionary- False
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

#4)# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

#5) get the first element in the sorted list of keys- about
print(sorted_keys[0])

#6) find the element with the highest value in the list of keys- yourself
print(sorted_keys[-1])