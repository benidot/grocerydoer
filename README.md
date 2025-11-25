# grocerydoer
grocerydoer is a Python-based grocery list terminal program built for speed, feature intuitiveness and simplicity. gui version tba.

tested on linux and macos. i have no windows devices to test it on


## usage
```bash
python3 ./program/main.py
```

available commands:
```
- help: show command list
- add: goes into adding mode. type nothing to quit
- remove: removes individual items
- export: saves to manfiles/list.txt
- import: loads from manfiles/list.txt
- clear: removes all ticked items
- wipe: removes every item
- recover: loads from a buffer after wipe
- quit: leaves program and saves to manfiles/autosave.txt
- load: loads from manfiles/autosave.txt
- tick: item turns into [x] item
- untick: removes [x]
```
