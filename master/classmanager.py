# =====================================================================================================================
# CLASS MANAGER SCRIPT:
# This one managers all of the classes that need to be made, which is very few as I do not want to restrict how players
# interact with the world. Player and Location are separate from Object, since both have to store "memory".
# =====================================================================================================================


class Player:
    # ======================================= #
    # PLAYER CLASS: What do you think it does #
    # ======================================= #

    # Public variables, can be seen in the GUI and used for actual gameplay
    name = "Player"
    hp = 100
    armor = 0
    strength = 0
    dexterity = 0
    constitution = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    # Hidden variables, used for the AI to make more educated and personal comments
    exhaustion = 0
    happiness = 0
    temper = 0
    temperature = 0

    # This memory is to allow the AI to "point things out". For example, if a player makes the same move
    # 20 times in a row then does something different, the AI can point that out in surprise as a normal human would
    memory = [""] * 20

    # ========= #
    # Functions #
    # ========= #
    def __init__(self, name, hp, armor, strength, dexterity, constitution, intelligence, wisdom, charisma,
                 exhaustion=0, happiness=50, temper=0, temperature=70):
        # God this took a long time
        self.name = name
        self.hp = hp
        self.armor = armor
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.exhaustion = exhaustion
        self.happiness = happiness
        self.temper = temper
        self.temperature = temperature


class Object:
    # ============================================================ #
    # OBJECT CLASS: Handles information for all non-player objects #
    # ============================================================ #

    name = "Object"  # Remember, this could be anything (trees, NPCs, mountains, houses, etc)

    # Variables used for consistently acting on objects and identifying what they are. None are visible to the player,
    # So they just think that I am much better at making AI than I actually am
    health = 100
    exhaustion = 0
    happiness = 0
    temper = 0
    temperature = 0

    # ========= #
    # Functions #
    # ========= #
    def __init__(self, health, exhaustion, happiness, temper, temperature):
        self.health = health
        self.exhaustion = exhaustion
        self.happiness = happiness
        self.temper = temper
        self.temperature = temperature


class Location:
    # ========================================= #
    # LOCATION CLASS: What do you think it does #
    # ========================================= #

    name = "Location"

    # The map maker script will eventually create a hidden virtual map to make sure gameplay is consistent. One of the
    # ways to make sure something is consistent is by keeping a relative location of everything on the map.
    relx = 0
    rely = 0

    # This will be available for players to see and will help the AI make informed comments and decision
    climate = "Normal"
    biome = "Plains"

    # Each location will have a set amount of things in it that will stay constant. This is again for consistency.
    surroundings = [Object] * 50

    # ========= #
    # Functions #
    # ========= #
    def __init__(self, x, y, climate, biome, surroundings):
        self.relx = x
        self.rely = y
        self.climate = climate
        self.biome = biome
        self.surroundings = surroundings

