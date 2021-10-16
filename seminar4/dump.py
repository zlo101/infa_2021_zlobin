from random import randint


def new_ball():
    """draws a new circle and puts its coordinates and radius into global variables x, y & r"""
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = (0, 0, 0)
    return [color, x, y, r]


print(new_ball()[1])
