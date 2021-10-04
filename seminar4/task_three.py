import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
# colors
brown = (230, 230, 230)
white = (255, 255, 255)
beige = (204, 204, 204)  # the fur
aquamarine = (147, 172, 167)  # the fish's scales
afro_american_screen_color = (1, 1, 1)
pink = (211, 95, 95)  # the fish's fins
dark_grey = (77, 77, 77)


def screen_creator(x):
    """

    :param x: screen length on x axis
    :return: creates the screen
    """
    # creates the screen and fills in the background

    the_screen = pygame.display.set_mode((x, round(1.5 * x)))
    y = round(1.5 * x)
    rect(the_screen, brown, (0, 0, x, round(0.4 * y)))
    rect(the_screen, white, (0, round(0.4 * y), x, y - round(0.4 * y)))

    return the_screen


def ellipse_rotation(dx, dy, width, ind, color):
    """

    :param dx: semi-major axis
    :param dy: semi-minor axis
    :param width: line width
    :param ind: +1: conterclockwise rotation, -1: clockwise rotation
    :param color:
    :return:
    """
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


def human(x, y, dx, scrn):
    """

    :param x: coordinate on x axis
    :param y: coordinate on y axis
    :param dx: human width
    :param scrn: picks the surface to draw on
    :return: 
    """
    # draws a human in a rectangular frame with the starting point in (x, y), the width being dx, and the height dy

    # finding the value of dy through dx:
    dy = round(1.19 * dx)

    # hood
    ellipse(scrn, (227, 222, 219), (x + round(0.2 * dx), y, round(0.6 * dx), round(dy * 0.36)))

    # torso and limbs
    brown = (145, 124, 111)
    ellipse(scrn, brown, (x + round(0.16 * dx), y + round(0.25 * dy), round(0.68 * dx), round(1.12 * dy)))
    rect(scrn, (255, 255, 255), (x + round(0.16 * dx), y + round(0.81 * dy), round(0.68 * dx), round(0.57 * dy)))
    ellipse(scrn, brown, (x, y + round(0.4 * dy), round(0.4 * dx), round(0.1 * dy)))
    scrn.blit(ellipse_rotation(round(0.4 * dx), round(0.15 * dy), round(0.1 * dy), -1, brown),
              (x + round(0.55 * dx), y + round(0.37 * dy)))
    ellipse(scrn, brown, (x + round(0.3 * dx), y + round(0.7 * dy), round(0.19 * dx), round(0.28 * dy)))
    ellipse(scrn, brown, (x + round(0.51 * dx), y + round(0.7 * dy), round(0.19 * dx), round(0.28 * dy)))
    ellipse(scrn, brown, (x + round(0.22 * dx), y + round(0.9 * dy), round(0.2 * dx), round(0.1 * dy)))
    ellipse(scrn, brown, (x + round(0.58 * dx), y + round(0.9 * dy), round(0.2 * dx), round(0.1 * dy)))

    # stuff on the torso
    rect(scrn, (108, 93, 83), (x + round(0.41 * dx), y + round(0.28 * dy), round(0.18 * dx), round(0.48 * dy)))
    rect(scrn, (108, 93, 83), (x + round(0.16 * dx), y + round(0.75 * dy), round(0.68 * dx), round(0.06 * dy)))

    # face
    ellipse(scrn, (172, 157, 147), (x + round(0.27 * dx), y + round(0.06 * dy), round(0.46 * dx), round(0.26 * dy)))
    ellipse(scrn, (227, 219, 219), (x + round(0.34 * dx), y + round(0.12 * dy), round(0.32 * dx), round(0.18 * dy)))
    line(scrn, (72, 70, 70), (x + round(0.364 * dx), y + round(0.16 * dy)),
         (x + round(0.364 * dx) + round(0.091 * dx), y + round(0.16 * dy) + round(0.028 * dy)))
    line(scrn, (72, 70, 70), (x + round(0.523 * dx), y + round(0.192 * dy)),
         (x + round(0.523 * dx) + round(0.091 * dx), y + round(0.192 * dy) - round(0.028 * dy)))
    line(scrn, (72, 70, 70), (x + round(0.43 * dx), y + round(0.24 * dy)),
         (x + round(0.43 * dx) + round(0.18 * dx), y + round(0.24 * dy)))

    # stick in left hand
    line(scrn, (4, 4, 4), (x + round(0.08 * dx), y), (x + round(0.14 * dx), y + round(0.92 * dy)))
    return None


