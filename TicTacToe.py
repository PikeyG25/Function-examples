#Parker Gowans
#12/18
#TicTacToe

#Global Constants
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
        print(
            """This is how you play,
    You need to find out who is going first, you or the computer.
    Once you find out who is going first, you need to find out who is X's and who is O's.
    A board will display and there will be nine spaces available to go in, you then
    place a piece down strategically, then the other person goes. You keep going till
    you get three pieces in a row or you and the other person tie"""
            )
display_instructions()
        
def ask_yes_no(question):
    response = None
    while response not in("y","n"):
        response = input(question + " y or n").lower()
    return response

x=ask_yes_no("Do i hate this class")
print(x)

def ask_number(question,low,high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high+1):
                break
            else:
                response = input(question)
        else:
            print("You must enter a number")
            response = input(question)
    return int(response)
            
x = ask_number("Enter a number between 1 and 10",1,11)
print(x)
        
