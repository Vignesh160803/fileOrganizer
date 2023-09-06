from os import listdir
from os.path import isfile, join
import os
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


filePath = find_downloads_directory()
if filePath:
    print(f"Downloads directory found: {filePath}")
else:
    print("Downloads directory not found.")

files = [file for file in listdir(filePath) if isfile(join(filePath, file))]

fileList = []
fileType = {}

for file in files:
    filetype = file.split('.')[1]
    if filetype not in fileType:
        fileList.append(filetype)
        newFolder = filePath + "/" + filetype + '_folder'
        fileType[str(filetype)] = str(newFolder)

        if os.path.isdir(newFolder):
            continue
        else:
            os.mkdir(newFolder)

for file in files:
    src = filePath + '/' + file
    filetype = file.split('.')[1]
    if filetype in fileType.keys():
        dest = fileType[str(filetype)]
        shutil.move(src, dest)
    print("Moving ", src + ">>>" + dest)
