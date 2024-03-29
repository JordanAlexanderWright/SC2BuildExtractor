from math import floor


class ZergBuildGetter:
    def __init__(self, loaded_replay, player):

        self.build_times = {
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

        self.upgrade_times = {
            'zergmeleeweaponslevel1': 114,
            'zergmeleeweaponslevel2': 136,
            'zergmeleeweaponslevel3': 157,
            'zergmissileweaponslevel1': 114,
            'zergmissileweaponslevel2': 136,
            'zergmissileweaponslevel3': 157,
            'zerggroundarmorslevel1': 114,
            'zerggroundarmorslevel2': 136,
            'zerggroundarmorslevel3': 157,
            'zergflyerarmorslevel1': 114,
            'zergflyerarmorslevel2': 136,
            'zergflyerarmorslevel3': 157,
            'zergflyerweaponslevel1': 114,
            'zergflyerweaponslevel2': 136,
            'zergflyerweaponslevel3': 157,
            'zerglingmovementspeed': 79,
            'glialreconstitution': 79,
            'evlovegroovedspines': 71,
            'infestorenergyupgrade': 57,
            'overlordspeed': 43,
            'tunnelingclaws': 79,
            'evolvemuscularaugments': 71,
            'zerglingattackspeed': 93,
            'burrow': 71,
            'lurkerrange': 57,
            'chitinousplating': 79,
            'anabolicsynthesis': 43,
            'centrifugalhooks': 79,
            'neuralparasite': 79,
            'adaptivetalons': 57
        }
        # Lair: 57
        # Greater Spire: 71

        self.player = player
        self.loaded_replay = loaded_replay

    # This function takes the data object to save the build order to, and the replay it is pulling information from
    # Then does a check to see what kind of event happened, parses the data, then saves it.

    def get_build_order(self):

        building = []

        for event in self.loaded_replay.events:

            if event.second > 0:

                if event.name == 'CameraEvent' or event.name == 'GetControlGroupEvent' or event.name == 'SelectionEvent':
                    pass

                if event.name == 'UpgradeCompleteEvent':
                    # if event.unit_controller.name == players_object[key]['name']:
                    name = event.upgrade_type_name

                    if name.lower() in self.upgrade_times:

                        upgrade_name = name
                        upgrade_time = (event.second / 1.4) - self.upgrade_times[name.lower()]
                        upgrade_supply = 0

                        building.append([upgrade_name, upgrade_time, upgrade_supply])

                if event.name == 'UnitBornEvent':
                    if event.unit_controller.name == self.player['name']:

                        unit_name = event.unit.name
                        born_time = event.second
                        unit_supply = event.unit.supply

                        try:

                            # Born time /1.4 because the built-in seconds are sped up to 1.4 speed,
                            # for faster game mode
                            converted_start_time = (born_time / 1.4 - self.build_times[unit_name.lower()])
                            building.append([unit_name, converted_start_time, unit_supply])

                        except:
                            pass

                if event.name == 'UnitInitEvent':
                    if event.unit_controller.name == self.player['name']:
                        unit_name = event.unit.name
                        unit_time = event.second / 1.4
                        unit_supply = 0

                        building.append([unit_name, unit_time, unit_supply])

                try:
                    name = event.ability.name
                    if 'Lair' in name or 'Hive' in name:

                        upgrade_name = name
                        upgrade_time = event.second / 1.4
                        upgrade_supply = 0

                        building.append([upgrade_name, upgrade_time, upgrade_supply])

                except AttributeError:
                    pass

        # Have to sort the build items before doing supply, due to it being out of the "event" order
        self.player['build'] = building
        self.player['build'].sort(key=lambda x: x[1])

        # Creating a supply data point
        supply_count = 12
        for item in self.player['build']:
            item[1] = floor(item[1])
            unit_supply = item[2]
            item[2] = 0 + supply_count
            supply_count += unit_supply

        return self.player


def main():

    print('nope!!')
    # path = sys.argv[1]
    # replay = sc2reader.load_replay(path)
    #
    # try:
    #     players = {
    #         'player1': {'name': replay.teams[0].players[0].name,
    #                     'race': '',
    #                     'build': []
    #                     },
    #         'player2': {'name': replay.teams[1].players[0].name,
    #                     'race': '',
    #                     'build': []
    #                     },
    #     }
    # except IndexError:
    #     players = {
    #         'player1': {'name': replay.teams[0].players[0].name,
    #                     'race': '',
    #                     'build': []
    #                     },
    #     }
    #
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