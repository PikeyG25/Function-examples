game_list=("GTA V",
           "UFC 2",
           "Monopoly",
           "COD Ghosts",
           "R6 Siege",
           "Battlefield 4",
           "WII Sports",
           "BO2",
           "MW2",
           "Minecraft")
print(len(game_list))
num5game=game_list[4]
print(num5game)
middle5=game_list[3:7]
print(middle5)
last4=game_list[6:]
print(last4)
even=game_list[::2]
backward=game_list[::-1]
print(even)
print(backward)
for i in game_list:
    print(i)

game_list +=("11",12,13.0,14,"15")
print(game_list)
game_list[0]= "UFC 2"

           
