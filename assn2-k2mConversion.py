# Assignment 2: Write a program that converts distances measured in kilometers to miles.
# One kilometer is approximately 0.62 miles.

def k2mConversion():
    print("This program converts kilometers to miles.") #prints a message
    
    km = float(input("What is the distance in kilometers? ")) #asks the user for input; 'float' allows for decimals
    miles = km * 0.62 #conversion formula
    
    print("The distance is", str(miles), "miles.") #prints the result

def main():
    k2mConversion() #runs the stated function as many times as desired

main()
