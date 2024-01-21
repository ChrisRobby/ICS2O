# The main hangman program
import random

# The maximum number of lives 
MAX_LIVES = 10

# return values for the start game function
ERROR = -1
LOSE  = 0
WIN   = 1

dictionary = [ "the dark knight", "iron man" , "captain america" , "avengers" , 
               "the hulk" , "deadpool" , "spider man" , "darth vader" , "luke skywalker", 
               "han solo" , "yoda" , "star wars" , "the terminator" , "green goblin" , 
               "venom" , "obi-wan kenobi" , "stormtrooper" , "jedi" , "homer simpson" , 
               "batman"];

# get a random word from the dictionary 
def getWordFromDictionary():
    length = len(dictionary)
    index = random.randrange(0,length)
    return dictionary[index]

# initialize the guess array from the phrase
# leters must be '_' and spaces left as a spaces
def initGuessStr(phrase):
    guessStr = ""
    for c in phrase:
        if c >= 'a' and c <= 'z':
            guessStr = guessStr + "_"
        else:
            guessStr = guessStr + c
    
    return guessStr

# start the game of hangman with maxLives
def startgame(maxLives):
    lives = int(maxLives)
    
    ## check maxLives .. must be at least 1 and less than max
    if (lives < 1 or lives > MAX_LIVES ):
        print( "Error: maxLives not valid = %d\n" % lives )
        return ERROR

    result = LOSE
    
    # get a random word
    phrase = getWordFromDictionary()
    print(phrase)
    
    # initialze the guess array based on the phrase
    guessStr = initGuessStr(phrase)
    print(guessStr)
    
    
    ## return result
    return result

