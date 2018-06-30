"""
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:
"""


def sumDigits(number):
	# Convert number to positive
    positive = abs(number)
	# convert the number into a list
    to_list = list(str(positive))
    # Change the list to be a list of integers
    c = list(map(int, to_list))

    add = sum(c)
    return add