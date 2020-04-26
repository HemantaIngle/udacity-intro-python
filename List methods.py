#Topic-Finding Unique Words
#Coded by- Hemanta Ingle
#Problem Statemsnt- Sentences are provided without any punctuations and we are supposed to find out unique elements of of them

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n") # Print the verse as it is
verse_list = verse.split() # split verse into list of words
print(verse_list, '\n')
verse_set = set(verse_list)# convert list to set to get unique words
print(verse_set, '\n')
num_unique = len(verse_set)# print the number of unique words
print(num_unique)