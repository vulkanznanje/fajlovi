import pygame as pg
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Ovčar i Kablar")
prozor.fill(pg.Color("skyblue")) #NEBO
#SUNCE
pg.draw.circle(prozor, pg.Color("yellow"), (300, 80), 70)
#OBLAK
pg.draw.circle(prozor, pg.Color("white"), (250, 150), 60)
pg.draw.circle(prozor, pg.Color("white"), (195, 150), 35)
pg.draw.circle(prozor, pg.Color("white"), (305, 150), 35)
#OVČAR
temena1 = ((0,400), (125,200), (275,400))
pg.draw.polygon(prozor, pg.Color("darkgreen"), temena1)
#KABLAR
temena2 = ((150,400), (280,270), (400,400))
pg.draw.polygon(prozor, pg.Color("darkgreen"), temena2)
#REPETITOR
pg.draw.line(prozor, pg.Color("black"), (125, 202),(125, 160), 2)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()



