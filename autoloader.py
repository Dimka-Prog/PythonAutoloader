import pathlib
import os


def loader(projectFolder, file):
    if projectFolder[0] != '\\':
        projectFolder = '\\' + projectFolder

    if file[0] != '\\':
        file = '\\' + file

    homePath = str(pathlib.Path.cwd())
    homePath = homePath.partition(f'{projectFolder}')[0]
    homePath += projectFolder
    listSubdirectories = [x[0] for x in os.walk(homePath)]

    for i in range(len(listSubdirectories) - 2):
        if os.path.isfile(listSubdirectories[i] + file):
            return listSubdirectories[i] + file

    file = file.replace('\\', '')
    projectFolder = projectFolder.replace('\\', '')
    raise ValueError(f"Could not find a {file} file in {projectFolder} folder")
