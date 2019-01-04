##while True:
##    try:
##    num = float(input("Enter a number: "))
##    except:
##        print("Something went wrong!")
##
##try:
##    num = float(input("\nEnter a number: "))
##except ValueError:
##    print("That was not a number!")
##
##print(num)

##for value in (None, "Hi!"):
##    try:
##        print("Attempting to convert",value,"-->",end=" ")
##        print(float(value))
##    except (TypeError):
##        print("Something went wrong! type error!")
##    except (ValueError):
##        print("Something went wrong! Value error")

##try:
##    num = float(input("\nEnter a number: "))
##except ValueError as e:
##    print("That was not a number!")
##    print(e)


try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number",num)
