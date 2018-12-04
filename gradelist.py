#Parker Gowans
#12/18
#Average grades

gradelist =[]
def getGrade(gradelist):
    while True:
        maxGrade = 100
        grade = input("Enter in a grade, to exit press spacebar")
        if grade == "":
            break
        elif grade.isdigit() and grade.isalnum():
            grade = float(grade)
            if grade <= maxGrade:
                gradelist.append(grade)
                
            else:
                q=input("Are you sure this "+str(grade)+"is a good grade y or n")
                if q == "y":
                    gradelist.append(grade)
                else:
                    print("That's not a good grade")
            
        else:
            print("That's not a good grade")

def avgfunction(gradelist):
    total = gradelist.sum() 
    
    avg = total / len(gradelist)
    return avg
def main(gradelist):

    getGrade(gradelist)
    avg = avgfunction(gradelist)
    xmax = gradelist.max()
    xmin = gradelist.min()
    print(xmax)
    print(xmin)
    print("Your grade is",avg)

main(gradelist)
