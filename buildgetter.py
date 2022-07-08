import sys
import sc2reader
from pprint import pprint
from math import floor


def formatReplay(replay):
    return """

{filename}
--------------------------------------------
SC2 Version {release_string}
{category} Game, {start_time}
{type} on {map_name}
Length: {game_length}

""".format(**replay.__dict__)


def get_build_order(players_object, loaded_replay):

    for key in players_object.keys():
        building = []

        for event in loaded_replay.events:

            if event.name == 'UnitInitEvent':

                if event.unit_controller.name == players_object[key]['name']:

                    unit_name = event.unit.name
                    unit_time = floor(event.second/1.4)

                    building.append((unit_name, unit_time))

            if event.name == 'BasicCommandEvent':

                match contains_substring('Train', event.ability_name):
                    case False:
                        pass
                    case True:
                        split_name = event.ability_name.split('Train')
                        unit_name = split_name[1]
                        unit_time = floor(event.second / 1.4)

                        unit_data = (unit_name, unit_time)


                match contains_substring('Build', event.ability_name):
                    case False:
                        pass
                    case True:
                        split_name = event.ability_name.split('Build')
                        unit_name = split_name[1]
                        unit_time = floor(event.second / 1.4)

                        building.append((unit_name, unit_time))

        players_object[key]['build'] = building

    print(players_object)
    return players_object\

def contains_substring(sub_string, parent_string):
    try:
        parent_string.index(sub_string)
        return True
    except:
        return False


def main():

    path = sys.argv[1]
    replay = sc2reader.load_replay(path)

    players = {
        'player1': {'name': replay.teams[0].players[0].name,
                    'build': []
                    },
        'player2': {'name': replay.teams[1].players[0].name,
                    'build': []
                    },
    }

    print(players['player1']['name'])
    print(players['player2']['name'])

    get_build_order(players, replay)


if __name__ == '__main__':
    main()