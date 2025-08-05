import gdComms

commandlist = {
    'quit': gdComms.quitProgram,
    'add': gdComms.addGrocery,
    'remove': gdComms.removeGrocery,
    'export': gdComms.exportList,
    'import': gdComms.importList,
    'clear': gdComms.clearList,
    'wipe': gdComms.wipeList,
    'recover': gdComms.recoverList,
    'load': gdComms.loadAutosave,
    'tick': gdComms.ticker,
    'untick': gdComms.unticker,
    'help': gdComms.helpPrinter
}

gdComms.printer()
while True:
    command = input('enter command: ')
    if command in commandlist: # i worked at blizzard for 8 years
        commandlist[command]()
    else:
        gdComms.printer()
