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
    with open(listFile, 'w') as f:
        f.write('\n'.join(list))

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
    for item in listBackup:
        list.append(item)
    return 0

def quitProgram():
    print('autosaving.', end='')
    listAutosave.clear()
    for item in list:
        listAutosave.append(item)
    print('.', end='')
    with open(autoSaveFile, 'w') as f:
        f.write('\n'.join(listAutosave))
    print('.')
    quit()

def loadAutosave():
    for item in listAutosave:
        list.append(item)

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

        case "load":
            loadAutosave()