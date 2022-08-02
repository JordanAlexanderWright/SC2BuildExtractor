from extractorscripts.protossbuildgetter import ProtossBuildGetter
from sys import argv
import sc2reader
from extractorscripts.zergbuildgetter import ZergBuildGetter
from extractorscripts.terranbuildgetter import *
from data.jsonexport import *

# def format_replay(replay):
#     return """
#
# {filename}
# --------------------------------------------
# SC2 Version {release_string}
# {category} Game, {start_time}
# {type} on {map_name}
# Length: {game_length}
#
# """.format(**replay.__dict__)


def main():

    path = argv[1]
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

    # This for loops takes each player, matches their race to a case, then runs the appropriate build extractor
    for key in players.keys():

        match players[key]['race']:

            case 'zerg':
                build_extractor = ZergBuildGetter(loaded_replay, players[key])
                players[key] = build_extractor.get_build_order()

            case 'terran':
                build_extractor = TerranBuildGetter(loaded_replay, players[key])
                players[key] = build_extractor.get_build_order()

            case 'protoss':
                build_extractor = ProtossBuildGetter(loaded_replay, players[key])
                players[key] = build_extractor.get_build_order()

    create_path('builds')

    player1 = players['player1']
    try:
        player2 = players['player2']
    except KeyError:
        player2 = ""

    json_file_creator(player1, player2)


if __name__ == '__main__':
    main()