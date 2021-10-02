import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30


def screen_creator(x):
    # creates the screen and fills in the background

    the_screen = pygame.display.set_mode((x, round(1.5 * x)))
    y = round(1.5 * x)
    rect(the_screen, (230, 230, 230), (0, 0, x, round(0.4 * y)))
    rect(the_screen, (255, 255, 255), (0, round(0.4 * y), x, y - round(0.4 * y)))

    return the_screen


def ellipse_rotation(dx, dy, width, ind, color):
    # the indicator is used to indicate in what direction to rotate

    # ellipse features:
    length = round(math.sqrt(dx ** 2 + dy ** 2))
    angle = math.atan(dy / dx) * 180 / math.pi

    # drawing an ellipse on a new surface:
    new_surface = pygame.Surface((length, width))
    new_surface.set_colorkey((0, 0, 0))
    ellipse(new_surface, color, (0, 0, length, width))

    # rotating the plane by the given angle:
    if ind == 1:
        new_surface = pygame.transform.rotate(new_surface, angle)
    elif ind == -1:
        new_surface = pygame.transform.rotate(new_surface, 2 * math.pi - angle)
    return new_surface


def human(x, y, dx):
    # draws a human in a rectangular frame with the starting point in (x, y), the width being dx, and the height dy

    # finding the value of dy through dx:
    dy = round(1.19 * dx)

    # hood
    ellipse(screen, (227, 222, 219), (x + round(0.2 * dx), y, round(0.6 * dx), round(dy * 0.36)))

    # torso and limbs
    color = (145, 124, 111)
    ellipse(screen, color, (x + round(0.16 * dx), y + round(0.25 * dy), round(0.68 * dx), round(1.12 * dy)))
    rect(screen, (255, 255, 255), (x + round(0.16 * dx), y + round(0.81 * dy), round(0.68 * dx), round(0.57 * dy)))
    ellipse(screen, color, (x, y + round(0.4 * dy), round(0.4 * dx), round(0.1 * dy)))
    screen.blit(ellipse_rotation(round(0.4 * dx), round(0.15 * dy), round(0.1 * dy), -1, color),
                (x + round(0.55 * dx), y + round(0.37 * dy)))
    ellipse(screen, color, (x + round(0.3 * dx), y + round(0.7 * dy), round(0.19 * dx), round(0.28 * dy)))
    ellipse(screen, color, (x + round(0.51 * dx), y + round(0.7 * dy), round(0.19 * dx), round(0.28 * dy)))
    ellipse(screen, color, (x + round(0.22 * dx), y + round(0.9 * dy), round(0.2 * dx), round(0.1 * dy)))
    ellipse(screen, color, (x + round(0.58 * dx), y + round(0.9 * dy), round(0.2 * dx), round(0.1 * dy)))

    # stuff on the torso
    rect(screen, (108, 93, 83), (x + round(0.41 * dx), y + round(0.28 * dy), round(0.18 * dx), round(0.48 * dy)))
    rect(screen, (108, 93, 83), (x + round(0.16 * dx), y + round(0.75 * dy), round(0.68 * dx), round(0.06 * dy)))

    # face
    ellipse(screen, (172, 157, 147), (x + round(0.27 * dx), y + round(0.06 * dy), round(0.46 * dx), round(0.26 * dy)))
    ellipse(screen, (227, 219, 219), (x + round(0.34 * dx), y + round(0.12 * dy), round(0.32 * dx), round(0.18 * dy)))
    line(screen, (72, 70, 70), (x + round(0.364 * dx), y + round(0.16 * dy)),
         (x + round(0.364 * dx) + round(0.091 * dx), y + round(0.16 * dy) + round(0.028 * dy)))
    line(screen, (72, 70, 70), (x + round(0.523 * dx), y + round(0.192 * dy)),
         (x + round(0.523 * dx) + round(0.091 * dx), y + round(0.192 * dy) - round(0.028 * dy)))
    line(screen, (72, 70, 70), (x + round(0.43 * dx), y + round(0.24 * dy)),
         (x + round(0.43 * dx) + round(0.18 * dx), y + round(0.24 * dy)))

    # stick in left hand
    line(screen, (4, 4, 4), (x + round(0.08 * dx), y), (x + round(0.14 * dx), y + round(0.92 * dy)))
    return None


