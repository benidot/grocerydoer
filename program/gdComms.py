import state

def addGrocery():
    while True:
        item = input('in add mode. type item or leave empty to quit: ')
        if item in state.groceryList:
            print('item already in list')
            return
        elif item == '':
            printer()
            return
        state.groceryList.append(item)

def removeGrocery():
    item = input('item: ')
    if item in state.groceryList:
        state.groceryList.remove(item)
        return
    else:
        print('item not in list')
    printer()

def exportList():
    with open(state.listFile, 'w') as f:
        f.write('\n'.join(state.groceryList))
    printer()

def importList():
    with open(state.listFile, 'r') as f:
        state.listBuffer = f.read().splitlines()

    for item in state.listBuffer:
        state.groceryList.append(item)
    printer()

def clearList():
    for item in state.groceryList[:]:
        if '[x] ' in item:
            state.groceryList.remove(item)
        state.listBackup.append(item)
    return 0
    printer()

def wipeList():
    for item in state.groceryList[:]:
        state.listBackup.append(item)
    state.groceryList.clear()
    return 0
    printer()

def recoverList():
    for item in state.listBackup:
        if item not in state.groceryList:
            state.groceryList.append(item)
    return 0
    printer()

def quitProgram():
    print('autosaving.', end='')
    state.listAutosave.clear()
    for item in state.groceryList:
        state.listAutosave.append(item)
    print('.', end='')
    with open(state.autoSaveFile, 'w') as f:
        f.write('\n'.join(state.listAutosave))
    print('.')
    quit()

def loadAutosave():
    for item in state.listAutosave:
        state.groceryList.append(item)
    printer()

def ticker():
    item = input('item: ')
    if item in state.groceryList:
        state.groceryList.remove(item)
        state.groceryList.append(f'[x] {item}')
    return 0
    printer()

def printer():
    printEmpty()
    printList()

def printEmpty():
    for i in range(11):
        print()

def printList():
    for item in state.groceryList:
        print(item)

def helpPrinter():
    printEmpty()
    print('quit: quit program')
    print('add: add item (bulk)')
    print('remove: remove item')
    print('export: export to list.txt')
    print('import: import from list.txt')
    print('clear: clear ticked items')
    print('wipe: wipe list entirely')
    print('recover: recover list from auto-backup')
    print('load: load autosave')
    print('tick: tick item')