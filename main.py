# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
import pygame, sys
from pygame.locals import *

#Main function
def main():
    pygame.init()

    #initialize display and launching point
    launch_center = (30, 470)
    DISPLAY=pygame.display.set_mode((500,500))
    launch_point = pygame.draw.circle(DISPLAY, (255, 0, 0), launch_center, 5)
    
    
    # Always loop
    while True:
        mouse_pos = pygame.mouse.get_pos()
        #use dirty rect method with blits here to move a crosshair to mouse location
        pygame.display.update()

        # check for events
        for event in pygame.event.get():
            # quit if quit
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

main()