from json import loads
from db import db
from discord import Embed

actions = loads(open("act/acts.json").read())

def doaction(command, country):
    if command == None or not command in actions:
        embed = Embed(title = f"Not a valid command",
                      description = "booooo",
                      color = 0xff0000)
        return embed

    if db[country] == 0:
        embed = Embed(title = f"{country} performs **{command}**",
                      description = "yippee!",
                      color = 0xfa6607)

        db[country] = actions[command]["turns"] + 1

    else:
        embed = Embed(title = f"Not your turn, silly",
                      description = f"you have {db[country]} turns left POOPOO360",
                      color = 0xff0000)

        for country in db.keys():
            above = False
            if db[country] > 0:
                print("switching above")
                db[country] -= 1
                above = True

            if above == False:
                db["month"] += 1

                embed = Embed(title = f"Month {db['month']}",
                             description = "make your move y'all",
                             color = 0xfa6607)

    return embed
