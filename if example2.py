
age = input("how old are you")

if not age>"15" and not age <"70":
    print("you are old enough to drive")
elif age>"70":
    print("you're too old to drive")
elif age<"15":
    print("you're too young to drive")
else:
    print("you shouldn't be driving")
