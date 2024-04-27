from house import house
from snurt import snurt
from cuteSmile import cute_smile
from sideeye import sideeye
from smile import smile
from normal import normal
from sad import sad
from lib.Colors import *
from skole.DictTools import *


def main():
    # list(dictionary) of allowed inputs
    inputs = {
        'smile emoji': smile,
        'sad emoji': sad,
        'normal emoji': normal,
        'cute emoji': cute_smile,
        'side eye emoji': sideeye,
        'weird guy emoji': snurt,
        'all colors': print_all_colors,
        'house': house,
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


if __name__ == "__main__":
    main()
