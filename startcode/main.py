import pygame, sys
#from pygame.examples.video import backgrounds
from pygame.locals import QUIT
kleur = (0,0,0)
pygame.init()
venster = pygame.display.set_mode((999, 300))
venster.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.draw.circle(venster,  kleur, pygame.mouse.get_pos(),6)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                kleur = (255,0,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                kleur = (0,0,0)
    if pygame.mouse.get_pressed() == (False, False, True):
        pygame.draw.circle(venster, (255,255,255), pygame.mouse.get_pos(), 6)
    pygame.display.update()

