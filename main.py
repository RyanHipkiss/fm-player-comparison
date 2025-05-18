from classes.Convert import Convert
from prettytable import PrettyTable
import argparse
from typing import List
from classes.Player import  Player
import importlib

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument('numPlayers', help='The number of players to return')
parser.add_argument('position', help='The position you want to compare', nargs="*")
args = parser.parse_args()

# Convert players
convert = Convert('example-data/search.html', 'example-data/search.csv')
players: List[Player] = convert.getPlayers()

fieldNames = list()
for position in args.position:
    fieldNames.append(position)

fieldNames.insert(0, 'Name')
fieldNames.append('Value')
fieldNames.append('Club')

calculatedPlayers = list()
for p in players:
    playerValues = list()
    playerValues.append(p.name)
    for position in args.position:
        moduleName = f"classes.{position}"
        module = importlib.import_module(moduleName)
        classObj = getattr(module, position)
        positionObj = classObj(p)
        playerValues.append(positionObj.getScore())
        playerValues.append(p.transfer_value)
        playerValues.append(p.club)
    calculatedPlayers.append(playerValues)


sorted = sorted(calculatedPlayers, key=lambda x: x[1], reverse=True)[:int(args.numPlayers)]

table = PrettyTable()
table.field_names = fieldNames
table.add_rows(sorted)
print(table)
