listFile = 'list.txt'
autoSaveFile = 'autosave.txt'

list = []
listBuffer = []
listBackup = []
listAutosave = []
with open(autoSaveFile, 'r') as f:
    listAutosave = f.read().splitlines()

def addGrocery():
    while True:
        item = input('in add mode. type item or leave empty to quit: ')
        if item in list:
            print('item already in list')
            return
        elif item == '':
            return
        list.append(item)

def removeGrocery():
    item = input('item: ')
    if item in list:
        list.remove(item)
        return
    else:
        print('item not in list')

def exportList():
    print('wip')

def importList():
    with open('list.txt', 'r') as f:
        listBuffer = f.read().splitlines()

    for item in listBuffer:
        list.append(item)

def clearList():
    for item in list:
        listBackup.append(item)
    list.clear()
    return 0

def recoverList():
    whichList = input('which list? autosave or backup? ')
    if whichList == 'autosave':
        eitherList = listBackup
    elif whichList == 'backup':
        eitherList = list
    for item in eitherList:
        list.append(item)
    return 0

def quitProgram():
    print('autosave work in progress')
    quit()

while True:
    for i in range(10):
        print()
    print(list)
    print('commands: quit, add, remove, export, import, help, clear, recover')
    command = input('command: ')

    match command: # i worked at blizzard for 7 years
        case "quit":
            quitProgram()

        case "add":
            addGrocery()

        case "remove":
            removeGrocery()

        case "export":
            exportList()

        case "import":
            importList()

        case "help":
            print("commands: quit, add, remove, export, import, show, help")

        case "clear":
            clearList()

        case "recover":
            recoverList()