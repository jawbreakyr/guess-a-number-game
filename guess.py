# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui



# initialize global variables used in your code
limits = 100
number_to_guess = random.randrange(0, 100)
guess_tries = math.ceil(math.log(limits+1,2))


# define event handlers for control panel
def range100():
    global number_to_guess, guess_tries, limits
    number_to_guess = random.randrange(0, 100)  
    guess_tries = math.ceil(math.log(limits+1,2))
    print "Let's try a new secret number game, ranging from 0 to 100!"
    print "You have", int(guess_tries),"guesses remaining.\n"
    # button that changes range to range [0,100) and restarts
    

def range1000():
    global number_to_guess, guess_tries, limits
    number_to_guess = random.randrange(0, 1000)
    limits=1000
    guess_tries = math.ceil(math.log(limits+1,2))
    print "Let's try a new secret number, ranging from 0 to 1000!"
    print "You have", int(guess_tries),"guesses remaining.\n"
    # button that changes range to range [0,1000) and restarts
    
    
def input_guess(guess):
    # main game logic goes here	
    global guess_tries, limits, number_to_guess
    guess_tries -= 1 
    if int(guess_tries) > 0 :
        if int(guess) == number_to_guess and limits==100:
            print guess, "is correct. You won congratulation!!! \n "
            guess_tries = math.ceil(math.log(limits+1,2))
            number_to_guess = random.randint(0,limit)
            range100()
     
        elif int(guess) == number_to_guess and limits==1000:
            print guess, "is correct. You won congratulation!!! \n"
            guess_tries = math.ceil(math.log(limits+1,2))
            number_to_guess = random.randint(0,limits)
            range1000()
    
        elif int(guess) > number_to_guess:
            print "Your guess is " + guess + ". Try Lower."
            print "You have", int(guess_tries),"guesses left.\n"
        else:	
            print "Your guess is " + guess +". Try Higher."
            print "You have", int(guess_tries),"guesses left.\n"
    
    else:
        
        if int(guess) == number_to_guess :
            if limits==100:
                print guess, "is correct. You won congratulation! \n "
                guess_tries = math.ceil(math.log(limits+1,2))
                number_to_guess = random.randint(0,limits)
                range100()
     
            else:
                print guess, "is correct. You won congratulation! \n"
                guess_tries = math.ceil(math.log(limits+1,2))
                number_to_guess = random.randint(0,limits)
                range1000()
        else:
            if limits==1000:
                print "You Lose. The Secret Number was ", number_to_guess, " \n"
                print "-" * 40
                guess_tries = math.ceil(math.log(limits+1,2))
                number_to_guess = random.randint(0,limits)
                range1000()
            
            else :
                print "You Lose. The Secret Number was ", number_to_guess," \n"
                print "-" * 40
                guess_tries = math.ceil(math.log(limits+1,2))
                number_to_guess = random.randint(0,limits)
                range100()
# create frame
frame = simplegui.create_frame("Guess The Number Game", 200, 200)


# register event handlers for control elements
game_100 = frame.add_button("Range: 0 - 100", range100)
game_1000 = frame.add_button("Range: 0 - 1000", range1000)
inpt = frame.add_input("Enter a guess number", input_guess, 100)


# call new_game and start frame
frame.start()


# always remember to check your completed program against the grading rubric
