from discord import Embed

def helpmessage(command):
    print("qhar")
    embed = Embed(title = f"dars bot: {command}",
                  description = open(f"help/{command}.txt").read(),
                  color = 0xfa6607)
    return embed
