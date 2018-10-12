##loops = 0
##while True:
##    print("I have looped ", loops, " times")
##    loops+=5
##    if loops>1000:
##        break
##    

##count = 0
##while True:
##    count+=1
##    if count>100:
##        break
##    if count==5 or count==25 or count==50 or count==75:
##        continue
##    print(count)


print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheates his sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health >=0:
    trolls += 1
    health-=damage
    print("Your hero swings and defeats an evil troll, "\
          "but takes" , damage, "damage points.\n")
    

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")
