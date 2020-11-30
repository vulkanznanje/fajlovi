import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Pygame!")
prozor.fill(pygame.Color("white"))
pygame.draw.circle(prozor, pygame.Color("green"),(200, 70), 60)
pygame.draw.circle(prozor, pygame.Color("purple"), (155, 125), 60)
temena3 = (250, 100), (280,10),(300,10),(270,100)
pygame.draw.polygon(prozor, pygame.Color("brown"),temena3)
pygame.draw.circle(prozor, pygame.Color("yellow"), (245, 125), 60)
pygame.draw.rect(prozor, pygame.Color("black"), (100, 150, 200, 15),2)
pygame.draw.rect(prozor, pygame.Color("brown"), (102, 152, 197, 14))
temena1 = (100, 165), (200,350),(300,165)
temena2 = (103, 167), (200,346),(297,167)
pygame.draw.polygon(prozor, pygame.Color("black"),temena1, 2)
pygame.draw.polygon(prozor, pygame.Color("orange"),temena2)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


