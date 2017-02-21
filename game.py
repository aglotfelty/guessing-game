from random import randint

print "Hello player! Welcome to our guessing game."
player_name = raw_input("What is your name? ")

print "%s, I'm thinking of a number between 1 and 100." % player_name

random_number = randint(1, 100)
print "Guess what number I am thinking: "
counter = 0

while True:
    guess = int(raw_input(">> "))
    counter += 1
    if guess != random_number:
        if guess > random_number:
            print "Your guess is too high. Try again."
        else:
            print "Your number is too low. Try again."
    else:
        print "Congratulations! You found my number in %d guesses!" % counter
        break