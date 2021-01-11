import pygame as pg
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Sladoled obojen")
prozor.fill(pg.Color("white"))
#KUGLA SLADOLEDA
pg.draw.circle(prozor, pg.Color("yellow"), (201, 130), 53)
#OBOD KORNETA ISPUNJEN BRAON BOJOM
pg.draw.rect(prozor, pg.Color("brown"), (150, 140, 101, 11))
#KONTURA OBODA KORNETA
pg.draw.rect(prozor, pg.Color("black"), (150, 140, 101, 11), 2)
#KORNET ISPUNJEN NARANDŽASTOM BOJOM
temenaTrougla = ((150,150), (200,300),(250,150))
pg.draw.polygon(prozor, pg.Color("orange"), temenaTrougla)
#KONTURA KORNETA
pg.draw.polygon(prozor, pg.Color("black"), temenaTrougla, 2)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


