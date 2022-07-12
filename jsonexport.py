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


def json_file_creator(data):

    file_name = input('What would you like to name the build?')

    with open(f'./builds/{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()


if __name__ == "__main__":
    print('Hello There!')