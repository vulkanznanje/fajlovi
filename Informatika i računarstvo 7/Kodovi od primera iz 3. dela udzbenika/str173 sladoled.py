import pygame
import math
pygame.init()
prozor = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Pygame!")
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("black"), (100, 150, 200, 15),2)
pygame.draw.arc(prozor, pygame.Color("black"), (99, 81, 108, 108), math.radians(-17),math.radians(200),3)
pygame.draw.arc(prozor, pygame.Color("black"), (195, 81, 108, 108), math.radians(-17),math.radians(155),3)
pygame.draw.arc(prozor, pygame.Color("black"), (150, 40, 108, 108), math.radians(10),math.radians(168),3)
temena = (100, 165), (200,350),(300,165)
pygame.draw.polygon(prozor, pygame.Color("black"),temena, 2)
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


