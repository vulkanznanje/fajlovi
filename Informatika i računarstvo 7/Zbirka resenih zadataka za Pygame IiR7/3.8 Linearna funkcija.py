#Nacrtaj koordinatni sistem i u njemu crvenu liniju koja prikazuje
#linearnu funkciju

import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Linearna funkcija")
prozor.fill(pygame.Color("white"))
pygame.draw.line(prozor,pygame.Color("black"),(200,0),(200,400),5)
pygame.draw.line(prozor,pygame.Color("black"),(0,200),(400,200),5)
pygame.draw.line(prozor,pygame.Color("red"),(0,400),(400,0),5)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


