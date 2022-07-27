# This is a game about gravity. The player launches a projectile with some initial velocity into a field of bodies; each have some gravity. 
# The goal of the game is to have the have the projectile orbit the bodies for as long as possible before it exits the screen.

# import libraries
from audioop import cross
from types import NoneType
import pygame, sys, math, time
from pygame.locals import *

# gravitational constant
g = 500
# set resolution
screen_width = 1920
screen_height= 1080

#Projectile Class
class Projectile(pygame.sprite.Sprite):
    # Initializes projectile at some point on screen with zero velocity
    def __init__(self, origin):
        self.origin = origin
        super().__init__()
        self.image = pygame.image.load("images/probe.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = self.origin
        # initial velocity constant
        self.vel_const = 0.5

        self.xvel = 0
        self.yvel = 0
        self.fired = False
    # updates position based on velocity, resets if offscreen    
    def update(self, dt):
        self.rect.center = (self.rect.center[0] + self.xvel * dt, self.rect.center[1] + self.yvel * dt)
        if self.rect.center[0] > screen_width + 200 or self.rect.center[0] < -200 or self.rect.center[1] > screen_height + 200 or self.rect.center[1] < -200:
            self.__init__(self.origin)
    # Fire sets initial velocity toward crosshair        
    def fire(self):
        #velocity constant
        self.fired = True
        mouse_mag = math.sqrt(pygame.mouse.get_pos()[0]**2 + pygame.mouse.get_pos()[1]**2)
        self.xvel = self.vel_const  * (pygame.mouse.get_pos()[0] - self.origin[0]) / mouse_mag
        self.yvel = self.vel_const * (pygame.mouse.get_pos()[1] - self.origin[1]) / mouse_mag
        self.t0 = time.time()
    
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
            
#Main function
def main(group, origin=(20,20)):

    # Initialize Objects
    crosshair = Crosshair()
    crosshair_group = pygame.sprite.Group()
    crosshair_group.add(crosshair)

    projectile = Projectile(origin)
    projectile_group = pygame.sprite.Group()
    projectile_group.add(projectile)

    body_group = group

    #Initialize and set cursor invisible
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    #Initialize Display
    DISPLAY=pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Gravity Game")
    font_obj=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25) 

    #initialize timer vars
    t1 = 0
    t0 = 0

    # Main Loop
    while True:
        # check for events
        for event in pygame.event.get():
            # quit if quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # fire probe with mouse
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if projectile.fired == False:
                        t0 = time.time()
                        projectile.fire()
                if event.button == 4:
                    projectile.vel_const += 0.05
                elif event.button == 5:
                    projectile.vel_const -= 0.05

            # press 'r' to reset
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    projectile.__init__(projectile.origin)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        dt = clock.tick(60)
        #Update screen fill and sprite groups
        DISPLAY.fill("black")
        body_group.draw(DISPLAY)
        body_group.update(projectile, dt)
        crosshair_group.draw(DISPLAY)
        crosshair_group.update()
        projectile_group.draw(DISPLAY)
        projectile_group.update(dt)

        #timer for score updates
        if projectile.fired == True:
            t1 = time.time()
        score = t1 - t0


        # Display score and instructions
        score_obj=font_obj.render(f"Flight Time: {round(score, 3)} seconds",True,"white")
        instructions_obj=font_obj.render(f"Click to fire    -   Press \"R\" to reset    -   Press \"Q\" to quit",True,"white")
        velocity_obj=font_obj.render(f"Launch Velocity: {round(projectile.vel_const, 2)}",True,"white")

        DISPLAY.blit(score_obj,(20, 0))
        DISPLAY.blit(instructions_obj, (20, 1000))
        DISPLAY.blit(velocity_obj, (20, 950))
        

        # check collision
        if pygame.sprite.spritecollide(projectile, body_group, False, pygame.sprite.collide_mask):
            projectile.__init__(projectile.origin)
        
        # Update Display
        pygame.display.update()
        