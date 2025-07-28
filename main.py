list = []

def addGrocery():
    item = input('item: ')
    if item in list:
        print('item already in list')
        return
    list.append(item)

def removeGrocery():
    item = input('item:')
    if item in list:
        list.remove(item)
        return
    else:
        print('item not in list')

def exportList():
    print('wip')

def importList():
    print('wip')

def showList():
    try:
        print(list)
        return 0
    except:
        print('error')
        return 1

while True:
    print('commands: quit, add, remove, export, import, show, help')
    command = input('command: ')

    match command: # i worked at blizzard for 7 years
        case "quit":
            break

        case "add":
            addGrocery()
            print("done")

        case "remove":
            removeGrocery()
            print("done")

        case "export":
            exportList()
            print("done")

        case "import":
            importList()
            print("done")

        case "show":
            showList()
            print("done")

        case "help":
            print("commands: quit, add, remove, export, import, show, help")
            print("done")