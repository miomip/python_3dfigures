from math import * # type: ignore
import turtle as tl
from lib.Colors import *
from lib.DictTools import *

def polygonal_shape():
    farger = ["Red", "Green", "Blue", "Black", "Yellow", "Orange", "Pink", "Cyan", "White"]
    tl.speed(10**1000000)
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
        tl.fd(1000/sides)
        tl.right(360/sides)
    tl.end_fill()
    tl.exitonclick()
