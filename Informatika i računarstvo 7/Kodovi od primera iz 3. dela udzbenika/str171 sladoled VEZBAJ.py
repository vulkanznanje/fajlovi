import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Pygame!")
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("black"), (195, 200, 10, 60),2)
pygame.draw.rect(prozor, pygame.Color("orange"), (197, 201, 7, 58))
temena1 = (170, 200), (177,130),(223,130),(230,200)
temena2 = (177, 130), (185,60),(215,60),(223,130)
pygame.draw.polygon(prozor, pygame.Color("black"),temena1, 2)
pygame.draw.polygon(prozor, pygame.Color("black"),temena2, 2)
pygame.draw.polygon(prozor, pygame.Color("brown"),temena2)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


