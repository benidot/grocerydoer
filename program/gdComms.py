import state


def addGrocery():
    while True:
        item = input("in add mode. type item or leave empty to quit: ")
        if item in state.groceryList:
            print("item already in list")
            return
        elif item == "":
            printer()
            return
        state.groceryList.append(item)
        state.groceryList.sort()


def removeGrocery():
    item = input("item: ")
    if item in state.groceryList:
        state.groceryList.remove(item)
        state.groceryList.sort()
        return
    else:
        print("item not in list")
    printer()


def exportList():
    with open(state.listFile, "w") as f:
        f.write("\n".join(state.groceryList))
    printer()


def importList():
    with open(state.listFile, "r") as f:
        state.listBuffer = f.read().splitlines()

    for item in state.listBuffer:
        if item not in state.groceryList:
            state.groceryList.append(item)
        state.groceryList.sort()
    printer()


def clearList():
    for item in state.groceryList[:]:
        state.tickedList.clear()
        state.listBackup.append(item)
    printer()


def wipeList():
    isS = input("confirm y/n ")
    if isS != "y":
        return
    for item in state.groceryList[:]:
        state.listBackup.append(item)
    state.groceryList.clear()
    state.tickedList.clear()
    printer()


def recoverList():
    for item in state.listBackup:
        if item not in state.groceryList:
            state.groceryList.append(item)
    printer()


def quitProgram():
    print("autosaving.", end="")
    state.listAutosave.clear()
    for item in state.groceryList:
        state.listAutosave.append(item)
    print(".", end="")
    with open(state.autoSaveFile, "w") as f:
        f.write("\n".join(state.listAutosave))
    print(".")
    quit()


def loadAutosave():
    for item in state.listAutosave:
        if item not in state.groceryList:
            state.groceryList.append(item)
    printer()


def ticker():
    item = input("item: ")
    if item in state.groceryList:
        state.groceryList.remove(item)
        state.tickedList.append(f"[x] {item}")
    printer()


def unticker():
    while True:
        item = input("in untick mode. type item or leave empty to quit: ")
        if item == "":
            printer()
            return
        item = "[x] " + item
        if item in state.tickedList:
            state.tickedList.remove(item)
            splitted = item.split("[x] ")
            item = splitted[1]
        else:
            print("not found")
            return
        state.groceryList.append(item)
        printer()
        return


def printer():
    printEmpty()
    printList()


def printEmpty():
    for i in range(11):
        print()


def printList():
    for index, item in enumerate(state.groceryList):
        print(f"{index + 1} - {item}")
    if len(state.tickedList) > 0:
        print("\nticked: ")
        for index, item in enumerate(state.tickedList):
            print(f"{index + 1} - {item}")


def helpPrinter():
    printEmpty()
    print("quit: quit program")
    print("add: add item (bulk)")
    print("remove: remove item")
    print("export: export to list.txt")
    print("import: import from list.txt")
    print("clear: clear ticked items")
    print("wipe: wipe list entirely")
    print("recover: recover list from auto-backup")
    print("load: load autosave")
    print("tick: tick item")
    print("untick: untick in bulk")
