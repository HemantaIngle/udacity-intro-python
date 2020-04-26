actual_number=12
guessed_number=12
if guessed_number  < actual_number:
    result="the guess is too low"
elif guessed_number  > actual_number:
    result="the guess is too  high"
elif guessed_number == actual_number:
    result="You guessed it right"
message="The number you guessed is {} and {}".format(guessed_number, result)
print(message)

