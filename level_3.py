# To make a level, make bodies, add them to a body group and then run main.main(body_group, probe origin)

import main, pygame

planet = main.Body("images/planet_rocky.png", 0.41, 300, 300)
planet2 = main.Body("images/planet_desert.png", 0.49, 300, 700)
planet3 = main.Body("images/planet_blue.png", 0.42, 1500, 300)
planet4 = main.Body("images/planet_terra.png", 0.53, 1500, 700)

body_group = pygame.sprite.Group()
body_group.add(planet)
body_group.add(planet2)
body_group.add(planet3)
body_group.add(planet4)

main.main(body_group, (900, 500))