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
##############################################################################
def ask_yes_no(question):
    response = None
    while response not in("y","n"):
        response = input(question + " y or n").lower()
    return response

x=ask_yes_no("Do i hate this class")
print(x)
##############################################################################
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
##############################################################################
def pieces():
        """Decides who goes first"""
        go_first = ask_yes_no("Would you like to go first? (y/n)")
        if go_first == "y":
                ("You will go first")
                human = X
                computer = O
                         
        else:
                print("The computer will go first")
                computer = X
                human = O
        return computer, human
computer, human = pieces()
                
print(computer)
print(human)
##############################################################################
def new_board():
        """Create a new game board"""
        board = []
        for squares in range(NUM_SQUARES):
                board.append(EMPTY)
        return board

board = new_board()
print(board)

##############################################################################
def display_board(board):
        """Display game board on screen"""
        print("\n\t", board[0],"|",board[1],"|", board[2])
        print("\t","---------")
        print("\n\t", board[3],"|",board[4],"|", board[5])
        print("\t","---------")
        print("\n\t", board[6],"|",board[7],"|", board[8])

board = [X,EMPTY,EMPTY,EMPTY,X,EMPTY,EMPTY,EMPTY,X]
display_board(board)
##############################################################################
def legal_moves(board):
        """Create list of legal moves"""
        moves = []
        for square in range(len(board)):
                if board[square]==EMPTY:
                        moves.append(square)
        return moves

board = new_board()
moves = legal_moves(board)
print(moves)
##############################################################################
def winner(board):
        """Determine the game winner"""
        WAYS_TO_WIN = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0,3,6),
                (1,4,7),
                (2,5,8),
                (0,4,8),
                (2,4,6))
        for row in WAYS_TO_WIN:
                if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                        winner = board[row[0]]
                        return winner

        if EMPTY not in board:
                return TIE
        
        return None
##############################################################################
board =[X,X,X,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]
win = winner(board)
print(win)
