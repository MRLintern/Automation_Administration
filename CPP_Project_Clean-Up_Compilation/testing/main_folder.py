import os
import json
import shutil
from subprocess import PIPE, run
import sys


APP_DIR_PATTERN = "app"

def find_all_app_paths(source):
    app_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if APP_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                app_paths.append(path)

        break

    return app_paths


def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


def make_json_metadata_file(path, app_dirs):
    data = {
        "Folder_Name": app_dirs,
        "Number_Of_Folders": len(app_dirs)
    }

    with open(path, "w") as f:
        json.dump(data, f)


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    app_paths = find_all_app_paths(source_path)
    new_app_dirs = get_name_from_paths(app_paths, "_app")

    create_dir(target_path)

    for src, dest in zip(app_paths, new_app_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        
    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_app_dirs)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")

    source, target = args[1:]
    main(source, target)
