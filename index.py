name = input("Enter your first and last name")
x=name.find("")
firstName = name[:x]
lastName = name[x+1:]
print(firstName)
print(lastName)
