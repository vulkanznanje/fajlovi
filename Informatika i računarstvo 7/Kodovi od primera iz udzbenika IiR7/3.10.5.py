import pygame as pg
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Mreža")
prozor.fill(pg.Color("white"))
#BROJ PODELA PO HORIZONTALI I VERTIKALI
brPodela = 10
#RAZMACI IZMEĐU LINIJA
x = s//brPodela
y = v//brPodela
for i in range(1,brPodela):
    #VERTIKALNE LINIJE
    pg.draw.line(prozor, pg.Color("red"), (i*x, 0), (i*x, v), 3)
    #HORIZONTALNE LINIJE
    pg.draw.line(prozor, pg.Color("red"), (0, i*y), (s, i*y), 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()








