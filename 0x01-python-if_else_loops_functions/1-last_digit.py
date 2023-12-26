#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# the last digit of the value of the number
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# print the result based on the last digit
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
