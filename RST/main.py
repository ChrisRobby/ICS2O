# entry to hangman

import sys
import hangman

valid = False
while valid == False:
    inputStr = input("Difficulty level? (0 - easy; 1 - normal; 2 - hard; 3 - quit): ")
    print (inputStr)
    if inputStr >= '0' and inputStr <= '3':
        valid = True

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

# print("maxLives = ", maxLives)
# start the hangman game and set the max lives
result = hangman.startgame(maxLives)

# print("Result = ", result)
# check the result and print a message
if result == hangman.WIN:
    print ("You Win!")
elif result == hangman.LOSE:
    print ("You lose. :-(")
else:
    print ("Error: startgame failed")
