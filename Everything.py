import pygame
from math import cos, sin, pi
from numpy import matrix
from time import sleep
from random import randint

def cube():
    white = (255, 255, 255)
    width = 500
    height = 500
    
    pygame.init()
    display = pygame.display
    screen = display.set_mode((width, height))
    display.set_caption("3D")
    
    clock = pygame.time.Clock()
    dt = 0
    
    running = True
    
    turning_speed = 190
    
    x = 50
    
    
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
    
    def points(x, y, z):
        points_3d = (
            ( x,  y,  z),
            (-x,  y,  z),
            ( x, -y,  z),
            ( x,  y, -z),
            (-x,  y, -z),
            ( x, -y, -z),
            (-x, -y, -z),
            (-x, -y,  z),
        )
        return points_3d


    pointers = points(x, x, x)
    
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
    
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, width, height))
    
        render_points = []
    
        for p in pointers:
    
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
    
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
             rotation[0] += (pi / turning_speed) * dt
        if keys[pygame.K_s]:
             rotation[0] -= (pi / turning_speed) * dt
        if keys[pygame.K_a]:
             rotation[1] -= (pi / turning_speed) * dt
        if keys[pygame.K_d]:
             rotation[1] += (pi / turning_speed) * dt
        
        dt = clock.tick(120) / 10
        display.flip()
        sleep(1/45)



import pygame
from math import cos, sin, pi
from numpy import matrix
from time import sleep
from random import randint

def slope():
    white = (100, 200, 255)
    width = 500
    height = 500

    pygame.init()
    display = pygame.display
    screen = display.set_mode((width, height))
    display.set_caption("3D")

    clock = pygame.time.Clock()
    dt = 0

    running = True

    turning_speed = 190

    x = 100

    points_3d = (
        ( x,  x,  x),
        ( x, -x,  x),
        ( x,  x, -x),
        (-x,  x, -x),
        ( x, -x, -x),
        (-x, -x, -x),
    )

    rotation = [4.8330922770752425, -0.8631112448283533, 0]


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
                pygame.draw.line(screen, white, render_points[p1], p2, 2)
                


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            rotation[0] -= (pi / turning_speed) * dt
        if keys[pygame.K_s]:
            rotation[0] += (pi / turning_speed) * dt
        if keys[pygame.K_a]:
            rotation[1] -= (pi / turning_speed) * dt
        if keys[pygame.K_d]:
            rotation[1] += (pi / turning_speed) * dt

        dt = clock.tick(120) / 10
        display.flip()
        sleep(1/45)





class Colors:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    purple = "\u001B[35m"
    cyan = "\u001b[36m"
    gray = "\u001B[37m"

    darkGray = "\u001b[30;1m"
    lightRed = "\u001b[31;1m"
    boldGreen = "\u001b[32;1m"
    boldYellow = "\u001b[33;1m"
    lightBlue = "\u001b[34;1m"
    boldPurple = "\u001b[35;1m"
    boldCyan = "\u001b[36;1m"
    lightGray = "\u001b[37;1m"

    backgroundBlack = "\u001b[40m"
    backgroundRed = "\u001b[41m"
    backgroundGreen = "\u001b[42m"
    backgroundYellow = "\u001b[43m"
    backgroundBlue = "\u001b[44m"
    backgroundPurple = "\u001b[45m"
    backgroundCyan = "\u001b[46m"
    backgroundGray = "\u001b[47m"

    backgroundDarkGray = "\u001b[40;1m"
    backgroundLightRed = "\u001b[41;1m"
    backgroundLime = "\u001b[42;1m"
    backgroundLightBlue = "\u001b[44;1m"
    backgroundLightGray = "\u001b[47;1m"

    bold = "\u001b[1m"
    italic = "\u001b[3m"
    underline = "\u001B[4m"
    crossedOver = "\u001B[9m"
    boldUnderline = "\u001B[21m"
    reversed = "\u001b[7m"


    resetColor = "\u001b[0m"

def print_all_colors():
    for j in range(0, 240):
        code = 1 * 16 + j
        code = code.__str__()
        out = "\u001b[48;5;" + code + "m" + " "
        j_out = 16 + j
        j_out = j_out.__str__()
        print(out + j_out + Colors.resetColor + Colors.resetColor, end="")
        if j == 239:
            print(Colors.resetColor + "\n")


def styled_text(text: str, color: str):
    return print(color + text + Colors.resetColor)


def throw_exception(exception: str, error_code: str):
    return print(
        Colors.bold +
        Colors.red +
        "Exception:" +
        Colors.gray +
        " " +
        exception +
        "\n" +
        Colors.red +
        "Error:" +
        Colors.gray +
        " " +
        error_code +
        Colors.resetColor
    )


def print_dictionary(dictionary: dict):
    for key, values in dictionary.items():
        if key is values:
            print()
        else:
            print(key, end=", ")


from turtle import *  # type: ignore


