from classes.Player import Player
from classes.Convert import Convert
import json
from typing import List
import argparse

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument('numPlayers', help='The number of players to return')
parser.add_argument('maxCost', help='Max transfer value of the player (upper limit if range)')
args = parser.parse_args()

convert = Convert('example-data/players.html', 'example-data/players.csv')
players = convert.getCsvContent()

# Test logic to display the stats/attrs of a player
# p = Player(players[0])
# j = json.dumps(p.getData(), indent=2, ensure_ascii=False)
# print(j)

examplePlayers: List[Player] = []

for p in players:
    examplePlayers.append(Player(p))

playerT = list()

for p in examplePlayers:
    if len(playerT) == int(args.numPlayers):
        break

        #Test code to compare strikers
    if 'ST' not in p.position:
        continue

    if p.getValue() > float(args.maxCost):
        continue
    playerT.append([p.name, p.position, p.transfer_value, p.getValue(), p.getScore()])

sPlayerT = sorted(playerT, key=lambda x: x[4], reverse=True)

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Position', 'Value', 'Cost', 'Score']
table.add_rows(sPlayerT)
print(table)