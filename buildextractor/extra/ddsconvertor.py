from PIL import Image
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


# Use this to return a list of dds in a file
def get_folder_dds(path):
    files = glob(f"{path}\*.dds")
    print(files)
    return files


def convert_to_png(file, target):
    img = Image.open(file)
    filename = get_filename(file)
    img = img.resize((100, 100))
    img.save(f"{target}\\{filename}.png", format='png')
    img.close()


# This will create a file name (whatever it's already called) for it to be called as a new file
def get_filename(file_path):
    name = str(file_path)
    splits = name.split("\\")
    edited_name = splits[-1]
    edited_name = edited_name[:-4]
    return edited_name


def convertor(dds_path, target_path):

    # Need create paths / check they exist
    dds_files = create_path(dds_path)
    target = create_path(target_path)

    # Need to create a list of files to be converted
    files = get_folder_dds(dds_files)

    for file in files:
        convert_to_png(file, target)


convertor("ddsicons", "Converted_Images")

