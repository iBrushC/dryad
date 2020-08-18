# =====================================================================================================================
# MAIN SCRIPT:
# The glue that holds all this mess together. everything that is run is run here, and its like a kind of gathering
# for all of the different packages that make up the game.
# =====================================================================================================================

# Basic Imports
import curses
from curses import textpad
import time
import gui as gui
import globalvars as gv
import os

# Outside folder imports
import sys
sys.path.append('F:/Python Projects/dryad/master/actionscript')
from actionscript import hardinterpreter as interpreter


WINDOW_X = 100  # Width of the window
WINDOW_Y = 100  # Height of the window

BACKGROUND = curses.COLOR_BLACK

Active = True  # Determines when the game is running or not

tickspeed = 60  # Also known as framerate. How many times a second a tick is added
tick = 0  # What tick the game is on


# Handles all of the things that need to be done before the game can run
def initialize(screen):
    # Makes sure color works on the terminal
    os.system('color')
    curses.start_color()

    # Visual stuff
    gui.init_colors(BACKGROUND)
    screen.bkgd(' ', curses.color_pair(1))

    # Basic checks to make sure that bad stuff cannot happen (ugly cursor, typing, etc)
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.keypad(True)
    screen.timeout(100)


# Once the game is done, this fixes up all of the things that need to be fixed
def deinitialize(screen):
    curses.echo()
    curses.nocbreak()
    screen.keypad(False)
    curses.curs_set(1)


# Updates the tick
def update():
    global tick

    # Refreshing, clearing, and updating the tick
    tick = 1 + tick * (tick != tickspeed)


# Everything inside here is run on every tick
def game_loop(screen, y, x):
    event = screen.getch()

    # Screen refreshing if the screen has been resized
    if curses.is_term_resized(y, x):
        screen.clear()

    # Colors
    gui.init_colors(BACKGROUND)  # initializes all the colors that are needed

    # ===================================================================
    # Drawing all of the different aspects that make up the frame
    # ===================================================================
    gui.load_all(screen, y, x, gv.scroll_view)

    # handles all of the input for typing
    if event != -1:
        # ===================================================================
        # General input handling for all the non-action buttons (for typing)
        # ===================================================================
        if event >= 11 or event == 32 or event == 33:
            if len(gv.user_input) < 90:
                gv.user_input += str(chr(event))

        # Handling action for enter
        elif event == 10:

            data = interpreter.parse_data(gv.user_input)

            if len(gv.user_input) > 2:
                if data == gv.user_input:
                    gv.scroll_view = gui.add_text_to_main("", gv.scroll_view)
                    gv.scroll_view = gui.add_text_to_main(gv.reference[gv.active_player + 1].name, gv.scroll_view, 6)
                    gv.scroll_view = gui.add_text_to_main(gv.user_input, gv.scroll_view)

                    gv.user_input = ""
                    screen.erase()
                    gui.load_all(screen, y, x, gv.scroll_view)
                else:
                    gv.scroll_view = gui.add_text_to_main("", gv.scroll_view)
                    gv.scroll_view = gui.add_text_to_main("Dungeon Master", gv.scroll_view, 7)
                    gv.scroll_view = gui.add_text_to_main(data, gv.scroll_view)

                    gv.user_input = ""
                    screen.erase()
                    gui.load_all(screen, y, x, gv.scroll_view)

        # Handling action for backspace
        elif event == 8:
            gv.user_input = gv.user_input[:-1]
            screen.erase()
            gui.load_all(screen, y, x, gv.scroll_view)

    # cursor ticking, will be changed/removed in the future, just a test
    cursor_speed = 10
    cursor = "|" * (tick % cursor_speed > cursor_speed / 2) + " " * (tick % cursor_speed < cursor_speed / 2)
    screen.addstr(y - 3, 3, str(gv.user_input + str(cursor)))

    time.sleep(1 / tickspeed)


# This handles everything that happens, including initializing, deinitializing, etc.
def main(screen):
    initialize(screen)

    y, x = screen.getmaxyx()

    while Active:
        update()
        game_loop(screen, y, x)

    deinitialize(screen)


curses.wrapper(main)  # Makes sure nothing breaks horribly, runs the main function
