from house import house
from snurt import snurt
from cuteSmile import cuteSmile
from sideeye import Sideeye
from smile import Smile
from normal import normal
from sad import sad
from lib.Colors import Colors, printAllColors

def main():
    #liste(dictionary) over mulig inputs
    inputs = {
        'smile emoji' : Smile,
        'sad emoji' : sad,
        'normal emoji' : normal,
        'cute emoji' : cuteSmile,
        'side eye emoji' : Sideeye,
        'weird guy emoji' : snurt,
        'all colors' : printAllColors,
        'house' : house
    }
    print("You can draw:")
    for key, values in inputs.items(): 
        print(key, end=", ")
    
    inp = input("\nWhat do you want to draw: ")
    if inputs.get(inp.lower()) == None:
        return print(Colors.bold
                     +Colors.red
                     +"Exception:"
                     +Colors.gray
                     +" IllegalArgumentException"
                     +"\n"
                     +Colors.red
                     +"Error:"
                     +Colors.gray 
                     +" -1" 
                     +Colors.resetColor
                     )
    else:
        return inputs[inp.lower()]()

if __name__ == "__main__":
    main()

