import curses
from curses import textpad
import texthelper as txt


def init_colors(bg):
    curses.init_pair(1, curses.COLOR_WHITE, bg)  # General
    curses.init_pair(2, curses.COLOR_GREEN, bg)  # Green Text
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)  # Health
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)  # Mana
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_WHITE)  # Armor
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_YELLOW)  # Highlight yellow
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED)  # Highlight red


def load_frames(screen, y, x):
    # Scene setup
    screen.addstr(0, 1, "Dryad ALPHA V0.1", curses.A_BOLD)  # Title pt.1
    screen.addstr(0, 25, "Made by Andrew Combs", curses.color_pair(2))  # Title pt.2

    textpad.rectangle(screen, 1, 1, y - 4, x - 26)  # Main box for the AI typing back to you
    textpad.rectangle(screen, 1, 1, y - 2, x - 26)  # Text box for typing things and communicating
    textpad.rectangle(screen, 1, x - 26, y - 2, x - 2)  # Info box for things like health, actions, etc.


def load_static_text(screen, y, x):
    # === TITLE === #
    screen.addstr(2, x - 19, "Information", curses.A_BOLD)  # Info title
    # === PLAYER NAME === #
    screen.addstr(5, x - 19, "Sample Name", curses.A_UNDERLINE)  # Info title
    # === HEALTH === #
    screen.addstr(8, x - 24, "Health:", curses.A_BOLD)  # Health title
    screen.addstr(8, x - 16, "||||||||||", curses.color_pair(3))  # Test for the actual health bar. This will be dynamic in the future
    # === MANA === #
    screen.addstr(10, x - 24, "Mana:", curses.A_BOLD)  # Mana title
    screen.addstr(10, x - 18, "||||||||||", curses.color_pair(4))  # Test for the actual mana bar. This will be dynamic in the future
    # === ARMOR === #
    screen.addstr(12, x - 24, "Armor:", curses.A_BOLD)  # Armor title
    screen.addstr(12, x - 17, "|", curses.color_pair(5))  # Test for the actual armor bar. This will be dynamic in the future

    # === PLAYER DESCRIPTION === #
    screen.addstr(15, x - 24, "Description:", curses.A_BOLD)  # Description Title
    screen.addstr(16, x - 24, "This is where the")  # Testing again, this high amount of
    screen.addstr(17, x - 24, "player description")  # new lines will be automated in the
    screen.addstr(18, x - 24, "would go.")  # future


def load_dynamic_text(screen, y, x, view_list):
    # Right now, in order to add colors to the text (as its stored in a list) a # with a number after (indicating the
    # color pair) is added. This may not be the best way of dealing with it, however for now it will work fine. A better
    # solution should be looked at later
    for i, line in enumerate(view_list):
        if line.startswith("#"):
            screen.addstr(y - (5 + i), 2, line[2:], curses.color_pair(int(line[1])))
        else:
            screen.addstr(y - (5 + i), 2, line)


def load_all(screen, y, x, view_list):
    load_frames(screen, y, x)
    load_static_text(screen, y, x)
    load_dynamic_text(screen, y, x, view_list)


def add_text_to_main(text, view_list, color_pair=1):
    # Right now, in order to add colors to the text (as its stored in a list) a # with a number after (indicating the
    # color pair) is added. This may not be the best way of dealing with it, however for now it will work fine. A better
    # solution should be looked at later
    if len(view_list) != 24:
        exit("GUI ERROR: What the fuck")
    return_list = ["#" + str(color_pair) + text] + view_list[:23]

    return return_list
