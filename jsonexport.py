import json
import os
from glob import glob
from pathlib import Path


# This will check if the path you want to use exists, and if it doesn't, will create it
def create_path(folder_name):
    dir_name = Path(folder_name)
    if dir_name.is_dir():
        return dir_name
    else:
        os.mkdir(Path(folder_name))
        return dir_name


# Player 2 is not required, could be a solo game for testing
def json_file_creator(player1, player2=None):

    if player2:
        players = [player1, player2]
        print(players)
    else:
        players = [player1]

    for player in players:
        file_name = input(f'What would you like to name the build for {player["name"]}?')

        # Saving a build order for player1
        with open(f'./builds/{file_name}{player["name"]}.json', 'w', encoding='utf-8') as f:
            json.dump(player, f, ensure_ascii=False, indent=4)
            f.close()

        # Saving Creating a build order for player2


if __name__ == "__main__":
    print('Hello There!')