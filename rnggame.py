#andrew kellmer and parker gowans 11/2/18
import random

mini = 0
maxi = 100
counter = 5
rng = 50







#menu
def menu():
    global mini
    global maxi
    global rng    

    choice = input("choose an option play/options/credits/quit:").lower()
    if choice == "play":
        print("starting game...")
        rng = random.randrange(mini, maxi)
        game()
    elif choice == "options":
        print("entering options...")
        options()
    elif choice == "credits":
        print("Made by Andrew Kellmer and Parker Gowans.")
        print("Made on 11/2/18")
        menu()
    elif choice == "quit":
        quit1()
    else:
        print("that was not a valid input")
        menu()


#game
def game():
    global counter
    global mini
    global maxi
    global rng
    if counter>0:
        print("you have",counter,"tries left. The range is",mini,"-",maxi,".")
    
        guess = input("enter your guess or quit").lower()

        if guess.isdigit():
            guess = int(guess)
            if guess == rng:
            
                print("you guessed correctly. good job. returning to the menu...")
                menu()
    
            elif guess>=rng:
                print("you guessed too high!.")
                counter = counter-1
                game()
        
            elif guess<=rng:
                print("you guessed too low!.")
                counter = counter-1
                game()

            else:
                print("the value you entered was not in the range.")
                game()
                
        elif guess.isalpha():
            if guess == "quit":
                print("quitting the game. returing to menu...")
                menu()
            else:
                print("that was not a valid input")
                game()
            
        else:
            print("that was not a valid input")
            game()

    else:
        print("you have run out of guesses.")
        print("the number was:",rng)
        counter=5
        menu()


#options
def options():
    global mini
    global maxi
    global counter

    yn = input("would you like to edit the options y/n:").lower()

    if yn == "y" or yn == "yes":
        print("the default minimum is 0")
        mini = int(input("enter a new minimum"))
        print("the default maximum is 100")
        maxi = int(input("enter a new maximum"))
        print("the default counter(number of guesses) is 5")
        counter = int(input("enter a new counter"))
        print("settings saved, returning to menu...")
        menu()

    else:
        print("returning to menu...")
        menu()





#quit
def quit1():
    print("you have quit the game.")
    quit




menu()
