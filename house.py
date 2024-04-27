from math import sqrt
import turtle as tl
from lib.Colors import Colors


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
    return 0


def house():
    types = {
        'small': small_house,
        'big': big_house
    }
    inp = input("what size do you want?")
    if types.get(inp.lower()) is None:
        return print(Colors.bold
                     + Colors.red
                     + "Exception:"
                     + Colors.gray
                     + " IllegalArgumentException"
                     + "\n"
                     + Colors.red
                     + "Error:"
                     + Colors.gray
                     + " -1"
                     + Colors.resetColor
                     )
    else:
        return types[inp.lower()]()
