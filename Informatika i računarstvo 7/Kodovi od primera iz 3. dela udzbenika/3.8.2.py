import pygame
pygame.init()
prozor = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Narodna zastava Srbije")
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("red"), (50,50,400,100))
pygame.draw.rect(prozor, pygame.Color("blue"), (50,150,400,100))
pygame.draw.rect(prozor, pygame.Color("white"), (50,250,400,100))
pygame.draw.rect(prozor, pygame.Color("black"), (50,50,400,300), 1)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
