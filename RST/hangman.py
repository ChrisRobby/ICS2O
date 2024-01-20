# The main hangman program

# The maximum number of lives 
MAX_LIVES = 10

# return values for the start game function
ERROR = -1
LOSE  = 0
WIN   = 1


def startgame(maxLives):
    lives = int(maxLives)
    
    ## check maxLives .. must be at least 1 and less than max
    if (lives < 1 or lives > MAX_LIVES ):
        print( "Error: maxLives not valid = %d\n" % lives )
        return ERROR
    
    ## return result
    return WIN


