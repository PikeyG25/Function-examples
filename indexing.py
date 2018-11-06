import random

name = input("Enter your name")
print(name[-4])
length =len(name)
print(length)
index_pos = random.randrange(0,length)
if index_pos<= length:
    char = name[index_pos]
    print(char)
else:
    print("thats out of the range")
