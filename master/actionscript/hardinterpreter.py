# =====================================================================================================================
# HARD INTERPRETER SCRIPT:
# This is going to be the super simple script used for testing the game. This will likely be replaced with an AI-based
# or AI-incorporated interpreter.
# =====================================================================================================================

import globalvars as gv
import random

test = ".PLAYER1 &roll 20."


def parse_data(actionscript):
    if actionscript.startswith('.') + actionscript.endswith('.') is not 2:
        return actionscript
    if len(actionscript.replace('.', ' ').split(' ')) < 2:
        return actionscript

    elements = actionscript.replace('.', '').split(' ')

    # === RELATIONS === #
    if elements[1].startswith('$'):
        return actionscript

    # === FUNCTIONS === #
    elif elements[1].startswith('%'):
        try:
            reference = gv.reference.index(str(elements[0]))
            code = elements[1][1:]
        except ValueError or IndexError:
            return actionscript

        if code == "setactive":
            gv.active_player = reference
            return str(gv.reference[reference + 1].name + " " + code)

    # === GETTERS === #
    elif elements[1].startswith('&'):

        try:
            reference = gv.reference[gv.reference.index(str(elements[0])) + 1]
            code = elements[1][1:]
            value = elements[2]
        except ValueError or IndexError:
            return actionscript

        if code == "roll":
            gv.dice = random.randrange(0, int(value))
            return str(reference.name + " " + code + " " + str(value))

        elif code == "sethp":
            reference.hp = int(value)
            return str(reference.name + " " + code + " " + str(value))

        elif code == "setarmor":
            reference.armor = int(value)
            return str(reference.name + " " + code + " " + str(value))

        elif code == "setname":
            reference.name = str(value)
            return str(reference.name + " " + code + " " + str(value))

    else:
        return actionscript



