import random
r = random.randint(1,100)

print "I have thought of a number. Its your turn to guess."

guesses = []

while True:
    guess = input("Enter your guess[1,100] :")
    guesses.append(str(guess))
    
    if guess < r:
        print "Low"
    elif guess > r:
        print "High"
    else:
        print "Bingo!! You guessed it right!"
        print "You took", len(guesses), 'guesses'
        print "These were your guesses",  "-->".join(guesses)
        break
        
# you took n number of guesses
# and these were your guesses  [60,70,30]