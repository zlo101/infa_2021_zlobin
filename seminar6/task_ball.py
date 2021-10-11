import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 800))

# creating an array of colors for circles:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """draws a new circle and puts its coordinates and radius into global variables x, y & r"""
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click_ind(action):
    """
    indicates if the click happened within the circle
    :param action: the event of the mouse click
    """
    x_mouse, y_mouse = action.pos[0], action.pos[1]
    x_circle, y_circle, r_circle = x, y, r

    if (x_mouse - x_circle) ** 2 + (y_mouse - y_circle) ** 2 <= r_circle ** 2:
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# setting the scores as zeros:
hit, miss = 0, 0

while not finished:
    clock.tick(FPS)
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and click_ind(event) is True:
            clicked = True
            hit += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and click_ind(event) is False:
            clicked = True
            miss += 1
    if clicked is False:
        miss += 1

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

# showing the result:
print('You have hit: {}. And you have missed: {}'.format(hit, miss))

pygame.quit()
