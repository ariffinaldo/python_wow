"""
This is the class that will print and return the available commands when the user asks for them

abbreviation PAC means Print Available Commands
"""


def pac_main_ooc():
    print()
    print("Available commands:")
    print("\tengage [Monster Name]")
    print("\t\tEngages in combat with the monster whose name you've entered.\n")
    print("\tprint alive monsters")
    print("\tpav")
    print("\t\tPrints 5 monsters that are alive.\n")
    print("\tprint all alive monsters")
    print("\t\tPrints all monsters that are alive.\n")
    print("\t?")
    print("\t\tShows a list of available commands.\n")


def pac_in_combat():
    print()
    print("Available commands that end the turn:")
    print("\tprint stats")
    print("\t\tPrints information about the character and monster\n")
    print("\tprint xp")
    print("\t\tPrints the experience points of the character and the amount needed to level up\n")
    print("\t?")
    print("\t\tShows a list of available commands.\n")
    print()
    print("Available commands that do not end the turn:")
    print("\tattack")
    print("\t\tAttacks the monster you are in combat with a meele swing.\n")
