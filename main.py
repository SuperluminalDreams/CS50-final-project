# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
from audioop import cross
from types import NoneType
import pygame, sys, math
from pygame.locals import *

# global constants
# initial velocity constant
vel_const = 0.6
#gravitational constant
g = 50

#Projectile Class

screen_width = 1920
screen_height= 1080
class Projectile(pygame.sprite.Sprite):
    # Initializes projectile at some point on screen with zero velocity
    def __init__(self):
        self.origin = (20, 100)
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/crosshair.png"), (50,50))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = self.origin

        self.xvel = 0
        self.yvel = 0
        self.fired = False
    # updates position based on velocity, resets if offscreen    
    def update(self, dt):
        self.rect.center = (self.rect.center[0] + self.xvel * dt, self.rect.center[1] + self.yvel * dt)
        if self.rect.center[0] > screen_width or self.rect.center[0] < 0 or self.rect.center[1] > screen_height or self.rect.center[1] < 0:
            self.__init__()
        # add "if hits body"
    # Fire sets initial velocity toward crosshair        
    def fire(self):
        #velocity constant
        self.fired = True
        mouse_mag = math.sqrt(pygame.mouse.get_pos()[0]**2 + pygame.mouse.get_pos()[1]**2)
        self.xvel = vel_const  * (pygame.mouse.get_pos()[0] - self.origin[0]) / mouse_mag
        self.yvel = vel_const * (pygame.mouse.get_pos()[1] - self.origin[1]) / mouse_mag
    
# Crosshair class - simple crosshair that replaces cursor
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/crosshair.png"), (50,50))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# Body Class
class Body(pygame.sprite.Sprite):
    def __init__(self, image, mass, xpos, ypos):
        super().__init__()
        # mass -> size of planet
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (int((self.image.get_height()) * mass), (self.image.get_width()) * mass))

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.mass = mass
        self.rect.center = (xpos, ypos)
    def update(self, projectile, dt):
        #calculate acceleration due to gravity
        self.xdist = self.rect.center[0] - projectile.rect.center[0]
        self.ydist = self.rect.center[1] - projectile.rect.center[1]
        self.dist = math.sqrt(self.xdist**2 + self.ydist**2)
        #apply gravity to projectile
        self.ax = g * (self.mass * self.xdist) / self.dist**3
        self.ay = g * (self.mass * self.ydist) / self.dist**3
        #check if projectile is fired before exerting gravity
        if projectile.fired:
            projectile.xvel += self.ax * dt
            projectile.yvel += self.ay * dt 
            

# Initialize Objects
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

projectile = Projectile()
projectile_group = pygame.sprite.Group()
projectile_group.add(projectile)

planet = Body("images/planet_terra.png", 0.75, 300, 500)
planet2 = Body("images/planet_jungle.png", 1, 1500, 500)
body_group = pygame.sprite.Group()
body_group.add(planet)
body_group.add(planet2)

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
        body_group.draw(DISPLAY)
        body_group.update(projectile, dt)
        crosshair_group.draw(DISPLAY)
        crosshair_group.update()
        projectile_group.draw(DISPLAY)
        projectile_group.update(dt)
        pygame.display.update()
        # check collision
        if pygame.sprite.spritecollide(projectile, body_group, False, pygame.sprite.collide_mask):
            projectile.__init__()
        
main()