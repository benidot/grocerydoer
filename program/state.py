from pathlib import Path

baseDir = Path(__file__).resolve().parent

projRoot = baseDir.parent

listFile = projRoot / 'manfiles' / 'list.txt'
autoSaveFile = projRoot / 'manfiles' / 'autosave.txt'

groceryList = []
listBuffer = []
listBackup = []
listAutosave = []
with open(autoSaveFile, 'r') as f:
    listAutosave = f.read().splitlines()