# Enter name: Daniel Lewis

import random

targetWord = "THE"

def monkeys_typing():
    length = len(targetWord)
    guess = ""
    for i in range(length):
        guessNumber = random.randint(65, 90)
        guess = guess + chr(guessNumber)
    count = 1
    #print(guess)

    while guess != targetWord:
        guess = ""
        for i in range(length):
            guessNumber = random.randint(65, 90)
            guess = guess + chr(guessNumber)
        #print(guess) Otherwise takes waaay too long
        count +=1
    
    #print()
    return count

#print(monkeys_typing())
# part i
times = 3
totalguesses = 0
for iteration in range(times):
    totalguesses += monkeys_typing()
average = round(totalguesses / times, 2)
print(f"It took an average of {average} guesses to get the target {targetWord}")
