
import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        print(make_figlet(), end='')

    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        print(make_figlet(sys.argv[2]), end="")
    else:
        sys.exit("Invalid usage")



def make_figlet(font=None):
    text = input("Input: ")
    if font is None:
        font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    return figlet.renderText(text)


if __name__ == '__main__':
    main()


