import random
import re

# create regex pattern  to recognize numbers
pattern = re.compile("\\d+")


# take input from user and find integers 
def decideRandom(inputfromuser):
    matches = pattern.findall(inputfromuser)
    firstval: object = matches[0]
    secondval = matches[1]
    return random.randint(int(firstval), int(secondval))


def main():
    random.seed()  # initialize random number system
    print(decideRandom(input("What range would you like the random value to be within?\n")))
    # ask the user what range the number should be in and print the number using 
    # "decideRandom" function


main()
