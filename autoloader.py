import pathlib
import os


def loader(projectFolder, FileOrFolder):
    if projectFolder[0] != '\\':
        projectFolder = '\\' + projectFolder

    if FileOrFolder[0] != '\\':
        FileOrFolder = '\\' + FileOrFolder

    homePath = str(pathlib.Path.cwd())
    homePath = homePath.partition(f'{projectFolder}')[0]
    homePath += projectFolder
    listSubdirectories = [x[0] for x in os.walk(homePath)]

    for i in range(len(listSubdirectories)):
        if os.path.exists(listSubdirectories[i] + FileOrFolder):
            return listSubdirectories[i] + FileOrFolder

    FileOrFolder = FileOrFolder.replace('\\', '')
    projectFolder = projectFolder.replace('\\', '')
    raise ValueError(f"Could not find a {FileOrFolder} file in {projectFolder} folder")
