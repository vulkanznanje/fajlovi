#Nacrtaj crveni kvadrat rotiran udesno za 45 stepeni
#čija je površina duplo manja od porvršine Pygame prozora.

import pygame
import math
pygame.init()
s = 400
v = 400
prozor = pygame.display.set_mode((s, v))
pygame.display.set_caption("Crveni kvadrat")
prozor.fill(pygame.Color("white"))
(x,y) = (s/2,v/2)
x = round(x)
y = round(y)
a = math.sqrt((s*v)/(2))
a = round(a)
d = a * math.sqrt(2)
d = round(d)
temena = (x-d/2,y),(x,y-d/2),(x+d/2,y),(x,y+d/2)
pygame.draw.polygon(prozor, pygame.Color("red"), temena)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()






