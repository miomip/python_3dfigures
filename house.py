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
