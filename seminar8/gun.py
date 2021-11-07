import math
from random import randint
from random import choice

import pygame

FPS = 30

# listing colors and creating an array of them for further use in ball coloring:
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# setting the screen's parameters:
WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, x, y):
        """initializes an object of the class"""
        self.screen = screen
        self.x = x
        self.y = y
        self.r = randint(10, 20)
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.alive = True
        self.ind = 0

    def move(self):
        """Moves the ball with gravity and walls considered"""
        # the value of square root of the power reduction coefficient and the gravity coefficient:
        k = 0.1
        g = 75
        # calculating the projected coordinates of the ball's center:
        p_x = self.x + self.vx * (1 / FPS)
        p_y = self.y + self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
        # destroying the ball if its power has decreased significantly (which means it's just on the floor):
        if self.ind > 10:
            self.alive = False

        # changing the ball's motion parameters:
        if self.alive is True:
            if self.r <= p_x <= WIDTH - self.r and self.r <= p_y <= HEIGHT - self.r:
                self.x += self.vx * (1 / FPS)
                self.y += self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vy += g * (1 / FPS)
            elif WIDTH - self.r < p_x or p_x < self.r:
                self.x -= k * self.vx * (1 / FPS)
                self.y += k * self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vx = k * (-1) * self.vx
                self.vy = k * self.vy + g * (1 / FPS)
                self.ind += 1
            elif HEIGHT - self.r < p_y or p_y < self.r:
                self.x += self.vx * (1 / FPS)
                self.y += (-1) * self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vy = (-1) * self.vy
                self.vy = k * self.vy + g * (1 / FPS)
                self.ind += 1

    def draw(self):
        """draws the ball"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test_ball(self, obj):
        """
        The function checks if this specific ball has collided with a target from the obj list
        :param obj: the list of targets
        :returns an array with boolean variables indicating if the ball has collided with each of the targets
        """
        result = []
        for o in obj:
            if (self.x - o.x) ** 2 + (self.y - o.y) ** 2 <= (self.r + o.r) ** 2:
                result.append(True)
            else:
                result.append(False)
        return result

    def hit_test_bunny(self, obj):
        """
        The function checks if this specific ball has collided with a target from the obj list
        :param obj: the list of targets
        :returns an array with boolean variables indicating if the ball has collided with each of the targets
        """
        result = []
        for o in obj:
            if abs(self.x - (o.width + o.x)) <= o.width and abs(self.y - (o.height + o.y)) <= o.height:
                result.append(True)
            else:
                result.append(False)
        return result


class Bunny:
    def __init__(self):
        """initializes an object of the class"""
        self.screen = screen
        self.x = randint(70, 730)
        self.y = randint(70, 530)
        self.height = 30  # half height
        self.width = 30  # half width
        self.vx = randint(10, 20)
        self.vy = randint(10, 20)
        self.live = 30
        self.ind = 0

    def move(self):
        """Moves the bunny with gravity and walls considered"""
        # the value of square root of the power reduction coefficient and the gravity coefficient:
        k = 1
        g = -75
        # calculating the projected coordinates of the bunny's center:
        p_x = self.x + self.vx * (1 / FPS) + self.width
        p_y = self.y + self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2 + self.height
        # destroying the ball if its power has decreased significantly (which means it's just on the floor):
        if self.ind > 10:
            self.live = 0

        # changing the ball's motion parameters:
        if self.live != 0:
            if self.width <= p_x <= WIDTH - self.width and self.height <= p_y <= HEIGHT - self.height:
                self.x += self.vx * (1 / FPS)
                self.y += self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vy += g * (1 / FPS)
            elif WIDTH - self.width < p_x or p_x < self.width:
                self.x -= k * self.vx * (1 / FPS)
                self.y += k * self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vx = k * (-1) * self.vx
                self.vy = k * self.vy + g * (1 / FPS)
                self.ind += 1
            elif HEIGHT - self.height < p_y or p_y < self.height:
                self.x += self.vx * (1 / FPS)
                self.y += (-1) * self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
                self.vy = (-1) * self.vy
                self.vy = k * self.vy + g * (1 / FPS)
                self.ind += 1

    def draw(self):
        """draws the bunny"""
        bunny_screen = pygame.Surface((2 * self.width, 2 * self.height))
        addscreen = pygame.image.load('dabunnae.png')
        bunny_screen.set_colorkey((0, 0, 0))
        bunny_screen.blit(addscreen, (0, 0))
        screen.blit(bunny_screen, (self.x, self.y))


class Tank:
    def __init__(self):
        """initializes an object of the class"""
        self.screen = screen
        self.screen = screen
        self.f2_power = 400
        self.f2_on = False
        self.angle = 1
        self.velocity = 100
        self.x = 50
        self.y = 530

    def fire2_start(self):
        """changes the indicator of the mouse being down"""
        self.f2_on = True

    def fire2_end_ball(self, event):
        """
        With the mouse button getting up, this creates a ball whose velocity depends on the mouse's last position
        and the gun's power; the point from which the ball is released depends on the tank's position
        """
        global balls
        new_ball = Ball(self.x + 50, self.y)
        self.angle = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = self.f2_power * math.sin(self.angle)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 150

    def fire2_end_bomb(self, event):
        """
        With the mouse button getting up, this creates a bomb whose velocity depends on the mouse's last position
        and the gun's power; the point from which the bomb is released depends on the tank's position
        """
        global bombs
        new_bomb = Bomb(self.x + 50, self.y)
        self.angle = math.atan2((event.pos[1] - new_bomb.y), (event.pos[0] - new_bomb.x))
        new_bomb.vx = self.f2_power * math.cos(self.angle)
        new_bomb.vy = self.f2_power * math.sin(self.angle)
        bombs.append(new_bomb)
        self.f2_on = 0
        self.f2_power = 150

    def targeting(self, event):
        """Updates the angle of the gun according to the position of the mouse"""
        if event:
            self.angle = math.atan2((event.pos[1] - self.y), (event.pos[0] - (self.x + 50)))

    def draw(self):
        """draws the tank with the gun"""
        rot_angle = (-1) * round(self.angle * 180 / 3.14)

        addscreen_1 = pygame.Surface((54, 12))
        addscreen_2 = pygame.Surface((100, 64))
        addscreen_1.set_colorkey((0, 0, 0))
        addscreen_2.set_colorkey((0, 0, 0))

        addscreen_1.blit(gunImg, (0, 0))
        addscreen_1 = pygame.transform.rotate(addscreen_1, rot_angle)
        addscreen_2.blit(tankImg, (0, 0))

        gun_size = addscreen_1.get_size()
        if 0 <= rot_angle < 90:
            screen.blit(addscreen_1, (self.x + 50, self.y - gun_size[1] + 20))
        elif 90 <= rot_angle <= 180:
            screen.blit(addscreen_1, (self.x + 50 - gun_size[0], self.y - gun_size[1] + 20))
        elif -90 < rot_angle <= 0:
            screen.blit(addscreen_1, (self.x + 50, self.y + 20))
        elif -180 <= rot_angle <= -90:
            screen.blit(addscreen_1, (self.x + 50 - gun_size[0], self.y + 20))

        screen.blit(addscreen_2, (self.x, self.y))

    def power_up(self):
        """if the mouse is down, this raises the gun's power by 20 and changes its color to red"""
        if self.f2_on:
            if self.f2_power < 400:
                self.f2_power += 40

    def move(self):
        px = self.x + (1 / FPS) * self.velocity  # projected x-coordinate of the tank's left side
        if 0 < px < WIDTH - 100:
            self.x = px
        else:
            self.velocity = (-1) * self.velocity
            self.x = self.x + (1 / FPS) * self.velocity


