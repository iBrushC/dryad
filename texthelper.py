# =====================================================================================================================
# TEXTHELPER SCRIPT:
# This may be removed in the future, but for now it will be used to format all the weird text things that occur because
# of the command line interface.
# =====================================================================================================================

import numpy as np


def rollover(text, max_len):
    return_list = []
    return_list = [text[i:i+max_len] for i in range(0, len(text), max_len)]

    return return_list

