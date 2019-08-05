# assn8-wages-function.py
# Assignment 8 - Wages in a function
# Kira Abell
# 8/4/19

# A program to calculate wages, including optional overtime pay,
    # using input from the user.

# "Many companies pay time-and-a-half for any hours worked above 40
    # in a given week. Write a program to input the number of hours worked
    # and the hourly rate and calculate the total wages for the week."

# input: number of hours worked
# input: hourly rate
# processing: formula
# output: print result

from math import *

def wages(hours, rate):
    # if input hours are less than or equal to 40,
        # calculates base pay and prints result
    if hours <= 40:
        base = hours * rate
        print("You earned", "${:.2f}".format(base))

    # if input hours are greater than 40,
        # calculates overtime hours, the base rate for 40 hours,
        # adds them together, and prints the result
    elif hours > 40:        
        ot = hours - 40
        pay = (rate * 40) + (rate * 1.5 * ot)
        print("You earned", "${:.2f}".format(pay))

def main():
    print("Welcome.")
    print("This program will calculate your week's pay, including any overtime wages.")
    print()

    # gets input from user
    hours = float(input("How many hours did you work? "))
    rate = float(input("What is your hourly rate in dollars per hour? "))

    wages(hours, rate)

    # test with 36 hours at $10/hr = $360.00
    # test with 40 hours at $10/hr = $400.00
    # test with 42 hours at $10/hr = $430.00
    

    # allows program to run from the command line without immediately closing
    print()
    input("Hit Enter to close.")

if __name__ == "__main__":
    main()
