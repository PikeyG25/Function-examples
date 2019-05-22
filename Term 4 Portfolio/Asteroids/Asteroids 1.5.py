#Asteroids 1.5
#Parker Gowans

#Imports
from superwires import games, color
import random
import math


#Global Info
games.init(screen_width = 640, screen_height = 480, fps = 60)







#Classes
class Game(object):
    def __init__(self):
        #Set level
        self.level = 0
        #Load sound for level advance
        self.sound = games.load_sound("sounds/levelUp.wav")
        #Create score
        self.score = 0
        
        self.score = games.Text(value = 0,
                                                    size = 30,
                                                   color = color.white,
                                                   top = 5,
                                                   right = games.screen.width - 10,
                                                   is_collideable = False)
        games.screen.add(self.score)
        #Create player's ship
        self.ship = Ship(games = self,
                                       x = games.screen.width/2,
                                       y = games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        games.music.load("sounds/gamenoise.mp3")
        games.music.play(-1)

        bg_img = games.load_image("images/background.jpg")
        games.screen.background = bg_img

        self.advance()
        

        games.screen.mainloop()

    def advance(self):
        self.level += 1
        #Amount of space around ship to preserve when creating asteroids
        BUFFER = 150

         #Create Objects
        for i in range(self.level):
            #Calculate an x and y at least BUFFER distance from the ship
            #Choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            #Choose distance along x-axis and y-axis based on minimum distance
            x = random.randrange(games.screen.width)
            y = random.randrange(games.screen.height)
            #Calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            #Wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height
            
            new_asteroid = Asteroid(game = self, x = x, y = y , size = Asteroids.LARGE)
            games.screen.add(new_asteroid)

        #display level number
        level_message = games.Message(value = "Level" + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        #Play new level sound (except at first level)
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game."""
        #Show 'Game Over' for 5 seconds
        end_message = games.Message(value = "Game Over",
                                    size = 90, color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)

class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width
            
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
            
    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        """Check for overlapping sprites."""
        super(Collider, self).update()
        
    #check if missile overlaps any other object
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
    def die(self):
        #Create explosion
        new_explosion = Explosion(obj_x = self.x, obj_y = self.y)
        #Add to screen
        games.screen.add(new_explosion)
        self.destroy()

    
class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/Asteroid_small.png"),
                      MEDIUM : games.load_image("images/Asteroid_med.png"),
                      LARGE : games.load_image("images/Asteroid_big.png")}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self,game, x, y, size):
        Asteroid.total += 1
        super(Asteroid,self).__init__(image = Asteroid.images[size],
                                      x = x,
                                      y = y,
                                      dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                      dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        self.size = size
        self.game = game

       
    def die(self):
        # If asteroid isn't small, replace with two smaller asteroids
        Asteroid.total -= 1
        #ADD TO SCORE
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10
        
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                                            x = self.x,
                                                            y = self.y,
                                                            size = self.size - 1)
                games.screen.add(new_asteroid)
        
        if Asteroid.total == 0:
            self.game.advance()
        super(Asteroid, self).die()

class Ship(Collider):
    image = games.load_image("images/spaceship.png")
    sound = games.load_sound("sounds/thrusters.wav")
    
    ROTATION_STEP = 7
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        
                                  
        self.missile_wait = 0

    def update(self):
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
            
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+= Ship.ROTATION_STEP
            
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            
        if self.missile_wait >0:
            self.missile_wait -= 1
            
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """Destroy ship and end the game"""
        self.game.end()
        super(Ship, self).die()
            


class Missile(Collider):
    image = games.load_image("images/missile.PNG", transparent = True)
    sound = games.load_sound("sounds/missileExplosion.wav")
    BUFFER = 60
    VELOCITY_FACTOR = 10
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180



        # Calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image = Missile.image,
                                                        x = x,
                                                        y = y,
                                                        dx = dx,
                                                        dy = dy)

        self.lifetime = Missile.LIFETIME
        self.angle = ship_angle
        
    def update(self):
        super(Missile, self).update()
        #If lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime ==0:
            self.destroy()
        
class Explosion(games.Animation):
    sound = games.load_sound("sounds/shipExplosion.wav")
    exp_images = ["images/explosion1.bmp",
                        "images/explosion2.bmp",
                        "images/explosion3.bmp",
                        "images/explosion4.bmp",
                        "images/explosion5.bmp"]

    def __init__(self, obj_x, obj_y):
        super(Explosion, self).__init__(images = Explosion.exp_images,
                                        x = obj_x, y = obj_y,
                                        repeat_interval = 4,
                                        n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()


#Main
def main(Game):
    asteroids = Game()
    asteroids.play()
main(Game)
    



   

    #Create Ship
    
    #shot = Missile(100, 100, 0)



    #Draw Objects
    
    



    #Game Setup





    #Start main loop
    



        

