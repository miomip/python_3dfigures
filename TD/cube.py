import pygame
from math import cos, sin, pi
from numpy import matrix
from time import sleep
from random import randint


white = (255, 255, 255)
width = 500
height = 500

pygame.init()
display = pygame.display
screen = display.set_mode((width, height))
display.set_caption("3D")


running = True

x = 50

points_3d = (
    ( x,  x,  x),
    (-x,  x,  x),
    ( x, -x,  x),
    ( x,  x, -x),
    (-x,  x, -x),
    ( x, -x, -x),
    (-x, -x, -x),
    (-x, -x,  x),
)

rotation = [0, 0, 0]


def generate_x(x):
    return matrix([
        [1, 0, 0],
        [0, cos(x), -sin(x)],
        [0, sin(x), cos(x)]
    ])

def generate_y(x):
    return matrix([
        [cos(x), 0, -sin(x)],
        [0, 1, 0],
        [sin(x), 0, cos(x)]
    ])

def generate_z(x):
    return matrix([
        [cos(x), -sin(x), 0],
        [sin(x), cos(x), 0],
        [0, 0, 1]
    ])


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height))

    render_points = []

    for p in points_3d:

        m = matrix([
        [p[0]],
        [p[1]],
        [p[2]]
        ])

        for method, angle in zip((generate_x, generate_y, generate_z), rotation):
            m = method(angle) * m

        x, y, z = map(lambda x: int(width/2 - x), (m[0,0], m[1,0], m[2,0]))

        render_points.append((x, y))

    for p1 in range(len(render_points) - 1):
        for p2 in render_points[p1 + 1:]:
            pygame.draw.line(screen, white, render_points[p1], p2)

    rotation[0] += pi / randint(100, 200)
    rotation[1] += pi / randint(100, 200)

    display.flip()
    sleep(1/45)