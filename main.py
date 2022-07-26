# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
from audioop import cross
import pygame, sys
from pygame.locals import *

#Projectile Class
class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

# Crosshair class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("crosshair.png"), (50,50))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
      
# Initialize Crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Main function
def main():
    #Initialize and set cursor invisible
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    #Initialize Display
    DISPLAY=pygame.display.set_mode((1000,1000))
 
    # Main Loop
    while True:
        # check for events
        for event in pygame.event.get():
            # quit if quit
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        #Update screen fill and sprite groups
        DISPLAY.fill("black")
        crosshair_group.draw(DISPLAY)
        crosshair_group.update()
        pygame.display.update()
        dt = clock.tick(60)

main()