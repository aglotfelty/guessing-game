from random import randint

print "Hello player! Welcome to our guessing game."
player_name = raw_input("What is your name? ")
print "%s, I'm thinking of a number between 1 and 100." % player_name
playing_game = True
best_score = 0

while playing_game:
    print "Great! Let's play" 
    random_number = randint(1, 100)
    print random_number
    print "Guess what number I am thinking: "
    counter = 0

    while True:
        counter += 1
        try:
            guess = int(raw_input(">> "))
        except ValueError:
            print "That is not a number! Try again."
            continue

        if guess != random_number:
            if guess > 100 or guess < 1:
                print "You idiot!! That number is not between 1 and 100. Try again."
            elif guess > random_number:
                print "Your guess is too high. Try again."
            else:
                print "Your number is too low. Try again."
        else:
            print "Congratulations! You found my number in %d guesses!" % counter
            if best_score == 0 or best_score > counter:
                best_score = counter
                print "Congratulations! You have the new best score!"
            else:
                print "The score to beat is %d" % best_score
            break
    play_again = raw_input("Would you like to play again? (Yes/No) ")
    if play_again == "Yes":
        continue
    else:
        playing_game = False
print "Thank you for playing our game!"


# while playing_game:
#     counter += 1
#     try:
#         guess = int(raw_input(">> "))
#         if guess != random_number:
#             if guess > 100 or guess < 1:
#                 print "You idiot!! That number is not between 1 and 100. Try again."
#             elif guess > random_number:
#                 print "Your guess is too high. Try again."
#             else:
#                 print "Your number is too low. Try again."
#         else:
#             print "Congratulations! You found my number in %d guesses!" % counter
#             play_again = raw_input("Would you like to play again? (Yes/No) ")
#             if play_again == "Yes":
#                 print "%s, I'm thinking of a number between 1 and 100." % player_name
#                 random_number = randint(1, 100)
#                 print random_number
#                 print "Guess what number I am thinking: "
#                 counter = 0
#                 continue
#             else:
#                 playing_game = False
#     except ValueError:
#         print "That is not a number!"