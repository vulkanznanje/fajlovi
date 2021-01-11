import pygame as pg
pg.init()
prozor = pg.display.set_mode((462,301))
pg.display.set_caption("Trzalački instrumenti")
prozor.fill(pg.Color("White"))

#promenljiva u kojoj je smeštena slika
slika = pg.image.load("Trzalački instrumenti.png")
#prikaz slike na odabranoj poziciji u prozoru
prozor.blit(slika, (0,0))

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


