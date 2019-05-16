#Parker Gowans
#4/19

#Imports
from superwires import games
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Ship(games.Sprite):
    ship_image = games.load_image("images/spaceship.png")
    
    def __init__(self):
        super(Ship, self).__init__(image = Ship.ship_image,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2)


def main():

    #load data
    bg_image = games.load_image("images/background.jpg",transparent = False)
    #create objects
    the_ship = Ship()
    #draw
    games.screen.background = background_image
    games.screen.add(the_ship)
    #game setup

    #start loop
games.screen.mainloop()
    
main()
