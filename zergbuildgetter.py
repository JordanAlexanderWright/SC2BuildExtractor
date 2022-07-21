import sys
import sc2reader
from pprint import pprint
from math import floor
from jsonexport import *


def format_replay(replay):
    return """

{filename}
--------------------------------------------
SC2 Version {release_string}
{category} Game, {start_time}
{type} on {map_name}
Length: {game_length}

""".format(**replay.__dict__)


build_times = {
    'drone': 12,
    'queen': 36,
    'zergling': 17,
    'baneling': 14,
    'roach': 19,
    'ravager': 9,
    'hydralisk': 24,
    'lurker': 18,
    'infestor': 36,
    'swarmhost': 29,
    'ultralisk': 39,
    'overlord': 18,
    'overseer': 12,
    'mutalisk': 24,
    'corruptor': 29,
    'viper': 29,
    'broodlord': 24,
    'spinecrawler': 36,
    'sporecrawler': 21,
}

upgrade_times = {

    'zergmeleeweaponslevel1': 'Melee Attacks +1',
    'zergmeleeweaponslevel2': 'Melee Attacks +2',
    'zergmeleeweaponslevel2': 'Melee Attacks +3',
    'zergmissileweaponslevel1': 'Missile Attacks +1',
    'zergmissileweaponslevel2': 'Missile Attacks +2',
    'zergmissileweaponslevel3': 'Missile Attacks +3',
    'zerggroundarmorslevel1': 'Ground Carapace +1',
    'zerggroundarmorslevel2': 'Ground Carapace +2',
    'zerggroundarmorslevel3': 'Ground Carapace +3',
    'zergflyerarmorslevel1': 'Flyer Carapace +1',
    'zergflyerarmorslevel2': 'Flyer Carapace +2',
    'zergflyerarmorslevel3': 'Flyer Carapace +3',
    'zergflyerweaponslevel1': 'Flyer Attacks +1',
    'zergflyerweaponslevel2': 'Flyer Attacks +2',
    'zergflyerweaponslevel3': 'Flyer Attacks +3',
    'zerglingmovementspeed': 'Metabolic Boost',
    'glialreconstitution': 'Glial reconstitution',
    'evlovegroovedspines': 'Grooved Spines',
    'infestorenergyupgrade': 'Pathogen Glands',
    'overlordspeed': 'Pneumatized Carapzce',
    'tunnelingclaws': 'Tunneling Claws',
    'evolvemuscularaugments': 'Muscular Augments',
    'zerglingattackspeed': 'Adrenal Glands',
    'burrow': 'Burrow',
    'lurkerrange': 'Seismic Spines',
    'chitinousplating': 'Chitinous Plating',
    'anabolicsynthesis': 'Anabolic Synthesis',
    'centrifugalhooks': 'Centrifugal Hooks'
}


# This function takes the data object to save the build order to, and the replay it is pulling information from
# Then does a check to see what kind of event happened, parses the data, then saves it.

def get_build_order(players_object, loaded_replay):

    # Getting lists for each player

    for key in players_object.keys():
        building = []
        upgrade_list = []
        for event in loaded_replay.events:

            if event.second > 0:

                if event.name == 'CameraEvent' or event.name == 'GetControlGroupEvent' or event.name == 'SelectionEvent':
                    pass

                if event.name == 'UpgradeCompleteEvent':

                    name = event.upgrade_type_name

                    if name.lower() in upgrade_times:

                        print(name)
                        pprint(dir(event))
                        print(event.count)
                        upgrade_name = name
                        upgrade_time = event.second / 1.4
                        upgrade_supply = 0

                        building.append([upgrade_name, upgrade_time, upgrade_supply])
                    # print([upgrade_name, upgrade_time, upgrade_supply])

                # except AttributeError:
                #     pass
                # try:
                #     name = event.ability.name
                #
                #     # if "Research" in name or "Upgrade" in name:
                #     #     # print(name)
                #     upgrade_name = name
                #     upgrade_time = event.second / 1.4
                #     upgrade_supply = 0
                #
                #     building.append([upgrade_name, upgrade_time, upgrade_supply])
                #     print([upgrade_name, upgrade_time, upgrade_supply])
                #
                # except AttributeError:
                #     pass


                # if event.name == 'UnitBornEvent':
                #     if event.unit_controller.name == players_object[key]['name']:
                #
                #         unit_name = event.unit.name
                #         born_time = event.second
                #         unit_supply = event.unit.supply
                #
                #         try:
                #
                #             # Born time /1.4 because the built-in seconds are sped up to 1.4 speed,
                #             # for faster game mode
                #             converted_start_time = (born_time / 1.4 - build_times[unit_name.lower()])
                #
                #             # building.append([unit_name, converted_start_time, unit_supply])
                #             print([unit_name, converted_start_time, unit_supply])
                #
                #         except:
                #             pass















                        # if event.name == 'UnitInitEvent':
                        #     if event.unit_controller.name == players_object[key]['name']:
                        #         unit_name = event.unit.name
                        #         unit_time = event.second / 1.4
                        #         unit_supply = 0
                        #
                        #         # building.append([unit_name, unit_time, unit_supply])
                        #         print([unit_name, unit_time, unit_supply])

    #
    #             try:
    #                 if event.name == 'UnitBornEvent':
    #                     if event.unit_controller.name == players_object[key]['name']:
    #
    #                         unit_name = event.unit.name
    #                         born_time = event.second
    #                         unit_supply = event.unit.supply
    #
    #                         try:
    #
    #                             # Born time /1.4 because the built-in seconds are sped up to 1.4 speed,
    #                             # for faster game mode
    #                             converted_start_time = (born_time/1.4 - build_times[unit_name.lower()])
    #
    #                             building.append([unit_name, converted_start_time, unit_supply])
    #                             print([unit_name, converted_start_time, unit_supply])
    #
    #                         except KeyError:
    #                             pass
    #
    #             except AttributeError:
    #                 pass
    #
    #     # Have to sort the build items before doing supply, due to it being out of the "event" order
    #     players_object[key]['build'] = building
    #     players_object[key]['build'].sort(key=lambda x: x[1])
    #
    #     # Creating a supply data point
    #     supply_count = 12
    #     for item in players_object[key]['build']:
    #         item[1] = floor(item[1])
    #         unit_supply = item[2]
    #         item[2] = 0 + supply_count
    #         supply_count += unit_supply
    #
    # return players_object
    #

def main():

    path = sys.argv[1]
    replay = sc2reader.load_replay(path)

    try:
        players = {
            'player1': {'name': replay.teams[0].players[0].name,
                        'build': []
                        },
            'player2': {'name': replay.teams[1].players[0].name,
                        'build': []
                        },
        }
    except IndexError:
        players = {
            'player1': {'name': replay.teams[0].players[0].name,
                        'build': []
                        },
        }

    # create_path('builds')
    get_build_order(players, replay)

    player1 = players['player1']
    try:
        player2 = players['player2']
    except KeyError:
        player2 = ""

    # json_file_creator(player1, player2)


if __name__ == '__main__':
    main()