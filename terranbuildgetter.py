from math import floor


class TerranBuildGetter:

    def __init__(self, loaded_replay, player):

        self.build_times = {
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

        self.player = player
        self.loaded_replay = loaded_replay
# This function takes the data object to save the build order to, and the replay it is pulling information from
# Then does a check to see what kind of event happened, parses the data, then saves it.

    def get_build_order(self):

        building = []

        for event in self.loaded_replay.events:
            if event.second > 0:

                if event.name == 'UnitBornEvent':
                    if event.unit_controller.name == self.player['name']:

                        unit_name = event.unit.name
                        born_time = event.second
                        unit_supply = event.unit.supply

                        try:

                            # Born time /1.4 because the built-in seconds are sped up to 1.4 speed, for faster game mode
                            converted_start_time = (born_time/1.4 - self.build_times[unit_name.lower()])

                            building.append([unit_name, converted_start_time, unit_supply])

                        except KeyError:

                            pass

                if event.name == 'UnitInitEvent':

                    if event.unit_controller.name == self.player['name']:

                        unit_name = event.unit.name
                        unit_time = event.second/1.4
                        unit_supply = 0

                        building.append([unit_name, unit_time, unit_supply])

                try:
                    name = event.ability.name
                    if "Research" in name or "Upgrade" in name or "Terran" in name:
                        if "Orbital" in name or "Planetary" in name:
                            pass
                        else:
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

    print('NOPE')


if __name__ == '__main__':
    main()