import pygame
pygame.init()
prozor = pygame.display.set_mode((300,300))
pygame.display.set_caption("Trougao lines")
prozor.fill(pygame.Color("White"))

#NAREDNA FUNKCIJE CRTA DUŽI IZMEĐU ZADATIH KOORDINATA
pygame.draw.lines(prozor,pygame.Color("Purple"),True,((50,250),(150,50),(250,250)),5)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


