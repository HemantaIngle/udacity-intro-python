# Topic:Find out the card given a condition of sum
if False:
    card_deck = [2, 5, 7, 10]
    hand = []  # declare an empty variable
    while sum(hand) <= 17:  # iterate in the loop till the value of the hand >=17
        hand.append(card_deck.pop())  # pop returns the last element in tbe  list
        print(hand)
    print(hand)

# Find out factorials using the while loop

# number to find the factorial of
if False:
    number = 5
    # start with our product equal to one
    product = 1
    # track the current number being multiplied
    current = 1

    while current <= number:
        # multiply the product so far by the current number
        product *= current
        print(product)
        # increment current with each iteration until it reaches number
        current += 1
    # Thanks for watching

    # print the factorial of number
    print("final factorial is", product)

# Count a number using the while loop
if False:
    import time

    time.sleep
    start_num = 1  # provide some start number
    end_num = 9  # provide some end number that you stop when you hit
    count_by = 1  # provide some number to count by
    break_num = 1
    print(break_num)
    while break_num <= end_num:
        break_num += 1
        time.sleep(1)

        print(break_num)
    # write a while loop that uses break_num as the ongoing number to
    #   check against end_num
    print("The final count number is :", break_num)

if False:
    # Find out the nearest Square
    # example- if number 40 is given the nearest neighbour will be 36
    no=40
    sr=0
    num=0
    while (num+1)**2 <= no:
        sr=num**2
        num+=1
        print (num)

        # we have 6 as the nearest square , thanks for watching

if False:
    #Topic-You need to write a loop that takes the numbers in a given list named num_list:
    num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    #Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5
    #odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers
    add=1
    for num in num_list:
        if num%2 != 0:
            add+=num
        print(num)
        print(add)
if False:
    num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    count_odd = 0
    list_sum = 0
    i = 0
    len_num_list = len(num_list)

    while (count_odd < 5) and (i < len_num_list):
        if num_list[i] % 2 != 0:
            list_sum += num_list[i]
            count_odd += 1
        i += 1

    print ("The numbers of odd numbers added are: {}".format(count_odd))
    print ("The sum of the odd numbers added is: {}".format(list_sum))
    #Thanks for watching

#Topic-USing break statement
# in this problem we will add the items until the weight has been reached and then we will stop
# the manifest tuple gives us list of items to be loaded
# METHOD 1
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest: # the loop again comes here and checks all conditions and runs till all conditions are met
    print("current weight: {}".format(weight))# we take this variable to mesure the weight and we will add items weights later on
    if weight >= 100:# in the 1st iteration the weight=0 so this condition dosent satisfy so it dosent enter the loop
        print("  breaking loop now!")
        break # finally it finds that the weight is greater than 100 , so it breaks the loop.
    else: # program comes here it adds 0+ item 1 s weight ie. 15
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        print(items)
        weight += cargo_weight # so we get current weight to be 15
# but there is a problem in the above loop as it exceeds weight limit 100 as the weight before the last
#iteration is less than 100 so the loop tries to add one more item to the list.and so we get the weeight to be 201 and thats way too much than 100

# METHOD 2
# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print(cargo_weight)
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# we use two methods as the method 1 is adding items even if the weight is exceded., now lets run the program