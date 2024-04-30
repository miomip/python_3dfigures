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
