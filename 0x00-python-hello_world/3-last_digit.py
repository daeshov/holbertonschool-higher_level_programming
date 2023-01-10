#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(last_digit)
if last_digit == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(last_digit))
if last_digit < 6 and not 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(last_digit))
