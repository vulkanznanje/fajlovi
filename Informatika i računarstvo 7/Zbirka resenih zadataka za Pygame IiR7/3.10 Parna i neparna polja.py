#Napisi program koji ce na osnovu vrednosti promenljive brojPolja, nacrtati toliko pravougaonika
#od vrha do dna prozora pri čemu će svaki parni pravougaonik biti crne, a neparni zelene boje.

import pygame as pg
pg.init()
(s,v) = (600,200)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Parna i neparna polja")
brojPolja = 40
sirinaPolja = s//brojPolja
visinaPolja = v
for i in range(0, brojPolja):
    if i%2==0:
        pg.draw.rect(prozor, pg.Color("Green"), (i*sirinaPolja, 0, sirinaPolja, visinaPolja), 0)
    else:
        pg.draw.rect(prozor, pg.Color("Black"), (i*sirinaPolja, 0, sirinaPolja, visinaPolja), 0)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()







