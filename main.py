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
