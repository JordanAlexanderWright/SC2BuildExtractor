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


def json_file_creator(player1, player2):

    file_name = input('What would you like to name the game?')

    # Saving a build order for player1
    with open(f'./builds/{file_name}{player1["name"]}.json', 'w', encoding='utf-8') as f:
        json.dump(player1, f, ensure_ascii=False, indent=4)
        f.close()

    with open(f'./builds/{file_name}{player2["name"]}.json', 'w', encoding='utf-8') as f:
        json.dump(player2, f, ensure_ascii=False, indent=4)
        f.close()

    # Saving Creating ab uild order for player2


if __name__ == "__main__":
    print('Hello There!')