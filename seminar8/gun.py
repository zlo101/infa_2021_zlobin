import math
from random import randint
from random import choice

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# screen's parameters
WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, x=20, y=450):
        """initializes an object of the class"""
        self.screen = screen
        self.x = x
        self.y = y
        self.r = randint(10, 20)
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Moves the ball with gravity and walls considered"""

        p_x = self.x + self.vx * (1 / FPS)
        p_y = self.y + self.vy * (1 / FPS) + 5 * (1 / FPS) ** 2
        if self.r <= p_x <= WIDTH - self.r and self.r <= p_y <= HEIGHT - self.r:
            self.x += self.vx * (1 / FPS)
            self.y += self.vy * (1 / FPS) + 5 * (1 / FPS) ** 2
            self.vy += 10 * (1 / FPS)
        elif WIDTH - self.r < p_x or p_x < self.r:
            self.x -= self.vx * (1 / FPS)
            self.y += self.vy * (1 / FPS) + 5 * (1 / FPS) ** 2
            self.vx = (-1) * self.vx
            self.vy += 10 * (1 / FPS)
        elif HEIGHT - self.r < p_y or p_y < self.r:
            self.x += self.vx * (1 / FPS)
            self.y += (-1) * self.vy * (1 / FPS) + 5 * (1 / FPS) ** 2
            self.vy = (-1) * self.vy
            self.vy += 10 * (1 / FPS)

    def draw(self):
        """draws the ball"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test(self, obj):
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


class Gun:
    def __init__(self):
        """initializes an object of the class"""
        self.screen = screen
        self.f2_power = 200
        self.f2_on = False
        self.angle = 1
        self.color = GREY

    def fire2_start(self):
        """changes the indicator of the mouse being down"""
        self.f2_on = True

    def fire2_end(self, event):
        """
        With the mouse button getting up, this creates a ball whose velocity depends on the mouse's last position
        and the gun's power
        """

        global balls, bullet
        bullet += 1
        new_ball = Ball()
        self.angle = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = self.f2_power * math.sin(self.angle)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 100

    def targeting(self, event):
        """Updates the angle of the gun according to the position of the mouse"""
        if event:
            self.angle = math.atan2((event.pos[1] - 450), (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """draws the gun"""
        pygame.draw.line(self.screen, self.color, (20, 450),
                         (20 + 40 * math.cos(self.angle), 450 + 40 * math.sin(self.angle)), 20)

    def power_up(self):
        """if the mouse is down, this raises the gun's power by 20 and changes its color to red"""
        if self.f2_on:
            if self.f2_power < 200:
                self.f2_power += 20
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """initializes an object of the class"""
        self.screen = screen
        self.x = randint(600, 780)
        self.y = randint(300, 550)
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


# starting the game, creating a screen, and creating a clock:
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False

# creating the needed objects and setting values:
gun = Gun()
target = [Target(), Target()]
bullet = 0
balls = []

while not finished:
    # updating the screen:
    screen.fill(WHITE)
    gun.draw()
    for t in target:
        t.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)

    #
    for b in balls:
        b.move()
        indicator = b.hit_test(target)
        for i in range(len(indicator)):
            if indicator[i] is True and target[i].live:
                target[i].live = 0
                target[i].hit()
                target[i] = Target()
    gun.power_up()

pygame.quit()