def cute_smile():
    pensize(5)
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    bk(100)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    fd(50)
    rt(90)
    fd(30)
    pendown()
    circle(12, 180)
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()

from math import sqrt
import turtle as tl
from lib.Colors import *
from lib.DictTools import *


def small_house():
    house_length = 50
    tl.right(90)
    tl.fd(house_length / 2)
    tl.left(90)
    for i in range(1, 4):
        tl.fd(house_length)
        tl.left(90)
    tl.fd(house_length / 2)
    tl.right(180)
    tl.fd(house_length / 2)
    tl.right(30)
    math_for_roof = sqrt((house_length * 0.87) ** 2 + (house_length / 2) ** 2)
    tl.fd(math_for_roof)
    tl.right(120)
    tl.fd(math_for_roof)
    tl.hideturtle()
    tl.exitonclick()


def big_house():
    house_length = 120
    tl.right(90)
    tl.fd(house_length / 2)
    tl.left(90)
    for i in range(1, 4):
        tl.fd(house_length)
        tl.left(90)
    tl.fd(house_length / 2)
    tl.right(180)
    tl.fd(house_length / 2)
    tl.right(30)
    math_for_roof = sqrt((house_length * 0.87) ** 2 + (house_length / 2) ** 2)
    tl.fd(math_for_roof)
    tl.right(120)
    tl.fd(math_for_roof)
    tl.hideturtle()
    tl.exitonclick()


def house():
    types = {
        'small': small_house,
        'big': big_house,
        '': ''
    }
    print("Sizes you can pick:", end=" ")
    print_dictionary(types)

    inp = input("what size do you want?: ")
    if types.get(inp.lower()) is None:
        throw_exception("IllegalArgumentException", "-1")
        return house()
    else:
        return types[inp.lower()]()


from turtle import *  # type: ignore


def normal():
    pensize(5)
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    bk(100)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    fd(25)
    rt(90)
    fd(15)
    lt(90)
    pendown()
    fd(40)
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()


import turtle as tl
from math import *  # type: ignore


def polygonal_shape():
    farger = ["Red", "Green", "Blue", "Black", "Yellow", "Orange", "Pink", "Cyan", "White"]
    tl.speed(10 ** 1000000)
    while True:
        sides = int(input("How many sides do you want?: "))
        if sides == int(sides):
            break
    while True:
        print("You can pick from: Red, Green, Blue, Black, Yellow, Orange, Pink, Cyan, White")
        color = input("What color do you want it to be?: ")
        color.lower()
        if color.capitalize() in farger:
            break
    color = color.capitalize()
    tl.begin_fill()
    tl.fillcolor(color)
    tl.pencolor(color)
    for i in range(sides):
        tl.fd(1000 / sides)
        tl.right(360 / sides)
    tl.end_fill()
    tl.exitonclick()


import random
import turtle as tl


def random_colors():
    tl.colormode(255)
    tl.speed(1000)
    tl.pensize(28)
    for i in range(200):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        tl.fillcolor(r, g, b)
        tl.pencolor(r, g, b)
        tl.right(random.randint(0, 360))
        tl.fd(20)

    tl.exitonclick()


from turtle import *  # type: ignore


def sad():
    pensize(5)
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    bk(100)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    fd(25)
    rt(90)
    fd(30)
    pendown()
    circle(30, -180)
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()


from turtle import *  # type: ignore


def sideeye():
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    bk(200)
    begin_fill()
    circle(35, color("black"))
    end_fill()
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()


from turtle import *  # type: ignore


def smile():
    pensize(5)
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    bk(100)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    fd(25)
    rt(90)
    fd(15)
    pendown()
    circle(30, 180)
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()


from turtle import *  # type: ignore


def weird_guy_emoji():  # ignore error
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    bk(100)
    begin_fill()
    circle(35, color("black"))
    end_fill()
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()


from random_colors import random_colors
from house import house
from polygonal_shape import polygonal_shape
from weird_guy_emoji import weird_guy_emoji
from cuteSmile import cute_smile
from sideeye import sideeye
from smile import smile
from normal import normal
from sad import sad
from lib.Colors import *
from lib.DictTools import *
from TD.cube import *
from TD.slope import *


def main():
    # liste(dictionary) av tillate inputs
    inputs = {
        'smile emoji': smile,
        'sad emoji': sad,
        'normal emoji': normal,
        'cute emoji': cute_smile,
        'side eye emoji': sideeye,
        'weird guy emoji': weird_guy_emoji,
        'all colors': print_all_colors,
        'house': house,
        'random colors': random_colors,
        'polygonal shape': polygonal_shape,
        'cube': cube,
        'slope': slope,
        '': ''
    }
    print("You can draw:", end=" ")
    print_dictionary(inputs)

    inp = input("What do you want to draw: ")
    if inputs.get(inp.lower()) is None:
        throw_exception("IllegalArgumentException", "-1")
        return main()
    else:
        return inputs[inp.lower()]()


# Hovedfunsjon
if __name__ == "__main__":
    main()

