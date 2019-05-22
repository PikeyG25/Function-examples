#Asteroids 1.0
#Parker Gowans

#Imports
from superwires import games
import random



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









#Main
def main():
    #Load Data
    bg_img = games.load_image("images/background.jpg")



    #Create Objects
    new_asteroid = Asteroid(x = 100, y = 100, size = 2)






    #Draw Objects
    games.screen.background = bg_img
    games.screen.add(new_asteroid)




    #Game Setup





    #Start main loop
    games.screen.mainloop()


main()
        

