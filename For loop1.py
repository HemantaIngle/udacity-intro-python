#Topic-Write a for loop that iterates over the names list to create a usernames list. To create a username for each name,
# make everything lowercase and replace spaces with underscores. Running your for loop over the list:
# coded by- Hemanta Ingle
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1