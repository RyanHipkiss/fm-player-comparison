from classes.Convert import Convert
import importlib
from prettytable import PrettyTable


class EvaluateSquad:
    squad = {
        'SKS': [
            {'player': '', 'score': 0}
        ],
        'LWBS': [
            {'player': '', 'score': 0}
        ],
        'RWBS': [
            {'player': '', 'score': 0}
        ],
        'LBPDD': [
            {'player': '', 'score': 0}
        ],
        'RBPDD': [
            {'player': '', 'score': 0}
        ],
        'DMS': [
            {'player': '', 'score': 0}
        ],
        'SVA': [
            {'player': '', 'score': 0}
        ],
        'AMA': [
            {'player': '', 'score': 0}
        ],
        'PA': [
            {'player': '', 'score': 0}
        ],
        'CFS': [
            {'player': '', 'score': 0}
        ],
        'F9S': [
            {'player': '', 'score': 0}
        ]
    }

    def __init__(self):
        return

    def getConvertedPlayers(self):
        # Using a more robust path for example data in a real scenario
        # Assuming 'example-data' is a directory at the same level as your script
        convert = Convert('example-data/squad.html', 'example-data/squad.csv')
        convert.convert()

        return convert.getPlayers()

    def getBestPlayersByPosition(self):
        data = self.getPlayerScores(
            self.getConvertedPlayers()
        )
        """
        Identifies the best player for each position as a starter, and then
        the best available player (not chosen as a starter) for each position
        as a backup. No player is reused.

        Args:
            data (dict): A dictionary where keys are positions and values are
                         lists of dictionaries, each containing 'player' and 'score'.

        Returns:
            dict: A dictionary with positions as keys and a dictionary containing
                  'starter' (dict: {'player', 'score'}) and 'backup' (dict: {'player', 'score'}).
        """
        final_selections = {}
        assigned_starters = set()  # To keep track of players chosen as starters

        # Initialize final_selections to preserve position order and structure
        for position in self.squad.keys():
            final_selections[position] = {'starter': None, 'backup': None}

        # --- PHASE 1: Select Starters ---
        # Store all player performances across all positions
        all_performances = []
        for position, players_data in data.items():
            for player_info in players_data:
                if player_info['player']:  # Only consider players with names
                    all_performances.append({
                        'player': player_info['player'],
                        'score': player_info['score'],
                        'position': position
                    })

        # Sort all performances by score in descending order for global starter selection
        all_performances.sort(key=lambda x: x['score'], reverse=True)

        for performance in all_performances:
            player = performance['player']
            position = performance['position']
            score = performance['score']

            if final_selections[position]['starter'] is None and player not in assigned_starters:
                final_selections[position]['starter'] = {'player': player, 'score': score}
                assigned_starters.add(player)

        # --- PHASE 2: Select Backups from remaining players ---
        # Collect all player names from the original data
        all_original_players = set()
        for position, players_data in data.items():
            for player_info in players_data:
                if player_info['player']:
                    all_original_players.add(player_info['player'])

        # Determine available players for backups
        available_players_for_backups = all_original_players.difference(assigned_starters)

        # Now, for each position, find the best backup from the available pool
        for position in self.squad.keys():
            if final_selections[position]['starter'] is not None:  # Only find backup if a starter was assigned
                # Iterate through players for this specific position, sorted by score
                for player_info in sorted(data[position], key=lambda x: x['score'], reverse=True):
                    player = player_info['player']
                    score = player_info['score']

                    # Ensure the player is in the backup pool and hasn't been assigned yet
                    if player and player in available_players_for_backups:
                        final_selections[position]['backup'] = {'player': player, 'score': score}
                        # Remove the player from the available_players_for_backups set
                        # so they aren't used as a backup for another position
                        available_players_for_backups.remove(player)
                        break  # Found a backup for this position, move to the next position

            # Handle cases where a starter might not have been assigned (though less likely with the new logic)
            # and try to find a backup from the available pool.
            elif final_selections[position]['starter'] is None:
                # If no starter was found, the first available player becomes the starter,
                # and the second available becomes the backup. This is a bit of a fall-through
                # for positions that struggled to get a starter in the first pass.
                temp_players_for_position = []
                for player_info in sorted(data[position], key=lambda x: x['score'], reverse=True):
                    player = player_info['player']
                    if player and player in available_players_for_backups:
                        temp_players_for_position.append(player_info)

                if temp_players_for_position:
                    # Assign the best available as starter for this position
                    final_selections[position]['starter'] = temp_players_for_position[0]
                    available_players_for_backups.remove(temp_players_for_position[0]['player'])

                    # Assign the second best available as backup if exists
                    if len(temp_players_for_position) > 1:
                        final_selections[position]['backup'] = temp_players_for_position[1]
                        available_players_for_backups.remove(temp_players_for_position[1]['player'])

        return final_selections

    def getPlayerScores(self, players):
        # Clear existing dummy data in squad
        for key in self.squad:
            self.squad[key] = []

        for key in self.squad.keys():
            for player in players:
                position = key

                if position in ("LWBS", "RWBS", "LBPDD", "RBPDD"):
                    position = position[1:]

                moduleName = f"classes.{position}"
                try:
                    module = importlib.import_module(moduleName)
                    classObj = getattr(module, position)
                    positionObj = classObj(player)

                    playerScore = {
                        'player': positionObj.player.name,
                        'score': positionObj.getScore()
                    }
                    self.squad[key].append(playerScore)
                except (ModuleNotFoundError, AttributeError) as e:
                    # Depending on your setup, you might want to log this or suppress it.
                    # print(f"Warning: Could not import or use class for position {position}: {e}")
                    continue

        for key, item in self.squad.items():
            sortedList = sorted(item, key=lambda x: x['score'], reverse=True)
            self.squad[key] = sortedList

        return self.squad


# Example Usage:
squad = EvaluateSquad()
players_data = squad.getBestPlayersByPosition()

table = PrettyTable()
table.field_names = ['Position', 'Starter', 'Score', 'Back-up', 'Back-up Score']

total_starter_score = 0
num_starters = 0
total_backup_score = 0
num_backups = 0

for position, roles in players_data.items():
    starter_name = roles['starter']['player'] if roles['starter'] else 'N/A'
    starter_score = roles['starter']['score'] if roles['starter'] else 'N/A'
    backup_name = roles['backup']['player'] if roles['backup'] else 'N/A'
    backup_score = roles['backup']['score'] if roles['backup'] else 'N/A'

    table.add_row([position, starter_name, starter_score, backup_name, backup_score])

    if isinstance(starter_score, (int, float)):
        total_starter_score += starter_score
        num_starters += 1

    if isinstance(backup_score, (int, float)):
        total_backup_score += backup_score
        num_backups += 1

# Calculate averages
average_starter_score = total_starter_score / num_starters if num_starters > 0 else 0
average_backup_score = total_backup_score / num_backups if num_backups > 0 else 0

# Append the average row
table.add_row(['---', '---', '---', '---', '---'])  # Separator for clarity
table.add_row([
    '-',
    'Average',
    f'{average_starter_score:.1f}',  # Format to 2 decimal places
    'Average',
    f'{average_backup_score:.1f}'  # Format to 2 decimal places
])

print(table)