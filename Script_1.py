'''Imagine you're a teacher who needs to send a message to each of your students reminding them of their missing
 assignments and grade in the class. You have each of their names, number of missing assignments, and grades on
 a spreadsheet and just have to insert them into placeholders in this message you came up with:
 [insert student name],
This is a reminder that you have [insert number of missing assignments] assignments left to submit before you can graduate.
 Your current grade is [insert current grade] and can increase to [insert potential grade] if you submit all assignments
 before the due date.'''
# Start of Program
'''i=0
names=[]
i: int
string="Hi {},This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date."

for i in range(3):
    name = input("enter a name")
    assignments=int(input("Enter the no of assignments"))
    grades=int(input("Enter the grades"))
    potentialgrades=(2*grades)+assignments# we added thi line to calculate the potential grade
    print(name)
    print(assignments)
    print(grades)
    print(string.format(name, assignments, grades, potentialgrades))


    i+=1'''

# now we are going to use another method to provide the inputs

string="Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. \nYour current grade is {} and can increase to {} if you submit all assignments before the due date."
names = (input("enter the names seperated by commas ")).title().split(",")# here we are asking a user to input names seperated bhy commas which will facilitate splitting and adding to a list generated  ie names
assignments=(input("Enter the no of assignments")).split(",") # similar with assignments , we are splitting the names and creating a list
grades=input("Enter the grades").split(",")

print(names) # lets see how the lists look like
print(assignments)
print(grades)
for name, assignment, grade in zip(names,assignments,grades): # for iterates over each item in the list and zips the three parameters list
    potentialgrades = int(grade) + int(assignment) * 2  # we added thi line to calculate the potential grade
    print(string.format(name, assignment, grade, potentialgrades))# .format appends the iterable variables

# lets run the program and see the output, Thanks for watching.