class Target:
    def __init__(self):
        """initializes an object of the class"""
        self.screen = screen
        self.x = randint(600, 730)
        self.y = randint(300, 530)
        self.r = randint(10, 50)
        self.vx = randint(10, 20)
        self.vy = randint(10, 20)
        self.color = RED
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def move(self):
        """Moves the target with the walls considered"""

        p_x = self.x + self.vx * (1 / FPS)
        p_y = self.y + self.vy * (1 / FPS)
        if self.r <= p_x <= WIDTH - self.r and self.r <= p_y <= HEIGHT - self.r:
            self.x += self.vx * (1 / FPS)
            self.y += self.vy * (1 / FPS)
        elif WIDTH - self.r < p_x or p_x < self.r:
            self.x -= self.vx * (1 / FPS)
            self.y += self.vy * (1 / FPS)
            self.vx = (-1) * self.vx
        elif HEIGHT - self.r < p_y or p_y < self.r:
            self.x += self.vx * (1 / FPS)
            self.y += (-1) * self.vy * (1 / FPS)
            self.vy = (-1) * self.vy

    def draw(self):
        """draws the target"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Bomb:
    def __init__(self, x, y):
        """initializes an object of the class"""
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 13
        self.height = 13
        self.vx = 0
        self.vy = 0
        self.alive = True
        self.ind = 0

    def move(self):
        """Moves the bomb with gravity and walls considered"""
        # the value of square root of the gravity coefficient:
        g = 75
        # calculating the projected coordinates of the bomb's center:
        p_x = self.x + self.width + self.vx * (1 / FPS)
        p_y = self.y + self.height + self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2

        # moving the bomb and killing it as soon as it hits a wall:
        if self.width <= p_x <= WIDTH - self.width and self.height <= p_y <= HEIGHT - self.height:
            self.x += self.vx * (1 / FPS)
            self.y += self.vy * (1 / FPS) + 0.5 * g * (1 / FPS) ** 2
            self.vy += g * (1 / FPS)
        else:
            self.alive = False

    def draw(self):
        addscreen = pygame.Surface((2 * self.width, 2 * self.height))
        addscreen.set_colorkey((0, 0, 0))
        addscreen.blit(bombImg, (0, 0))

        screen.blit(addscreen, (self.x, self.y))

    def hit_test_ball(self, obj):
        """
        The function checks if this specific bomb has collided with a target from the obj list (here, balls)
        :param obj: the list of targets (here, balls)
        :returns an array with boolean variables indicating if the ball has collided with each of the targets
        """
        result = []
        for o in obj:
            if (self.x + self.width - o.x) ** 2 + (self.y + self.height - o.y) ** 2 <= (self.width + o.r) ** 2:
                result.append(True)
            else:
                result.append(False)
        return result

    def hit_test_bunny(self, obj):
        """
        The function checks if this specific bomb has collided with a target from the obj list (here, bunnies)
        :param obj: the list of targets (here, bunnies)
        :returns an array with boolean variables indicating if the bomb has collided with each of the targets
        """
        result = []
        for o in obj:
            if abs(self.x + self.width - (o.width + o.x)) <= o.width \
                    and abs(self.y + self.height - (o.height + o.y)) <= o.height:
                result.append(True)
            else:
                result.append(False)
        return result


def temporary_draw(objects):
    """draws the temporary objects"""
    for o in objects:
        if o[0] != 0:
            screen.blit(o[0], (o[1], o[2]))


def add_temporary(addsurface, x, y):
    """
    adds a new temporary explosion to the array of the explosions
    x and y are the coordinates of the center of the object exploded
    assigns a pair of coordinates to each item which reflects the point to which the picture should be attached
    """
    add_size = addsurface.get_size()
    x_0 = x - round(0.5 * add_size[0])
    y_0 = y - round(0.5 * add_size[1])
    objects.append([addsurface, x_0, y_0, 0])


def check_temporary(objects):
    """updates the clock for each of the temporary objects and kills objects with the clock running over 250"""
    for i in range(len(objects)):
        if objects[i][3] == 250:
            objects[i][0] = 0
    for o in objects:
        o[3] += 1


def bunny_death():
    """creates a surface with the bunny explosion for further attachment to the parent surface (screen)"""
    main_screen = pygame.Surface((100, 100))
    main_screen.set_colorkey((0, 0, 0))
    main_screen.blit(bunnyexplosionImg, (0, 0))
    return main_screen


def bomb_explosion():
    """creates a surface with the bomb explosion for further attachment to the parent surface (screen)"""
    main_screen = pygame.Surface((30, 30))
    main_screen.set_colorkey((0, 0, 0))
    main_screen.blit(bombexposionImg, (0, 0))
    return main_screen


def menu_draw():
    """draws the menu with two buttons according to what mode is now on"""
    addscreen = pygame.Surface((100, 92))
    addscreen.set_colorkey((0, 0, 0))

    if mode[0] is True:
        addscreen.blit(menuballImg, (0, 0))
        screen.blit(addscreen, (800 - 5 - 100, 5))
    elif mode[1] is True:
        addscreen.blit(menubombImg, (0, 0))
        screen.blit(addscreen, (800 - 5 - 100, 5))


def menu_click(action):
    """checks if the user has clicked on one of the buttons and changes the mode accordingly"""
    x_mouse, y_mouse = action.pos[0], action.pos[1]
    if 695 + 4 <= x_mouse <= 795 - 4 and 5 + 4 <= y_mouse <= 5 + 4 + 36:
        return [True, False]
    if 695 + 4 <= x_mouse <= 795 - 4 and 5 + 52 <= y_mouse <= 5 + 52 + 36:
        return [False, True]
    else:
        return mode


# starting the game, creating a screen, and creating a clock:
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False

# creating the needed objects and setting values:
objects = []
tank = Tank()
target = [Target(), Target()]
bunny = [Bunny(), Bunny()]
balls = []
bombs = []
mode = [True, False]


# images:
bombImg = pygame.image.load('dabomb.png')
gunImg = pygame.image.load('dagun.png')
tankImg = pygame.image.load('datank.png')
menubombImg = pygame.image.load('bomb_mode.png')
menuballImg = pygame.image.load('ball_mode.png')
bombexposionImg = pygame.image.load('dabombexplosion.png')
bunnyexplosionImg = pygame.image.load('daexplosion.png')

while not finished:
    # updating the screen:
    screen.fill(WHITE)
    temporary_draw(objects)
    menu_draw()
    tank.draw()
    for b in bunny:
        b.draw()
    for t in target:
        t.draw()
    for b in balls:
        if b.alive is True:
            b.draw()
    for b in bombs:
        if b.alive is True:
            b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tank.fire2_start()
            mode = menu_click(event)
        elif event.type == pygame.MOUSEBUTTONUP and mode[0] is True:
            tank.fire2_end_ball(event)
        elif event.type == pygame.MOUSEBUTTONUP and mode[1] is True:
            tank.fire2_end_bomb(event)
        elif event.type == pygame.MOUSEMOTION:
            tank.targeting(event)

    # checking all projectiles for collision with targets on the screen:
    for b in balls:
        if b.alive is True:
            # checking for collision with ball targets:
            indicator_1 = b.hit_test_ball(target)
            for i in range(len(indicator_1)):
                if indicator_1[i] is True:
                    target[i].live = 0
                    target[i].hit()
                    target[i] = Target()
            # checking for collision with bunny targets:
            indicator_2 = b.hit_test_bunny(bunny)
            for j in range(len(indicator_2)):
                if indicator_2[j] is True:
                    add_temporary(bunny_death(), bunny[j].x + bunny[j].width, bunny[j].y + bunny[j].height)
                    bunny[j].live = 0
                    bunny[j] = Bunny()
    for j in range(len(bombs)):
        b = bombs[j]
        ind = False
        if b.alive is True:
            # checking for collision with ball targets:
            indicator_1 = b.hit_test_ball(target)
            for i in range(len(indicator_1)):
                if indicator_1[i] is True:
                    target[i].live = 0
                    target[i].hit()
                    target[i] = Target()
                    ind = True
            # checking for collision with bunny targets:
            indicator_2 = b.hit_test_bunny(bunny)
            for j in range(len(indicator_2)):
                if indicator_2[j] is True:
                    add_temporary(bunny_death(), bunny[j].x + bunny[j].width, bunny[j].y + bunny[j].height)
                    bunny[j].live = 0
                    bunny[j] = Bunny()
                    ind = True
            print(ind)
            if ind is True:
                add_temporary(bomb_explosion(), b.x + b.width, b.y + b.height)
                b.alive = False

    tank.power_up()

    # moving all the objects displayed on the screen:
    tank.move()
    for t in target:
        t.move()
    for b in bunny:
        b.move()
    for b in bombs:
        if b.alive is True:
            b.move()
    for b in balls:
        if b.alive is True:
            b.move()

    # checking if the clocks of the temporary objects have run out:
    check_temporary(objects)

pygame.quit()
