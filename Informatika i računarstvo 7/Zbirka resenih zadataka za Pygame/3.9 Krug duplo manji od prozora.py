#Nacrtaj plavi krug čiji je centar u sredini Pygame prozora i
#čija je površina duplo manja od porvršine prozora.

import pygame
import math
pygame.init()
s = 400
v = 400
prozor = pygame.display.set_mode((s, v))
pygame.display.set_caption("Plavi krug")
prozor.fill(pygame.Color("white"))
(x,y) = (s/2,v/2)
x = round(x)
y = round(y)
r = math.sqrt((s*v)/(2*math.pi))
r = round(r)
pygame.draw.circle(prozor, pygame.Color("blue"), (x,y), r)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()






