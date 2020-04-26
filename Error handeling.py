# topic- use of error handeling statements
# error handeling statements try out other operations if one fails
# some of them are - try and except statement
# coded by- Hemanta Ingle

'''while True:# infinite loop until condition satisfies
    try: # trying the code
        x=int(input("Enter the integer")) # we input the the right integer number
        break# break out of loop if condition is satisfied , this is satisfied
    except: # if the code above has an exception error then run this code below
        print("that is not a valid number") #
    finally: # print this when the loop is done # it compulsarily prints this
        print("done")
print("that was the right input")# gets out of the loop and prints this
# lets try out this code
# Thanks for watching'''

'''# topic - cookies problem
#The party_planner function below takes as input a number of party people and cookies
# and figures out how many cookies each person gets at the party, assuming equitable distribution of cookies.
# Then, it returns that number along with how many cookies will be left over.
def party_planner(cookies, people): # function to calculate number of cookies each one gets
    leftovers = None # declare the variable for , cookies left after equally dividing
    num_each = None # number of cookies each person gets
    try:
        num_each = cookies // people # actual formulation
        leftovers = cookies % people
    except ZeroDivisionError:# if a xero division error occours then print the code below
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return (num_each, leftovers) # return the value  of the function
#main code
lets_party = 'y' # initialization
while lets_party == 'y': # if y is indicated proceed further

    cookies = int(input("How many cookies are you baking? ")) #Inputs
    people = int(input("How many people are attending? "))
    

    #cookies_each, leftover = party_planner(cookies, people) # cookies_each and leftover are the new variables which take up the output
    print(num_each)

    print ("cookies_each",cookies_each)
    print("leftovers", leftover)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftover))

    lets_party = input("\nWould you like to party more? (y or n) ")
    # lets run the code'''

###############################################################################################py
'''# Reading a external file in python.
f=open('C:/Users/ingle/ws/udacity/Scripting/121.txt','w')# Openinig the file
s=f.write("make it work")# writing a string to the file
f.close() # closing does the job of saving
a=open('C:/Users/ingle/ws/udacity/Scripting/121.txt','r')# open the  file again with read permission
w=a.read()#Read the file
print(w) # print the contents of the file
# so we learnt how to read and write to a txt file
# lets try it out
# now we will physically confirm the location of the file'''
###############################################################################################
'''#here we are having a file 121.txt opened by a new method --with - with closes the file when its processed
#We're the knights of the round table # this iis the line of text in the file 121.txt
#We dance whenever we're able# this too
with open('C:/Users/ingle/ws/udacity/Scripting/121.txt','r') as song:
    print(song.read(2))# tiis will print out only 2 characters from the code, lets run and see
    print(song.read(8))# it will print out next 8 characters
    print(song.read())# it will print remaining all
# Now it prints the content of th whole file, but , we dont want the whole file to be printed so, lets change the code'''
#
'''newlines=[]
with open('C:/Users/ingle/ws/udacity/Scripting/121.txt') as f:
    for line in f:
        newlines.append(line.strip)
print(newlines)'''
###############################################################################################
'''#Topic- There is a cast list and the associated wotk in the file 123.txt
# we want only thee list of the actors
def create_cast_list(filename): # creating a function
    cast_list = [] # Empty list
    with open('C:/Users/ingle/ws/udacity/Scripting/123.txt') as new:# Path for thr file,#use with to open the file filename
        for line in new:  #use the for loop syntax to process each lin
            name = line.split(",")[0]# taking one element no 0 from the fileS
            cast_list.append(name)   #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('123.txt')
for actor in cast_list:
    print(actor)'''
########################################################################
# hello , we will now do a addition of even numbers that the user inputs
# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0 # container to store the sum of list

# seek user input for ten numbers
for i in range(10): # user can input 10 integers only
    userInput = int(input("Enter any 2-digit number: ")) # so we define the type of input as int

    # check to see if number is even and if yes, add to list_sum
    # print incorrect value warning  when ValueError exception occurs
    try:
       # number = userInput
        user_list.append(userInput) # append userInput to user_list
        if userInput % 2 == 0: # the number is even if this happens
            list_sum += userInput # sum list = user Input + list_sum
    except ValueError:
        print("Incorrect value. That's not an int!")# Print an acception if the value isnt correct

print("user_list: {}".format(user_list)) # Print the user list
print("The sum of the even numbers in user_list is: {}.".format(list_sum)) # print the lsum of even numbers
# lets run the code and see
# thanks for watching