def human_reflected(x, y, dx):
    human_surface = pygame.Surface((dx, round(1.19 * dx)))
    human_surface.set_colorkey((0, 0, 0))
    human(0, 0, dx, human_surface)
    human_surface = pygame.transform.flip(human_surface, True, False)
    screen.blit(human_surface, (x, y))


def cat(x, y, dx, scrn):
    """

    :param x: coordinate on x axis
    :param y: coordinate on y axis
    :param dx: width
    :param scrn: picks the surface to draw on
    :return: draws a cat
    """
    # draws a cat in a rectangular frame with the starting point in (x, y), the width being dx, and the height dy.

    # finding the value of dy through dx:
    dy = round(0.333 * dx)


    # the torso with limbs:
    ellipse(scrn, beige, (x + round(0.152 * dx), y + round(0.318 * dy), round(0.508 * dx), round(0.327 * dy)))
    scrn.blit(ellipse_rotation(round(0.372 * 0.9 * dx), round(0.473 * 0.9 * dy), round(0.2 * dy), 1, beige),
              (x + round(0.6 * dx), y))
    scrn.blit(ellipse_rotation(round(0.254 * dx), round(0.364 * dy), round(0.14 * dy), -1, beige),
              (x + round(0.58 * dx), y + round(0.455 * dy)))
    scrn.blit(ellipse_rotation(round(0.254 * dx), round(0.455 * dy), round(0.14 * dy), -1, beige),
              (x + round(0.508 * dx), y + round(0.5 * dy)))
    scrn.blit(ellipse_rotation(round(0.338 * dx), round(0.273 * dy), round(0.14 * dy), 1, beige),
              (x + round(0.054 * dx), y + round(0.518 * dy)))
    scrn.blit(ellipse_rotation(round(0.302 * dx), round(0.182 * dy), round(0.14 * dy), 1, beige),
              (x, y + round(0.436 * dy)))

    # the fish:
    f1x, f1y = x + round(0.12203 * dx), y + round(0.2818 * dy)
    polygon(scrn, pink, [(f1x, f1y), (f1x - round(0.0136 * dx), f1y + round(0.0545 * dy)),
                            (f1x + round(0.061 * dx), f1y + round(0.191 * dy)),
                            (f1x + round(0.0406 * dx), f1y + round(0 * dy))])
    f2x, f2y = x + round(0.1355 * dx), y + round(0.15 * dy)
    polygon(scrn, pink, [(f2x, f2y), (f2x + round(0.0237 * dx), f2y + round(0.0909 * dy)),
                            (f2x + round(0.0542 * dx), f2y + round(0.109 * dy)),
                            (f2x + round(0.0677 * dx), f2y + round(0.036 * dy))])
    scrn.blit(ellipse_rotation(round(0.17 * dx), round(0.275 * dy), round(0.14 * dy), -1, aquamarine),
              (x + round(0.0916 * dx), y + round(0.164 * dy)))
    tx, ty = x + round(0.249 * dx), y + round(0.4181 * dy)
    polygon(scrn, aquamarine, [(tx, ty), (tx + round(0.0779 * dx), ty + round(0 * dy)),
                            (tx + round(0.0508 * dx), ty + round(0.118 * dy))])
    circle(scrn, (0, 1, 253), (x + round(0.1254 * dx), y + round(0.256 * dy)), round(0.01356 * dy))
    circle(scrn, afro_american_screen_color, (x + round(0.1254 * dx), y + round(0.256 * dy)), round(0.00678 * dy))

    # the face:
    line(scrn, white, (x + round(0.176 * dx), y + round(0.272 * dy)),
         (x + round(0.176 * dx), y + round(0.37 * dy)), 2)
    line(scrn, white, (x + round(0.21 * dx), y + round(0.318 * dy)),
         (x + round(0.21 * dx), y + round(0.42 * dy)), 2)
    ellipse(scrn, beige, (x + round(0.16 * dx), y + round(0.1 * dy), round(0.16 * dx), round(0.3 * dy)))
    circle(scrn, afro_american_screen_color, (x + round(0.2 * dx), y + round(0.269 * dy)), round(0.01017 * dy))
    ellipse(scrn, white, (x + round(0.195 * dx), y + round(0.12 * dy), round(0.03 * dx), round(0.08 * dy)))
    ellipse(scrn, white, (x + round((0.25 - 0.009) * dx), y + round((0.156 + 0.03) * dy),
                            round(0.03 * dx), round(0.08 * dy)))
    circle(scrn, afro_american_screen_color, (x + round(0.215 * dx), y + round(0.156 * dy)), round(0.01017 * dy))
    circle(scrn, afro_american_screen_color, (x + round((0.275 - 0.009) * dx), y + round((0.192 + 0.03) * dy)), round(0.01017 * dy))

    # ears:
    x_1, y_1 = x + round(0.21 * dx), y + round(0.0909 * dy)
    x_2, y_2 = x + round(0.278 * dx), y + round(0.1 * dy)
    polygon(scrn, beige, [(x_1, y_1 + round(0.018 * dy)), (x_1 + round(0.0338 * dx), y_1 + round(0 * dy)),
                            (x_1 + round(0.013 * dx), y_1 - round(0.0636 * dy))])
    polygon(scrn, beige, [(x_2, y_2 + round(0.018 * dy)), (x_2 + round(0.0339 * dx), y_2 + round(0.0909 * dy)),
                            (x_2 + round(0.0237 * dx), y_2 - round(0.0545 * dy))])
    return None


