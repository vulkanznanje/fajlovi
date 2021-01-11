#uvoz i učitavanje biblioteke Pygame
#i skraćivanje njenog naziva na pg
import pygame as pg
pg.init()

#podešavanje veličine prozora za crtanje na 300x200 px
prozor = pg.display.set_mode((300,200))
#promena naziva prozora u "Crtanje duži"
pg.display.set_caption("Crtamo oblike")
#promena boje pozadine prozora u belu
prozor.fill(pg.Color("White"))

#crtanje 1 duži plave boje sa zadatim koordinatama i debljinom
pg.draw.line(prozor, pg.Color("Blue"), (50, 100), (250, 100), 5)
#osvežavanje sadržaja prozora tj. prikaz crteža
pg.display.update()

#beskonačna petlja koja se prekida jedino kada se desi događaj
#zatvaranje prozora klikom na dugme X u naslovnoj liniji
while pg.event.wait().type != pg.QUIT:
    pass

#isključivanje biblioteke Pygame i zatvaranje prozora
pg.quit()


