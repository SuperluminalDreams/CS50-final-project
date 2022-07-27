# To make a level, make bodies, add them to a body group and then run main.main(body_group, probe origin)

import main, pygame

planet = main.Body("images/planet_terra.png", 0.5, 850, 500)
planet2 = main.Body("images/planet_jungle.png", 0.65, 1200, 600)

body_group = pygame.sprite.Group()
body_group.add(planet)
body_group.add(planet2)

main.main(body_group, (200, 500))