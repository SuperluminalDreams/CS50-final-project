# To make a level, make bodies, add them to a body group and then run main.main(body_group, probe origin)

import main, pygame

# create plaentsd
planet = main.Body("images/planet_terra.png", 0.5, 850, 500)
planet2 = main.Body("images/planet_jungle.png", 0.65, 1200, 600)

# put them in a group
body_group = pygame.sprite.Group()
body_group.add(planet)
body_group.add(planet2)

# run main with group, desired origin
main.main(body_group, (200, 500))