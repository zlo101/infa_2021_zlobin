import pygame
from pygame.draw import *
from random import randint
from random import randrange
from math import sqrt

# requesting the player's name and reading it:
print('Please write your name in the space below:')
player_name = input()

# initialising pygame:
pygame.init()
pygame.font.init()

FPS = 60
length, width = 800, 1200
screen = pygame.display.set_mode((width, length))
the_font = pygame.font.SysFont('Comic Sans MS', 30)

# creating an array of colors for targets:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """creates data for a new circle and returns its data in an array"""
    x = randint(100, width - 100)
    y = randint(100, length - 100)
    r = randint(40, 90)
    color = COLORS[randint(0, 5)]
    v_x = randrange(-1, 2, 2) * randint(1, 7)
    v_y = randrange(-1, 2, 2) * randint(1, 7)
    return [color, x, y, r, v_x, v_y]


def new_triangle():
    """creates a new regular triangle and returns it data in an array"""
    x = randint(100,  width - 100)
    y = randint(100, length - 100)
    side = randint(100, 140)
    color = COLORS[randint(0, 5)]
    v_x = randrange(-1, 2, 2) * randint(1, 5)
    v_y = randrange(-1, 2, 2) * randint(1, 5)
    cen_to_right = round(side / sqrt(3))
    cen_to_updown = round(side / 2)
    cen_to_left = round(side / sqrt(12))
    return [color, x, y, cen_to_left, cen_to_right, cen_to_updown, v_x, v_y]


def balls(qty):
    """
    creates & returns a data set for the given number of balls
    uses the new_ball function to generate data for each ball
    """
    dataset = []
    for j in range(qty):
        dataset.append(new_ball())
    return dataset


def triangles(qty):
    """
    creates & returns a data set for the given number of triangles
    uses the new_triangle function to generate data for each triangle
    """
    dataset = []
    for j in range(qty):
        dataset.append(new_triangle())
    return dataset


def click_ind(action, balls_data, triangles_data):
    """
    returns an array of Boolean variables which reflect if the click hit this particular target
    :param action: the event of the mouse click
    :param balls_data: the array of data of the balls
    :param triangles_data: the array of data of the triangles
    """
    x_mouse, y_mouse = action.pos[0], action.pos[1]
    indicator = []
    qty_balls, qty_triangles = len(balls_data), len(triangles_data)

    # filling the indicator array for the balls:
    for j in range(qty_balls):
        x_circle, y_circle, r_circle = balls_data[j][1], balls_data[j][2], balls_data[j][3]
        if (x_mouse - x_circle) ** 2 + (y_mouse - y_circle) ** 2 <= r_circle ** 2:
            indicator.append(True)
        else:
            indicator.append(False)

    # filling the indicator for the triangles:
    for k in range(qty_triangles):
        x_triangle, y_triangle = triangles_data[k][1], triangles_data[k][2]
        left, right, updown = triangles_data[k][3], triangles_data[k][4], triangles_data[k][5]
        x1, y1 = x_triangle - left, y_triangle
        x2_3 = x_triangle + right
        b1, b2 = round(y1 - x1 / sqrt(3)), round(y1 + x1 / sqrt(3))
        if (y_mouse - x_mouse / sqrt(3) - b1 <= 0) and (y_mouse + x_mouse / sqrt(3) - b2 >= 0) and (x_mouse <= x2_3):
            indicator.append(True)
        else:
            indicator.append(False)
    return indicator


def balls_move(balls_data):
    """
    first, changes balls_data according to whether the next projected movement is possible
    second, moves each ball according to the changed data in balls_data
    :param balls_data: the array of data for each ball
    """
    qty = len(balls_data)
    for j in range(qty):
        # taking out the data of the ball and naming its elements for easier further use:
        a_ball = balls_data[j]
        x_coord, y_coord = a_ball[1], a_ball[2]
        r, v_x, v_y = a_ball[3], a_ball[4], a_ball[5]
        color = a_ball[0]

        # finding projected coordinates of the ball's position:
        xp = x_coord + v_x
        yp = y_coord + v_y

        # checking if the ball is about to leave the screen and giving instructions accordingly:
        if width - r >= xp >= r and length - r >= yp >= r:
            circle(screen, color, (xp, yp), r)
            a_ball[1], a_ball[2] = xp, yp
        elif yp < r or yp > length - r:
            circle(screen, color, (xp, y_coord - v_y), r)
            a_ball[1], a_ball[2], a_ball[5] = xp, y_coord - v_y, -v_y
        elif xp < r or xp > width - r:
            circle(screen, color, (x_coord - v_x, yp), r)
            a_ball[1], a_ball[2], a_ball[4] = x_coord - v_x, yp, -v_x

        # inserting the changed data of the ball into its place in balldata:
        balls_data[j] = a_ball


