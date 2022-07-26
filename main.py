# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
from audioop import cross
import pygame, sys, math
from pygame.locals import *

#Projectile Class

screen_width = 1000
screen_height= 1000
class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        origin = (20, 20)
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = origin
        self.xvel = 0
        self.yvel = 0
        self.fired = False
    def update(self, dt):
        self.rect.center = (self.rect.center[0] + self.xvel * dt, self.rect.center[1] + self.yvel * dt)
        if self.rect.center[0] > screen_width or self.rect.center[1] > screen_height:
            self.__init__()
    def fire(self):
        self.fired = True
        mouse_mag = math.sqrt(pygame.mouse.get_pos()[0]**2 + pygame.mouse.get_pos()[1]**2)
        self.xvel = pygame.mouse.get_pos()[0] / mouse_mag
        self.yvel = pygame.mouse.get_pos()[1] / mouse_mag
    
# Crosshair class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("crosshair.png"), (50,50))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
            

# Initialize Objects
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

projectile = Projectile()
projectile_group = pygame.sprite.Group()
projectile_group.add(projectile)

#Main function
def main():
    #Initialize and set cursor invisible
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    #Initialize Display
    DISPLAY=pygame.display.set_mode((screen_width, screen_height))
 
    # Main Loop
    while True:
        # check for events
        for event in pygame.event.get():
            # quit if quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if projectile.fired == False:
                    projectile.fire()

        dt = clock.tick(60)
        #Update screen fill and sprite groups
        DISPLAY.fill("black")
        crosshair_group.draw(DISPLAY)
        crosshair_group.update()
        projectile_group.draw(DISPLAY)
        projectile_group.update(dt)
        pygame.display.update()
        

main()