class Colors:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    blue = "\u001b[34m"
    lime = "\u001B[32m"
    orange = "\u001B[33m"
    magenta = "\u001B[35m"
    lightBlue = "\u001B[36m"
    gray = "\u001B[37m"

    brightBlack = "\u001b[30;1m"
    brightRed = "\u001b[31;1m"
    brightGreen = "\u001b[32;1m"
    brightYellow = "\u001b[33;1m"
    brightBlue = "\u001b[34;1m"
    brightMagenta = "\u001b[35;1m"
    brightCyan = "\u001b[36;1m"
    brightWhite = "\u001b[37;1m"

    backgroundBlack = "\u001b[40m"
    backgroundRed = "\u001b[41m"
    backgroundGreen = "\u001b[42m"
    backgroundYellow = "\u001b[43m"
    backgroundBlue = "\u001b[44m"
    backgroundMagenta = "\u001b[45m"
    backgroundCyan = "\u001b[46m"
    backgroundWhite = "\u001b[47m"

    backgroundBrightBlack = "\u001b[40;1m"
    backgroundBrightRed = "\u001b[41;1m"
    backgroundBrightGreen = "\u001b[42;1m"
    backgroundBrightYellow = "\u001b[43;1m"
    backgroundBrightBlue = "\u001b[44;1m"
    backgroundBrightMagenta = "\u001b[45;1m"
    backgroundBrightCyan = "\u001b[46;1m"
    backgroundBrightWhite = "\u001b[47;1m"

    bold = "\u001b[1m"
    italic = "\u001b[3m"
    underline = "\u001B[4m"
    crossedOver = "\u001B[9m"
    boldUnderline = "\u001B[21m"
    reversed = "\u001b[7m"

    resetColor = "\u001b[0m"



def printAllColors():
    for j in range(0, 240):
        code = 1 * 16 + j
        Code = code.__str__()
        out = "\u001b[48;5;" + Code + "m" + " "
        jOut = 16 + j
        JOut = jOut.__str__()
        print(out + JOut + Colors.resetColor + Colors.resetColor, end="")
        if j == 239:
            print(Colors.resetColor + "\n")
def styledText(text:str, Color:str):
    return Color+text+Colors.resetColor