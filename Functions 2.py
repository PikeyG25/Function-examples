#Parker Gowans
#9/18

#Get a users name
def get_name():
    
#Step 1: Ask for users name
    name=input("What's your name")
#Step 2: Display the name back for user
    print("the name you entered was", name)
#Step 3: Verify that the name is correct
    input("Is this correct, yes or no?")

print("this is our function")
##get_name()


#Calculate the area of a circle
#Radius*Radius*pi
def areaOfCircle():
    pi=3.14159265359
    
#1: Get radius
    radius = input("What is the radius")
    
#2: calculate the area
    radius = float(radius)
    area = radius*radius*pi
    
#3: Display the area
    print("The area of the circle is: ",area)

areaOfCircle()
