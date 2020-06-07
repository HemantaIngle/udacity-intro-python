'''We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where
you want to organize your code into multiple files and reuse code in those files. If the Python script you want to import
is in the same directory as your current script, you just type import followed by the name of the file, without the .py
extension.'''
# USE OF MAIN FUNCTION
'''To avoid running executable statements in a script when it's imported as a module in another script, include these 
lines in an if __name__ == "__main__" block. Or alternatively, include them in a function called main() and call this in
the if main block.
Whenever we run a script like this, Python actually sets a special built-in variable called __name__ for any module. 
When we run a script, Python recognizes this module as the main program, and sets the __name__ variable for this module to 
the string "__main__". For any modules that are imported in this script, this built-in __name__ variable is just set to the 
name of that module. Therefore, the condition if __name__ == "__main__"is just checking whether this module is the main program.'''

'''import Modules as uf #import the module Modules as object uf

scores = [88, 92, 79, 93, 85] # list of scores

mean = uf.mean(scores) # calling the module mean and passing the argument scores list
curved = uf.add_five(scores) # Calling add_five

mean_c = uf.mean(curved)

print("Scores:", scores) # printing the output
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

# thanks for watching'''

## print e to the power of 3 using the simple method
'''exponent=0
exponent = int(input("please enter a input to be cubed"))
cubed= exponent**3
print("The cubed value is ",cubed)'''

# print e to the power of 3 using the math module
from math import exp, expm1
num=0
num=int(input("please input a number to be cubed using module method"))
print("the exponent is ",exp((num)e3))