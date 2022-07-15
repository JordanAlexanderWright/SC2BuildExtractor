import sc2reader
from pathlib import Path
from math import floor
import sys

def main():
    #
    # path = Path("C:\Users\jaws6\Documents\StarCraft II\Accounts\2257274\1-S2-1-3252282\Replays\Multiplayer\replay2.SC2Replay")
    # replay = sc2reader.load_replay(path)
    #
    # players = {
    #     'player1': {'name': replay.teams[0].players[0].name,
    #                 'build': []
    #                 },
    #     'player2': {'name': replay.teams[1].players[0].name,
    #                 'build': []
    #                 },
    # }

    my_data = {
        1: 1.43,
        2: 1.54
    }

    print(my_data)
    floor(my_data[1])

    my_data[1] = floor(my_data[1])

    print(my_data)
if __name__ == '__main__':
    main()