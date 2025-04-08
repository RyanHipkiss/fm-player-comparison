from classes.Player import Player
from classes.Convert import Convert
import json
from typing import List
import argparse

parser = argparse.ArgumentParser(description="Example script")
parser.add_argument('numPlayers', help='The number of players to return')
# parser.add_argument('maxCost', help='Max transfer value of the player (upper limit if range)')
parser.add_argument('position', help='The position you want to compare', nargs="?")
args = parser.parse_args()

convert = Convert('example-data/wolves-moneyball-example-player-list.html', 'example-data/wolves-moneyball-example-player-list.csv')
players = convert.getCsvContent()

examplePlayers: List[Player] = []

for p in players:
    examplePlayers.append(Player(p))

playerT = list()

for p in examplePlayers:
    if args.position is not None and args.position not in p.position:
        continue

    playerT.append([p.name, p.transfer_value, p.getScore(), p.getXgOverperformance(), p.drb_90, p.shot_pct, p.hdr_pct])

sPlayerT = sorted(playerT, key=lambda x: x[2], reverse=True)
limited = sPlayerT[:int(args.numPlayers)]

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Transfer Value', 'Role Ability', 'xG Overperformance', 'Dribbles per 90', 'Shot %', 'Header %']
table.add_rows(limited)
print(table)
# print(json.dumps(examplePlayers[82].getData(), indent=2))