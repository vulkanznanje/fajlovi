import pygame
import random
pygame.init()
s = 500
v = 50
prozor = pygame.display.set_mode((s, v))
pygame.display.set_caption("Niz raznobojnih duži sa razmakom")
prozor.fill(pygame.Color("white"))
praznine = 30
sredina = v // 2
x = 0
while x < s:
        boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(prozor, boja, (x, sredina), (x + praznine, sredina), 5)
        x = x + 2 * praznine
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()






