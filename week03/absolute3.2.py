# Give the absolute value of a number
#
# Author: Andrew Beatty
# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float - 3.7- como redondar um numero

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))∏