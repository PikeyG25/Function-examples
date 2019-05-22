# Donut Eater
# Created by Parker Gowans
# 4/19

#Imports
from superwires import games, color
import random

#Global Variables
games.init(screen_width = 640, screen_height = 480, fps = 60)


#Classes

class Baker(games.Sprite):
    images = games.load_image("images/baker.png", transparent = False)

    def __init__(self, y = 60, speed = 5, odds_change = 100):
        super(Baker,self).__init__(image = Baker.image,
                                  x = games.screen.width / 2,
                                  y = y,
                                  dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx

        self.check_drop()
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop-=1
        else:
            new_donut = Donut(x = self.x)
            games.screen.add(new_donut)
            self.time_til_drop = random.randint(60, 250)

                              
class Homer(games.Sprite):
    image = games.load_image("images/homer.png", transparent = False)

    def __init__(self):
        super(Homer, self).__init__(image = Homer.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)
    
    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
    def check_catch(self):
        for donut in self.overlapping_sprites:
            addtoscore()
            donut.handle_caught()
    
class Donut(games.Sprite):
    image = games.load_image("images/donut.PNG", transparent = False)
    speed = 10                         
    def __init__(self, x, y=90, speed = random.randrange(speed)+1):
        super(Donut,self).__init__(image = Donut.image, x=x, y=y, dy = speed)
    def update(self):
        if self.top > games.screen.height:
            self.destroy()
##            self.end_game()

    def end_game(self):
        """End the game."""
        
    def handle_caught(self):
        self.destroy()    
     
class ScText(games.Text):
    pass


#Main
def main():
#Load Data
    wall_image = games.load_image("images/homerdonut.png", transparent= False)
    

#Create Objects
    the_homer = Homer()
    the_baker = Baker()
    the_donut = Donut(x = 250)
#Draw
    games.screen.background = wall_image
    games.screen.add(the_homer)
    games.screen.add(the_baker)
    
#Game Setup
    games.mouse.is_visible = False
    games.screen.event_grab = True


#Start Loop
    games.screen.mainloop()



#Starting Point
main()
