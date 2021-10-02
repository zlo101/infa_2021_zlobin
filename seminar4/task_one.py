import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (224, 224, 224), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 3)

circle(screen, (255, 0, 0), (160, 175), 20)   # left eye _change_
circle(screen, (0, 0, 0), (160, 175), 20, 2)

circle(screen, (0, 0, 0), (160, 175), 10)

circle(screen, (255, 0, 0), (240, 175), 15)   # right eye _change_
circle(screen, (0, 0, 0), (240, 175), 15, 2)

circle(screen, (0, 0, 0), (240, 175), 7)

rect(screen, (0, 0, 0), (150, 240, 100, 20))

polygon(screen, (0, 0, 0), [(190, 175), (190 + 10, 175 - 12), (190 + 10 - 90, 175 - 12 - 40),
                            (190 + 10 - 90 -10, 175 - 12 - 40 + 12)])
polygon(screen, (0, 0, 0), [(220, 165), (220 - 5, 165 - 10), (220 - 5 + 90, 165 - 10 - 30),
                            (220 - 5 + 90 + 5, 165 - 10 - 30 + 10)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
