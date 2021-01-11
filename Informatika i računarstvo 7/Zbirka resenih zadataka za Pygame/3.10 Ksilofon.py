#Ksilofon je udarački instrument koji ima osam pločica gde je svaka naredna
#manja od prethodne (gledano s leva na desno). Pored toga su i različitih boja.
#Pokušaj da u Pygame-u nacrtaš ksilofon.

import pygame
import random
pygame.init()
s = 400
v = 400
prozor = pygame.display.set_mode((s, v))
pygame.display.set_caption("Ksilofon")
prozor.fill(pygame.Color("white"))
broj_plocica = 8
sirina = s//broj_plocica
visina = v//broj_plocica
for i in range(broj_plocica):
    boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(prozor, boja, (i*sirina, i-visina, sirina, v-i*visina+4*broj_plocica))
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()






