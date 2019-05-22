import pygame, sys, random
from pygame.locals import *
from superwires import games
pygame.init()

screen = pygame.display.set_mode((700, 600), 0, 32)
pygame.display.set_caption("Pong (1 Player)")
clock = pygame.time.Clock()

x = 350
y = 300
paddlelefty = 20
paddlerighty = 20
dx = random.randint(-7, -5)
dy = random.randint(5, 7)
pscore = 0
aiscore = 0

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(message, x, y, size, font, color):
    fontObj = pygame.font.Font(font, size)
    textSurfaceObj = fontObj.render(message, True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)

    screen.blit(textSurfaceObj, textRectObj)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        paddlelefty -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        paddlelefty += 5

    if paddlerighty < y - 50:
        paddlerighty += 5
    if paddlerighty > y - 50:
        paddlerighty -= 5

    if paddlelefty < 0:
        paddlelefty = 0
    if paddlelefty > 500:
        paddlelefty = 500

    if paddlerighty < 0:
        paddlerighty = 0
    if paddlerighty > 500:
        paddlerighty = 500

    if x < 0:
        x = 350
        y = 300
        aiscore += 1
    if x > 685:
        x = 350
        y = 300
        pscore += 1
        
    if pscore >=10:
        print("Congratulations! You have won the game")
        quit()
    if aiscore>=10:
        print("You aren't very good at this game")
        quit()
    screen.fill((0, 0, 0))

    puck = pygame.draw.rect(screen, (0,255, 0), pygame.Rect(x, y, 15, 15))
    paddleleft = pygame.draw.rect(screen, (0, 0, 255
                                           ), pygame.Rect(20, paddlelefty, 20, 100))
    paddleright = pygame.draw.rect(screen, (255,0, 0), pygame.Rect(660, paddlerighty, 20, 100))

    message_to_screen("Score: " + str(pscore), 95, 25, 25, "freesansbold.ttf", (255, 255, 255))
    message_to_screen("Score: " + str(aiscore), 600, 25, 25, "freesansbold.ttf", (255, 255, 255))

    x += dx
    y += dy

    if y < 0:
        dy = -dy
    if y > 585:
        dy = -dy

    if x < 40 and x > 20 and y < paddlelefty+100 and y > paddlelefty:
        dx = -dx
    if x < 680-15 and x > 660-15 and y < paddlerighty+100 and y > paddlerighty:
        dx = -dx

##    sound = games.music.load("sound/soundtrack.mp3")
##    sound.play()

    pygame.display.update()
    clock.tick(60)


