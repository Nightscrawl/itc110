# Assignment 4: Word Counter
# Calculate the number of words in a sentence entered by the user.

def main():

    print("This returns the word count for a given sentence.")
    print()
    message = str(input("Enter a sentence: "))

    # splits the string into a list of component words with 'split'
    # counts the length of the list with 'len'
    count = len(message.split())
    
    print("Word count is:", count)
    
main()