def cat(x, y, dx):
    # draws a cat in a rectangular frame with the starting point in (x, y), the width being dx, and the height dy.

    # finding the value of dy through dx:
    dy = round(0.333 * dx)

    # colors
    color_1 = (204, 204, 204)  # the fur
    color_2 = (147, 172, 167)  # the fish's scales
    color_3 = (255, 255, 255)  # white
    color_4 = (0, 0, 0)  # black
    color_5 = (211, 95, 95)  # the fish's fins

    # the torso with limbs:
    ellipse(screen, color_1, (x + round(0.152 * dx), y + round(0.318 * dy), round(0.508 * dx), round(0.327 * dy)))
    screen.blit(ellipse_rotation(round(0.372 * 0.9 * dx), round(0.473 * 0.9 * dy), round(0.2 * dy), 1, color_1),
                (x + round(0.6 * dx), y))
    screen.blit(ellipse_rotation(round(0.254 * dx), round(0.364 * dy), round(0.14 * dy), -1, color_1),
                (x + round(0.58 * dx), y + round(0.455 * dy)))
    screen.blit(ellipse_rotation(round(0.254 * dx), round(0.455 * dy), round(0.14 * dy), -1, color_1),
                (x + round(0.508 * dx), y + round(0.5 * dy)))
    screen.blit(ellipse_rotation(round(0.338 * dx), round(0.273 * dy), round(0.14 * dy), 1, color_1),
                (x + round(0.054 * dx), y + round(0.518 * dy)))
    screen.blit(ellipse_rotation(round(0.302 * dx), round(0.182 * dy), round(0.14 * dy), 1, color_1),
                (x, y + round(0.436 * dy)))

    # the fish:
    f1x, f1y = x + round(0.12203 * dx), y + round(0.2818 * dy)
    polygon(screen, color_5, [(f1x, f1y), (f1x - round(0.0136 * dx), f1y + round(0.0545 * dy)),
                              (f1x + round(0.061 * dx), f1y + round(0.191 * dy)),
                              (f1x + round(0.0406 * dx), f1y + round(0 * dy))])
    f2x, f2y = x + round(0.1355 * dx), y + round(0.15 * dy)
    polygon(screen, color_5, [(f2x, f2y), (f2x + round(0.0237 * dx), f2y + round(0.0909 * dy)),
                              (f2x + round(0.0542 * dx), f2y + round(0.109 * dy)),
                              (f2x + round(0.0677 * dx), f2y + round(0.036 * dy))])
    screen.blit(ellipse_rotation(round(0.17 * dx), round(0.275 * dy), round(0.14 * dy), -1, color_2),
                (x + round(0.0916 * dx), y + round(0.164 * dy)))
    tx, ty = x + round(0.249 * dx), y + round(0.4181 * dy)
    polygon(screen, color_2, [(tx, ty), (tx + round(0.0779 * dx), ty + round(0 * dy)),
                              (tx + round(0.0508 * dx), ty + round(0.118 * dy))])
    circle(screen, (0, 1, 253), (x + round(0.1254 * dx), y + round(0.256 * dy)), round(0.01356 * dy))
    circle(screen, color_4, (x + round(0.1254 * dx), y + round(0.256 * dy)), round(0.00678 * dy))

    # the face:
    line(screen, color_3, (x + round(0.176 * dx), y + round(0.272 * dy)),
         (x + round(0.176 * dx), y + round(0.37 * dy)), 2)
    line(screen, color_3, (x + round(0.21 * dx), y + round(0.318 * dy)),
         (x + round(0.21 * dx), y + round(0.42 * dy)), 2)
    ellipse(screen, color_1, (x + round(0.16 * dx), y + round(0.1 * dy), round(0.16 * dx), round(0.3 * dy)))
    circle(screen, color_4, (x + round(0.2 * dx), y + round(0.269 * dy)), round(0.01017 * dy))
    ellipse(screen, color_3, (x + round(0.195 * dx), y + round(0.12 * dy), round(0.03 * dx), round(0.08 * dy)))
    ellipse(screen, color_3, (x + round((0.25 - 0.009) * dx), y + round((0.156 + 0.03) * dy),
                              round(0.03 * dx), round(0.08 * dy)))
    circle(screen, color_4, (x + round(0.215 * dx), y + round(0.156 * dy)), round(0.01017 * dy))
    circle(screen, color_4, (x + round((0.275 - 0.009) * dx), y + round((0.192 + 0.03) * dy)), round(0.01017 * dy))

    # ears:
    x_1, y_1 = x + round(0.21 * dx), y + round(0.0909 * dy)
    x_2, y_2 = x + round(0.278 * dx), y + round(0.1 * dy)
    polygon(screen, color_1, [(x_1, y_1 + round(0.018 * dy)), (x_1 + round(0.0338 * dx), y_1 + round(0 * dy)),
                              (x_1 + round(0.013 * dx), y_1 - round(0.0636 * dy))])
    polygon(screen, color_1, [(x_2, y_2 + round(0.018 * dy)), (x_2 + round(0.0339 * dx), y_2 + round(0.0909 * dy)),
                              (x_2 + round(0.0237 * dx), y_2 - round(0.0545 * dy))])
    return None


