#Asteroids 1.0
#Parker Gowans

#Imports
from superwires import games
import random
import math


#Global Info
games.init(screen_width = 640, screen_height = 480, fps = 60)







#Classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/Asteroid_small.png"),
                      MEDIUM : games.load_image("images/Asteroid_med.png"),
                      LARGE : games.load_image("images/Asteroid_big.png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid,self).__init__(image = Asteroid.images[size],
                                      x = x,
                                      y = y,
                                      dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                      dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        self.size = size

    def update(self):
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height


class Ship(games.Sprite):
    image = games.load_image("images/spaceship.png")
    sound = games.load_sound("sounds/thrusters.wav")
    ROTATION_STEP = 6
    VELOCITY_STEP = .03

    def __init__(self):
        super(Ship, self).__init__(image = Ship.image,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+= Ship.ROTATION_STEP
            # This is copied code look into to better ways of doing it
            #Wrap the ship around the screen
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
       
        






#Main
def main():
    
    #Load Data
    bg_img = games.load_image("images/background.jpg")



    #Create Objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y , size = size)
        games.screen.add(new_asteroid)

    #Create Ship
    player = Ship()




    #Draw Objects
    games.screen.background = bg_img
    games.screen.add(new_asteroid)
    games.screen.add(player)



    #Game Setup





    #Start main loop
    games.screen.mainloop()


main()
        

