import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import shutil


def find_downloads_directory():
    download_paths = [
        Path.home() / 'Downloads',
        Path(os.getenv('USERPROFILE')) / 'Downloads',
        Path(os.getenv('HOMEPATH')) / 'Downloads',
    ]

    for path in download_paths:
        if path.is_dir():
            return str(path)

    return None


def main():
    filePath = find_downloads_directory()
    if filePath:
        print(f"Downloads directory found: {filePath}")
    else:
        print("Downloads directory not found.")
        return

    files = [file for file in listdir(filePath) if isfile(join(filePath, file))]

    fileType = {}

    for file in files:
        filetype = file.split('.')[-1]
        if filetype:
            filetype = filetype.lower()  # Convert to lowercase for consistency
            if filetype not in fileType:
                fileType[filetype] = []

            fileType[filetype].append(file)

    for filetype, file_list in fileType.items():
        folder_name = os.path.join(filePath, f"{filetype}_folder")
        os.makedirs(folder_name, exist_ok=True)

        for file in file_list:
            src = os.path.join(filePath, file)
            dest = os.path.join(folder_name, file)

            # Check if the destination file already exists and rename if necessary
            counter = 1
            while os.path.exists(dest):
                base, extension = os.path.splitext(file)
                new_file = f"{base}_{counter}{extension}"
                dest = os.path.join(folder_name, new_file)
                counter += 1

            shutil.move(src, dest)
            print(f"Moving {src} >>> {dest}")


if __name__ == "__main__":
    main()