import sys
import sc2reader
from pprint import pprint
from math import floor
from jsonexport import *


def formatReplay(replay):
    return """

{filename}
--------------------------------------------
SC2 Version {release_string}
{category} Game, {start_time}
{type} on {map_name}
Length: {game_length}

""".format(**replay.__dict__)


build_times = {
    'scv': 12,
    'mule': 0,
    'marine': 18,
    'marauder': 21,
    'reaper': 32,
    'ghost': 29,
    'hellion': 21,
    'hellbat': 21,
    'widowmine': 21,
    'siegetank': 32,
    'cyclone': 32,
    'thor': 43,
    'viking': 30,
    'medivac': 30,
    'liberator': 43,
    'banshee': 43,
    'raven': 43,
    'battlecruiser': 64,
    'planetaryfortress': 36,
}


# This function takes the data object to save the build order to, and the replay it is pulling information from
# Then does a check to see what kind of event happened, parses the data, then saves it.

def get_build_order(players_object, loaded_replay):

    # Getting lists for each player

    for key in players_object.keys():
        building = []

        for event in loaded_replay.events:
            if event.second > 0:
                if event.name == 'UnitBornEvent':
                    if event.unit_controller.name == players_object[key]['name']:

                        unit_name = event.unit.name
                        born_time = event.second
                        unit_supply = event.unit.supply

                        try:

                            # Born time /1.4 because the built-in seconds are sped up to 1.4 speed, for faster game mode
                            converted_start_time = (born_time/1.4 - build_times[unit_name.lower()])

                            building.append([unit_name, converted_start_time, unit_supply])

                        except KeyError:

                            print(event.unit.name, 'error')

                if event.name == 'UnitInitEvent':

                    if event.unit_controller.name == players_object[key]['name']:

                        unit_name = event.unit.name
                        unit_time = event.second/1.4
                        unit_supply = 0

                        building.append([unit_name, unit_time, unit_supply])

        # Have to sort the build items before doing supply, due to it being out of the "event" order
        players_object[key]['build'] = building
        players_object[key]['build'].sort(key=lambda x: x[1])

        # Creating a supply data point
        supply_count = 12
        for item in players_object[key]['build']:
            item[1] = floor(item[1])
            unit_supply = item[2]
            item[2] = 0 + supply_count
            supply_count += unit_supply

    return players_object


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

    create_path('builds')
    get_build_order(players, replay)
    json_file_creator([players])


if __name__ == '__main__':
    main()