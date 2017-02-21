from random import randint

print "Hello player! Welcome to our guessing game."
player_name = raw_input("What is your name? ")

print "%s, I'm thinking of a number between 1 and 100." % player_name

random_number = randint(1, 101)
print "Guess what number I am thinking: "
print random_number

while True:
    guess = int(raw_input(">> "))
    if guess != random_number:
        if guess > random_number:
            print "Your guess is too high. Try again."
        else:
            print "Your number is too low. Try again."
    else:
        print "Congratulation! You found my number!"
        break
