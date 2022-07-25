# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
import pygame, sys
from pygame.locals import *

#Main function
def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400))

    # Check for events, close screen if quit event
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()