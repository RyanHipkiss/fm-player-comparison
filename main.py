from classes.Player import Player
from classes.Convert import Convert
import json

convert = Convert('example-data/players.html', 'example-data/players.csv')
players = convert.getCsvContent()

# Test logic to display the stats/attrs of a player
p = Player(players[0])
j = json.dumps(p.getData(), indent=2, ensure_ascii=False)
print(j)