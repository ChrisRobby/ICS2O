# entry to hangman

import sys
import hangman

inputStr = input("Difficulty level? (0 - easy; 1 - normal; 2 - hard; 3 - quit): ")
print (inputStr)


difficulty = int(inputStr)
maxLives = 0

if difficulty == 0:
    maxLives = 10
elif difficulty == 1:
    maxLives = 6
elif difficulty == 2:
    maxLives = 3
elif difficulty == 3:
    print("quitting ... ")
    sys.exit()

print("maxLives = ", maxLives)

result = hangman.startgame(maxLives)

print("Result = ", result)

