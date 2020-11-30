import pygame as pg
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Koncentrične kružnice")
prozor.fill(pg.Color("White"))
#KOORDINATE CENTRA KRUŽNICA SE POSTAVLJAJU U CENTAR PROZORA
(x,y) = (s//2,v//2)
#BROJAČ PETLJE UZIMA VREDNOSTI OD 10 DO 100 SA KORAKOM 20
for r in range(10,100,20):
    pg.draw.circle(prozor, pg.Color("Black"), (x,y), r, 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()






