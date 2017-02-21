from random import randint

print "Hello player! Welcome to our guessing game."
player_name = raw_input("What is your name? ")

print "%s, I'm thinking of a number between 1 and 100." % player_name

random_number = randint(1, 101)
