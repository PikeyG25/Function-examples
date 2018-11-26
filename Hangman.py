#Hangman game
#Parker Gowans
#11/18
#The classic gmae of Hangman. The computer picks a random word
#and the player wrong to guess it, one letter at a time. If the player
#can't guess the word in time, the little stick figure gets hanged.


#Imports
import random
import time

#Constants
HANGMAN = (
"""
 ________
|        |
|        |
|        |
|       ( )
|        +
|
|
|
|
|________
""",
"""
 ________
|        |
|        |
|        |
|       ( )
|        +
|        +
|
|
|________
""",
"""
 ________
|        |
|        |
|        |
|       ( )
|        +\
|        +
|
|
|________
""",
"""
 ________
|        |
|        |
|        |
|       ( )
|       /+\
|        +
|
|
|________
""",
"""
 ________
|        |
|        |
|        |
|       ( )
|       /+\
|        +
|       /
|
|________
""",
"""
 ________
|        |
|        |
|        |
|       ( )
|       /+\
|        +
|       / \
|
|________
""")

MAX_WRONG=len(HANGMAN)-1
WORDS =()

for i in range(len(HANGMAN)):
    print(HANGMAN[i])
    time.sleep(5)

    