def triangles_move(triangles_data):
    """
    first, changes triangles_data according to whether the next projected movement is possible
    second, moves each triangle according to the changed data in triangles_data
    :param triangles_data: the array of data for each ball
    """
    qty = len(triangles_data)
    for j in range(qty):
        # taking out the data of the ball and naming its elements for easier further use:
        a_triangle = triangles_data[j]
        x_coord, y_coord = a_triangle[1], a_triangle[2]
        left, right, updown = a_triangle[3], a_triangle[4], a_triangle[5]
        color, v_x, v_y = a_triangle[0], a_triangle[6], a_triangle[7]

        # finding projected coordinates of the triangle's position:
        xp = x_coord + v_x
        yp = y_coord + v_y

        # checking if the triangle is about to leave the screen and giving instructions accordingly:
        if left <= xp <= width - right and updown <= yp <= length - updown:
            x, y = xp, yp
            polygon(screen, color, [(x - left, y), (x + right, yp - updown), (x + right, y + updown)])
            a_triangle[1], a_triangle[2] = x, y
        elif xp < left or width - right < xp:
            x, y = x_coord - v_x, yp
            polygon(screen, color, [(x - left, y), (x + right, y - updown), (x + right, y + updown)])
            a_triangle[1], a_triangle[2], a_triangle[6] = x, y, -v_x
        elif yp < updown or length - updown < yp:
            x, y = xp, y_coord - v_y
            polygon(screen, color, [(x - left, y), (x + right, y - updown), (x + right, y + updown)])
            a_triangle[1], a_triangle[2], a_triangle[7] = x, y, -v_y

        # inserting the changed data of the triangle into its place in triangles_data:
        triangles_data[j] = a_triangle


def score_display(x):
    """
    updates the score sign on the screen
    """
    surface = the_font.render('Score: {}'.format(x), False, (255, 255, 255))
    screen.blit(surface, (0, 0))


def screen_update():
    screen.fill(BLACK)
    balls_move(the_balls)
    triangles_move(the_triangles)
    score_display(hit)
    quit_the_game()
    pygame.display.update()

    # updating the clock:
    for j in range(num_all):
        clocky[j] += 1


def targets_update(j):
    if 0 <= j < num_balls:
        del_hit = 1
        the_balls[j] = new_ball()
    else:
        del_hit = 1.5
        the_triangles[j - num_balls] = new_triangle()
    return del_hit


def quit_the_game():
    """
    updates the quit sign on the screen
    """
    surface = the_font.render('QUIT', False, (255, 0, 0))
    screen.blit(surface, (width - 100, 0))


def quit_click(action):
    x_mouse, y_mouse = action.pos[0], action.pos[1]
    if width - 100 <= x_mouse <= width and 0 <= y_mouse <= 30:
        return True
    else:
        return False


def quit_screen():
    screen.fill(BLACK)
    text = [the_font.render('{}, you have completed the game! We sincerely hope you liked it!'.format(player_name),
                            False, (255, 255, 255)), the_font.render('Here are your results:', False, (255, 255, 255)),
            the_font.render('You have scored: {}. The number of targets you have missed: {}'.format(hit, miss),
                            False, (255, 255, 255)), the_font.render("Your scores have been saved in a file which you "
                                                                     "will be able to find later.", False, (255, 255,
                                                                                                            255)),
            the_font.render("Please come back and play again!", False, (255, 255, 255))]
    for j in range(len(text)):
        screen.blit(text[j], (100, 100 + 40 * j))
    pygame.display.update()


pygame.display.update()
clock = pygame.time.Clock()
finished = False
ended = False

# creating and opening a file with the results of the game:
result_file = open("results_of_the_game.txt", "w+")


# setting the scores as zeros:
hit, miss = 0, 0


# creating balls, triangle, and a clock:
num_all, num_balls = 7, randint(2, 5)
num_triangles = num_all - num_balls
the_balls = balls(num_balls)
the_triangles = triangles(num_triangles)
clocky = [0] * num_all


# displaying the targets on the screen:
screen_update()


while not finished:
    clock.tick(FPS)

    if ended is True:
        quit_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    else:
        # updating the targets, the score sign, the quit sign, and the clock:
        screen_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_click(event) is True:
                    ended = True
                else:
                    ind = click_ind(event, the_balls, the_triangles)
                    for i in range(num_all):
                        if ind[i] is True:
                            hit += targets_update(i)
                            clocky[i] = 0
        for i in range(num_all):
            if clocky[i] == 500:
                miss += 1
                clocky[i] = 0
                targets_update(i)


# filling in the result file and closing it:
result_file.write('The player {} has scored {}.'.format(player_name, hit))
result_file.close()

pygame.quit()
