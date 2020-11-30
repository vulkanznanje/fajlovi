import pygame
pygame.init()

prozor = pygame.display.set_mode((300,200))
pygame.display.set_caption("Crtanje duži")
prozor.fill(pygame.Color("White"))

pygame.draw.line(prozor, pygame.Color("Blue"), (50, 100), (250, 100), 5)
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()

