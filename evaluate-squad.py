from classes.Convert import Convert
from prettytable import PrettyTable
from typing import List
from classes.Player import  Player
import importlib
import statistics

# Convert players
convert = Convert('example-data/squad.html', 'example-data/squad.csv')
convert.convert()
players: List[Player] = convert.getPlayers()


def select_players(data):
    selected_players = set()
    result = []

    for item_key, players_list in data.items():
        # Sort players by score in descending order
        sorted_players = sorted(players_list, key=lambda x: x['score'], reverse=True)

        chosen_player = None
        for player_info in sorted_players:
            if player_info['player'] not in selected_players:
                chosen_player = player_info
                break

        if chosen_player:
            selected_players.add(chosen_player['player'])
            result.append({item_key: chosen_player})
        else:
            # Handle cases where all players for an item are already selected
            # For this problem, we assume there will always be an unselected player
            # or we might add a placeholder like {item_key: "No player available"}
            # For now, we'll just skip if no player can be chosen
            result.append({item_key: {}})  # Or handle as per specific requirement if no player is found

    return result

squad = {
    'SKS': [
        { 'player': '', 'score': 0 }
    ],
    'LWBS': [
        { 'player': '', 'score': 0 }
    ],
    'RWBS': [
        { 'player': '', 'score': 0 }
    ],
    'LBPDD': [
        { 'player': '', 'score': 0 }
    ],
    'RBPDD': [
        { 'player': '', 'score': 0 }
    ],
    'DMS': [
        { 'player': '', 'score': 0 }
    ],
    'SVA': [
        { 'player': '', 'score': 0 }
    ],
    'AMA': [
        { 'player': '', 'score': 0 }
    ],
    'PA': [
        {'player': '', 'score': 0}
    ],
    'CFS': [
        {'player': '', 'score': 0}
    ],
    'F9S': [
        { 'player': '', 'score': 0 }
    ]
}

# need to change this so that, for each player, it gets their best position, and then loops through those to put them into the table correctly.
for key, item in squad.items():
    topScorer = {
        'player': '',
        'score': 0
    }

    for player in players:
        position = key

        if position in ("LWBS", "RWBS", "LBPDD", "RBPDD"):
            position = position[1:]

        moduleName = f"classes.{position}"
        module = importlib.import_module(moduleName)
        classObj = getattr(module, position)
        positionObj = classObj(player)

        playerScore = {
            'player': positionObj.player.name,
            'score': positionObj.getScore()
        }

        squad[key].append(playerScore)

for key, item in squad.items():
    sortedList = sorted(item, key=lambda x: x['score'], reverse=True)
    squad[key] = sortedList

squad = select_players(squad)

table = PrettyTable()
table.field_names = ['Position', 'Starter', 'Score']

rows = []
for item in squad:
    for key, item in item.items():
        row = [key, item['player'], item['score']]
        rows.append(row)
        table.add_row(row)

scores = []
for row in rows:
    scores.append(row[2])

tableTwo = PrettyTable()
tableTwo.field_names = ['Average']
tableTwo.add_row([round(statistics.mean(scores), 1)])

print(table)
print(tableTwo)