#Parker Gowans
#10/18
import random

win=0
pHealth = 100
mHealth = 100

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheates his sword for the last fight of his life.\n")
choice = input("fight or run")


while choice == "fight" or "Fight":
    playerDamage = random.randrange(0,30)
    print("You attack the trolls and did ",playerDamage,"damage killing hundreds of trolls")
    mHealth-= playerDamage
    if mHealth > 0:
        monsterDamage = random.randrange(0,50)
        print("The troll attacks you back doing", monsterDamage,"damage")
        pHealth-= monsterDamage
    if pHealth<=0:
        print("You have died")
        win = 0
        break
    elif mHealth <=0:
        print("You have killed the trolls")
        win = 1
        break
    elif pHealth >=0 and mHealth >=0:
        print("You have ",pHealth,"health")
        print("the trolls have" ,mHealth,"health")
        choice = input("fight or run")
        if choice == "fight":
            print("You attack again")
        elif choice == "run":
            break

if choice == "run":
    print("You are a coward")
if win == 0:
    print("Game over")
else:
    print("You win")
        


