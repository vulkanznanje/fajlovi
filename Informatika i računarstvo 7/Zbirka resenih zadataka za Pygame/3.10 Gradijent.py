#Podeli Pygame prozor na 10 delova i naprvi gradijent
#od nasumično izabranih boja

import pygame as pg
import random
pg.init()
(s, v) = (400,400)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Gradijent")
def nasumicnaBoja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
brojNijansi = 10
sirinaPolja = s//10
visinaPolja = v
(r1, g1, b1) = nasumicnaBoja()
(r2, g2, b2) = nasumicnaBoja()
for i in range(0, brojNijansi):
    r = round(r1 + i*(r2 - r1)/brojNijansi)
    g = round(r1 + i*(r2 - r1)/brojNijansi)
    b = round(b1 + i*(b2 - b1)/brojNijansi)
    pg.draw.rect(prozor, (r, b, g), (sirinaPolja*i, 0, sirinaPolja, v))
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()