def find_xcoord_on_ellipse(ycoord, cx, cy, a, b):
    # (cx, cy) are the coordinates of the ellipse's center
    # a, b are the half height and half width of the ellipse
    # ycoord is the knows y-coordinate of a point on the ellipse
    return cx - round(a * math.sqrt(1 - ((ycoord - cy) / b) ** 2))


def ice_house(x, y, dx):
    # finding the value of dy through dx:
    dy = round(0.9 * dx)

    ellipse(screen, (230, 230, 230), (x, y, dx, dy))
    arc(screen, (2, 2, 2), (x, y, dx, dy), 0, math.pi + 1, 4)
    rect(screen, (255, 255, 255), (x, round(y + 0.5 * dy), dx, round(0.51 * dy)))
    line(screen, (2, 2, 2), (x, y + 0.5 * dy), (x + dx, y + 0.5 * dy), 2)

    # horizontal lines between the snow blocks:
    cx, cy = x + dx / 2, y + dy / 2
    line(screen, (77, 77, 77), (find_xcoord_on_ellipse(y + round(dy / 8), cx, cy, dx / 2, dy / 2), y + round(dy / 8)),
         ((-1) * find_xcoord_on_ellipse(y + round(dy / 8), cx, cy, dx / 2, dy / 2) + 2 * cx, y + round(dy / 8)), 1)
    line(screen, (77, 77, 77), (find_xcoord_on_ellipse(y + round(dy / 4), cx, cy, dx / 2, dy / 2), y + round(dy / 4)),
         ((-1) * find_xcoord_on_ellipse(y + round(dy / 4), cx, cy, dx / 2, dy / 2) + 2 * cx, y + round(dy / 4)), 1)
    line(screen, (77, 77, 77), (find_xcoord_on_ellipse(y + round(3 * dy / 8), cx, cy, dx / 2, dy / 2),
                                y + round(3 * dy / 8)),
         ((-1) * find_xcoord_on_ellipse(y + round(3 * dy / 8), cx, cy, dx / 2, dy / 2) + 2 * cx,
          y + round(3 * dy / 8)), 1)

    # vertical lines between the snow blocks:
    line(screen, (77, 77, 77), (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.25 * dx), y + round(dy / 8)), 1)
    line(screen, (77, 77, 77), (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.54 * dx), y + round(dy / 8)), 1)
    line(screen, (77, 77, 77), (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.7 * dx), y + round(dy / 8)), 1)

    line(screen, (77, 77, 77), (x + round(0.3 * dx), y + round(dy / 8)), (x + round(0.25 * dx), y + round(dy / 4)), 1)
    line(screen, (77, 77, 77), (x + round(0.46 * dx), y + round(dy / 8)), (x + round(0.43 * dx), y + round(dy / 4)), 1)
    line(screen, (77, 77, 77), (x + round(0.59 * dx), y + round(dy / 8)), (x + round(0.62 * dx), y + round(dy / 4)), 1)
    line(screen, (77, 77, 77), (x + round(0.7 * dx), y + round(dy / 8)), (x + round(0.75 * dx), y + round(dy / 4)), 1)

    line(screen, (77, 77, 77), (x + round(0.15 * dx), y + round(dy / 4)), (x + round(0.12 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, (77, 77, 77), (x + round(0.3 * dx), y + round(dy / 4)),
         (x + round(0.27 * dx), y + round(3 * dy / 8)), 1)
    line(screen, (77, 77, 77), (x + round(0.45 * dx), y + round(dy / 4)), (x + round(0.42 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, (77, 77, 77), (x + round(0.54 * dx), y + round(dy / 4)), (x + round(0.57 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, (77, 77, 77), (x + round(0.68 * dx), y + round(dy / 4)), (x + round(0.75 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, (77, 77, 77), (x + round(0.83 * dx), y + round(dy / 4)),
         (x + round(0.89 * dx), y + round(3 * dy / 8)), 1)

    line(screen, (77, 77, 77), (x + round(0.13 * dx), y + round(3 * dy / 8)), (x + round(0.11 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.26 * dx), y + round(3 * dy / 8)), (x + round(0.23 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.36 * dx), y + round(3 * dy / 8)), (x + round(0.32 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.49 * dx), y + round(3 * dy / 8)), (x + round(0.48 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.63 * dx), y + round(3 * dy / 8)), (x + round(0.65 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.75 * dx), y + round(3 * dy / 8)), (x + round(0.78 * dx), y + round(dy / 2)),
         1)
    line(screen, (77, 77, 77), (x + round(0.87 * dx), y + round(3 * dy / 8)), (x + round(0.91 * dx), y + round(dy / 2)),
         1)
    return None


# drawing:
screen = screen_creator(600)
ice_house(20, 300, 250)
cat(50, 600, 280)
human(350, 400, 200)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
