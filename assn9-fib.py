# assn9-fib.py
# Assignment 9 - Fibonacci Sequence
# Kira Abell
# 8/10/19

# A program to compute the Fibonacci sequence,
    # using input from the user.

# "The Fibonacci sequence starts 1, 1, 2, 3, 5, 8,...
    # Each number in the sequence (after the first two) is the sum of the
    # previous two. Write a program that computes and outputs the
    # nth Fibonacci number, where n is a value entered by the user."

# input: the number of loops to iterate
# processing: forumla to compute via swiching variable values
# output: fib sequence


def fib(n):
    # sets initial values of x, y, the first two numbers in the sequence
    x, y = 0, 1

    # n sets the number of iterations from user input
    # calculates the values of x+y and replaces those values
    # iterates n times, printing the result of each loop on the same line
    for i in range(n):
        x, y = x+y, x
        print(x, end=" ")

    print("\nThe value for", n, "is", x)

def main():
    print("Welcome.")
    print("This program calculates the Fibonacci sequence.")
    print()

    # gets input from the user
    n = int(input("Enter the number of the values for the sequence. "))
    # calls fib function and plugs in the n value
    fib(n)
    
    # test: n = 9   -- 1 1 2 3 5 8 13 21 34
    # test: n = 12  -- 1 1 2 3 5 8 13 21 34 55 89 144


    # allows program to run from the command line without immediately closing
    print()
    input("Hit Enter to close.")

if __name__ == "__main__":
    main()


    # working formula example:
    # x, y = 0,1
    # x, y = x+y, x

    # 1, 0 = 0+1, 0
    # 1, 1 = 1+0, 1
    # 2, 1 = 1+1, 1
    # 3, 2 = 2+1, 2
    # 5, 3 = 3+2, 3
    # 8, 5 = 5+3, 5
    # 13, 8 = 8+5, 8
    # 21, 13 = 13+8, 13
    # 34, 21 = 21+13, 21
    
    # 34 is 9th position
    