def find_xcoord_on_ellipse(ycoord, cx, cy, a, b):
    # (cx, cy) are the coordinates of the ellipse's center
    # a, b are the half height and half width of the ellipse
    # ycoord is the knows y-coordinate of a point on the ellipse
    return cx - round(a * math.sqrt(1 - ((ycoord - cy) / b) ** 2))


def ice_house(x, y, dx):
    """

    :param x: coordinate on x axis
    :param y: coordinate on y axis
    :param dx: width
    :return: draws an ice house
    """
    # finding the value of dy through dx:
    dy = round(0.9 * dx)

    ellipse(screen, brown, (x, y, dx, dy))
    arc(screen, afro_american_screen_color, (x, y, dx, dy), 0, math.pi + 1, 4)
    rect(screen, white, (x, round(y + 0.5 * dy), dx, round(0.51 * dy)))
    line(screen, afro_american_screen_color, (x, y + 0.5 * dy), (x + dx, y + 0.5 * dy), 2)

    # horizontal lines between the snow blocks:
    cx, cy = x + dx / 2, y + dy / 2
    line(screen, dark_grey, (find_xcoord_on_ellipse(y + round(dy / 8), cx, cy, dx / 2, dy / 2), y + round(dy / 8)),
         ((-1) * find_xcoord_on_ellipse(y + round(dy / 8), cx, cy, dx / 2, dy / 2) + 2 * cx, y + round(dy / 8)), 1)
    line(screen, dark_grey, (find_xcoord_on_ellipse(y + round(dy / 4), cx, cy, dx / 2, dy / 2), y + round(dy / 4)),
         ((-1) * find_xcoord_on_ellipse(y + round(dy / 4), cx, cy, dx / 2, dy / 2) + 2 * cx, y + round(dy / 4)), 1)
    line(screen, dark_grey, (find_xcoord_on_ellipse(y + round(3 * dy / 8), cx, cy, dx / 2, dy / 2),
                                y + round(3 * dy / 8)),
         ((-1) * find_xcoord_on_ellipse(y + round(3 * dy / 8), cx, cy, dx / 2, dy / 2) + 2 * cx,
          y + round(3 * dy / 8)), 1)

    # vertical lines between the snow blocks:
    line(screen, dark_grey, (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.25 * dx), y + round(dy / 8)), 1)
    line(screen, dark_grey, (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.54 * dx), y + round(dy / 8)), 1)
    line(screen, dark_grey, (x + round(0.5 * dx), y + round(0 * dy)), (x + round(0.7 * dx), y + round(dy / 8)), 1)

    line(screen, dark_grey, (x + round(0.3 * dx), y + round(dy / 8)), (x + round(0.25 * dx), y + round(dy / 4)), 1)
    line(screen, dark_grey, (x + round(0.46 * dx), y + round(dy / 8)), (x + round(0.43 * dx), y + round(dy / 4)), 1)
    line(screen, dark_grey, (x + round(0.59 * dx), y + round(dy / 8)), (x + round(0.62 * dx), y + round(dy / 4)), 1)
    line(screen, dark_grey, (x + round(0.7 * dx), y + round(dy / 8)), (x + round(0.75 * dx), y + round(dy / 4)), 1)

    line(screen, dark_grey, (x + round(0.15 * dx), y + round(dy / 4)), (x + round(0.12 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, dark_grey, (x + round(0.3 * dx), y + round(dy / 4)),
         (x + round(0.27 * dx), y + round(3 * dy / 8)), 1)
    line(screen, dark_grey, (x + round(0.45 * dx), y + round(dy / 4)), (x + round(0.42 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, dark_grey, (x + round(0.54 * dx), y + round(dy / 4)), (x + round(0.57 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, dark_grey, (x + round(0.68 * dx), y + round(dy / 4)), (x + round(0.75 * dx), y + round(3 * dy / 8)),
         1)
    line(screen, dark_grey, (x + round(0.83 * dx), y + round(dy / 4)),
         (x + round(0.89 * dx), y + round(3 * dy / 8)), 1)

    line(screen, dark_grey, (x + round(0.13 * dx), y + round(3 * dy / 8)), (x + round(0.11 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.26 * dx), y + round(3 * dy / 8)), (x + round(0.23 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.36 * dx), y + round(3 * dy / 8)), (x + round(0.32 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.49 * dx), y + round(3 * dy / 8)), (x + round(0.48 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.63 * dx), y + round(3 * dy / 8)), (x + round(0.65 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.75 * dx), y + round(3 * dy / 8)), (x + round(0.78 * dx), y + round(dy / 2)),
         1)
    line(screen, dark_grey, (x + round(0.87 * dx), y + round(3 * dy / 8)), (x + round(0.91 * dx), y + round(dy / 2)),
         1)
    return None


# drawing the screen:
screen = screen_creator(600)

# drawing the ice houses:
ice_house(10, 350, 90)
ice_house(250, 370, 100)
ice_house(30, 370, 300)
ice_house(25, 490, 120)
ice_house(120, 500, 140)

# drawing the cats:
cat(50, 675, 300, screen)

cat(0, 550, 150, screen)

cat_surface_2 = pygame.Surface((330, round(0.333 * 330)))
cat_surface_2.set_colorkey((0, 0, 0))
cat(0, 0, 330, cat_surface_2)
screen.blit(cat_surface_2, (150, 820))

# drawing the humans:
human_reflected(400, 330, 50)
human(480, 360, 60, screen)
human_reflected(330, 390, 40)
human_reflected(410, 400, 70)
human(530, 400, 90, screen)
human(350, 450, 180, screen)

# drawing the last cat on top of the humans' shadow:
cat_surface_1 = pygame.Surface((250, round(0.333 * 250)))
cat_surface_1.set_colorkey((0, 0, 0))
cat(0, 0, 250, cat_surface_1)
screen.blit(cat_surface_1, (400, 700))

# initialising the screen
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
