# =====================================================================================================================
# VARIABLE SCRIPT:
# This one hols all of the global variables that are relied upon by scripts from everywhere. This is just for tidiness,
# or perhaps I'm making this unintentionally complex by splitting everything up. Who knows?
# =====================================================================================================================

from classmanager import Player, Object, Location

user_input = ""
scroll_view = ["#1Try: '.PLAYER1 &sethp 10.', '.PLAYER1 &setname Joe.', and '.PLAYER4 %setactive.'",
               "#7Dungeon Master (Dryad)",
               "",
               "#1for testing.",
               "#1variables. A basic hard ActionScript, interpreter. See 'rules.txt' and 'hardinterpreter.py'",
               "#1no longer static. Backend updated to contain classes, and a dedicated script for global ",
               "#1Release Notes (Alpha 0.2): Party and dice boxes added. Health, mana, armor, and name are",
               "#7Dungeon Master (Dryad)", "", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", ""]

Player1 = Player("p1", 1, 1, 1, 1, 1, 1, 1, 1)
Player2 = Player("p2", 2, 2, 2, 2, 2, 2, 2, 2)
Player3 = Player("p3", 3, 3, 3, 3, 3, 3, 3, 3)
Player4 = Player("p4", 4, 4, 4, 4, 4, 4, 4, 4)


reference = ["PLAYER1", Player1, "PLAYER2", Player2, "PLAYER3", Player3, "PLAYER4", Player4]

active_player = 0

dice = 20

