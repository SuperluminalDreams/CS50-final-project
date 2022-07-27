# To make a level, make bodies, add them to a body group and then run main.main(body_group, probe origin)

import main, pygame

planet = main.Body("images/planet_rocky.png", 0.6, 1400, 600) 
planet2 = main.Body("images/planet_desert.png", 0.25, 500, 300)
planet3 = main.Body("images/planet_blue.png", 0.4, 700, 800)

body_group = pygame.sprite.Group()
body_group.add(planet)
body_group.add(planet2)
body_group.add(planet3)

main.main(body_group, (150, 500))