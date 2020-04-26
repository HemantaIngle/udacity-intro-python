#Topic- Identify the prize won bythe points
#Coded by- Hemanta Ingle

points = 10# use this input to make your submission

# write your if statement here
if points<=50:
    prin="Wooden Rabbit"
elif points<=150:
    prin="No prize"
elif points<=180:
    prin="Wafer thin mint"
elif points<=120:
    prin="Penguin"
else:
    prin="no value"
print(prin)
message= "Someone with points {} will win the prize {}".format(points,prin)
print (message)