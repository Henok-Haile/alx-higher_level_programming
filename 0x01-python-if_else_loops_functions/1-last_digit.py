#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Lastdigit = number % -10
else:
    Lastdigit = number % 10
if Lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, Lastdigit))
elif Lastdigit < 6 and Lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, Lastdigit))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, Lastdigit))
