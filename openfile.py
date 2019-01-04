#Parker Gowans
#1/19
import sys
#########################################################################
def open_file(file_name,mode):
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name,"Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
            return the_file
#########################################################################
def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/","\n")
    return line


#########################################################################
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answer = next_line(the_file)
        answers.append(answer)
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation
#########################################################################
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    the_file = open_file("test.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1,":"+answers[i])
        user_input = input("What is the correct answer")
        if user_input == correct:
            print("Congrats")
            score +=1

        else:
            print("You're a failure")
        print(explanation)
        print(score)
        category, question, answers, correct, explanation = next_block(the_file)
    the_file.close()
    print("This is the last question in the program. Thanks for participating.")
    print("This is your score: ",score)
main()
