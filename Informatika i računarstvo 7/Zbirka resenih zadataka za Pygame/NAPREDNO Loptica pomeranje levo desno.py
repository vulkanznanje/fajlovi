#Nacrtaj narandžasti krug čiji je centar u sredini prozora, a poluprečnik
#iznosi desetinu širine prozora. Omogući da se tasterima sa levom i desnom
#strelicom krug pomera ulevo odnosno udesno.

import pygame as pg, random
pg.init() 
pg.display.set_caption("Pomeranje kruga") 
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
pg.key.set_repeat(50, 25)
(x, y) = (sirina // 2, visina // 2) 
r = sirina//10                              
(dx, dy) = (10, 10)            
def crtanje():
    prozor.fill(pg.Color("white"))                      
    pg.draw.circle(prozor, pg.Color("darkorange"), (x, y), r)
def obradi_dogadjaj(dogadjaj):
    global x, y
    if dogadjaj.type == pg.KEYDOWN:      
        if dogadjaj.key == pg.K_LEFT:    
            x = x - dx                      
            return True                  
        elif dogadjaj.key == pg.K_RIGHT:
            x = x + dx                      
            return True                                           
treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:   
        crtanje()
        pg.display.update()        
        treba_crtati = False
    dogadjaj = pg.event.wait() 
    if dogadjaj.type == pg.QUIT:   
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)
pg.quit()  

