

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
