##Pseudocode:
##num1: input from the user;
##num2: inpout from the user;
##
##check numbers if num1 and num2 are all digits
##if both are digits tell user
##if one or the other is a digit tell user
##if neither are digits tell user


num1 =input("enter a number")
num2 =input("enter a number")
if num1.isdigit() and num2.isdigit():
    print("both are digits")
elif num1.isdigit() or num2.isdigit():
    print("num1 or num2 is a digit")
else:
    print("no digits")

