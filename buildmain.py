from protossbuildgetter import ProtossBuildGetter
import sys
import sc2reader
from zergbuildgetter import *
from buildgetter import *
from jsonexport import *


def main():

    path = sys.argv[1]
    loaded_replay = sc2reader.load_replay(path)

    try:
        players = {
            'player1': {'name': loaded_replay.teams[0].players[0].name,
                        'race': '',
                        'build': []
                        },
            'player2': {'name': loaded_replay.teams[1].players[0].name,
                        'race': '',
                        'build': []
                        },
        }
    except IndexError:
        players = {
            'player1': {'name': loaded_replay.teams[0].players[0].name,
                        'race': '',
                        'build': []
                        },
        }

    # Setting player races
    players['player1']['race'] = loaded_replay.players[0].detail_data['race'].lower()

    try:
        players['player2']['race'] = loaded_replay.players[1].detail_data['race'].lower()
    except:
        pass

    for key in players.keys():

       match players[key]['race']:
           case 'zerg':
               print("It's a wild Zerg")
           case 'terran':
               print("WTF a TERRAN?")
           case 'protoss':
               print('FUCK, INVISIBLE MEN INC')


    # create_path('builds')
    # get_build_order(players, replay)
    #
    # player1 = players['player1']
    # try:
    #     player2 = players['player2']
    # except KeyError:
    #     player2 = ""
    #
    # json_file_creator(player1, player2)


if __name__ == '__main__':
    main()