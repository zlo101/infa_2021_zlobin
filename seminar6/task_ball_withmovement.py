import pygame
from pygame.draw import *
from random import randint
from random import randrange

pygame.init()
pygame.font.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
the_font = pygame.font.SysFont('Comic Sans MS', 30)

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
    """creates data for a new circle and returns it in an array"""
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(40, 90)
    color = COLORS[randint(0, 5)]
    v_x = randrange(-1, 2, 2) * randint(1, 7)
    v_y = randrange(-1, 2, 2) * randint(1, 7)
    return [color, x, y, r, v_x, v_y]


def balls(qty):
    """
    creates & returns a data set for the given number of balls
    uses the new_ball function to generate data for each ball
    """
    dataset = []
    for j in range(qty):
        dataset.append(new_ball())
    return dataset


def ball_displayer(balldata):
    """displays the balls using the data from balldata & updates the screen"""
    qty = len(balldata)
    for j in range(qty):
        circle(screen, balldata[j][0], (balldata[j][1], balldata[j][2]), balldata[j][3])
    pygame.display.update()


def click_ind(action, balldata):
    """
    returns an array of Boolean variables which reflect if the click hit this particular ball
    :param action: the event of the mouse click
    :param balldata: the array of data of the balls
    """
    x_mouse, y_mouse = action.pos[0], action.pos[1]
    indicator = []
    qty = len(balldata)

    for j in range(qty):
        x_circle, y_circle, r_circle = balldata[j][1], balldata[j][2], balldata[j][3]
        if (x_mouse - x_circle) ** 2 + (y_mouse - y_circle) ** 2 <= r_circle ** 2:
            indicator.append(True)
        else:
            indicator.append(False)
    return indicator


def move(balldata):
    """
    first, changes balldata according to whether the next projected movement is possible
    second, moves each ball according to the changed data in balldata
    :param balldata: the array of data for each ball
    """
    screen.fill(BLACK)
    qty = len(balldata)
    for j in range(qty):
        # taking out the data of the ball and naming its elements for easier further use:
        a_ball = balldata[j]
        x_coord, y_coord = a_ball[1], a_ball[2]
        r, v_x, v_y = a_ball[3], a_ball[4], a_ball[5]
        color = a_ball[0]

        # finding projected coordinates of the ball's position:
        xp = x_coord + v_x
        yp = y_coord + v_y

        # checking if the ball is about to leave the screen and giving instructions accordingly:
        if 1200 - r >= xp >= r and 800 - r >= yp >= r:
            circle(screen, color, (xp, yp), r)
            a_ball[1], a_ball[2] = xp, yp
        elif yp < r:
            circle(screen, color, (xp, y_coord - v_y), r)
            a_ball[1], a_ball[2], a_ball[5] = xp, y_coord - v_y, -v_y
        elif yp > 800 - r:
            circle(screen, color, (xp, y_coord - v_y), r)
            a_ball[1], a_ball[2], a_ball[5] = xp, y_coord - v_y, -v_y
        elif xp < r:
            circle(screen, color, (x_coord - v_x, yp), r)
            a_ball[1], a_ball[2], a_ball[4] = x_coord - v_x, yp, -v_x
        elif xp > 1200 - r:
            circle(screen, color, (x_coord - v_x, yp), r)
            a_ball[1], a_ball[2], a_ball[4] = x_coord - v_x, yp, -v_x

        # inserting the changed data of the ball into its place in balldata:
        balldata[j] = a_ball

    pygame.display.update()


def score_display(x, y):
    """
    updates the score sign on the screen
    :param x: the number of hits
    :param y: the number of fails
    """
    surface = the_font.render('Hit: {}. Missed: {}.'.format(x, y), False, (255, 255, 255))
    screen.blit(surface, (500, 0))
    pygame.display.update()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# setting the scores as zeros:
hit, miss = 0, 0

# creating balls and a clock:
num = randint(2, 5)
the_balls = balls(num)
clocky = [0] * num

# displaying the ball(s) and the score:
ball_displayer(the_balls)
score_display(hit, miss)

while not finished:
    clock.tick(FPS)

    # moving the ball(s):
    move(the_balls)

    # updating the clock:
    for i in range(num):
        clocky[i] += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ind = click_ind(event, the_balls)
            for i in range(num):
                if ind[i] is True:
                    hit += 1
                    clocky[i] = 0
                    the_balls[i] = new_ball()
    for i in range(num):
        if clocky[i] == 480:
            miss += 1
            clocky[i] = 0
            the_balls[i] = new_ball()

    # updating the score sign:
    score_display(hit, miss)

# showing the result and displaying some nice words:
print("You have completed the game! We sincerely hope you liked it!")
print("Here are your results:")
print('You have hit: {}. And you have missed: {}'.format(hit, miss))
print("Please come back and play it again!")

pygame.quit()
