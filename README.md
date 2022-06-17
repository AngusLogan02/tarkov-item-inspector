# tarkov-item-inspector
A tool to automatically identify and examine un-examined items from Escape from Tarkov trader inventories. This is a chore at the beginning of wipe and when new trader levels are unlocked, this tool aims to provide a small QoL upgrade.

## How to use
In its current state, the program meets all the goals I had originally set out. In order to use it, run the python script main.py in the background, and then press "Shift+T" to begin the automatic inspection when you are on a desired trader menu.

## Dependencies
- mouse
- keyboard
- time
- win32api
- win32con
- PIL
- mss
- numpy
- keras
- tensorflow
## Goals
- :heavy_check_mark: Use machine learning to identify un-examined items
- :heavy_check_mark: Inspect these items by moving the mouse and clicking on the items in game

## Nice-to-haves
- :x: Would like to include a GUI, however I don't deem it necessary.
- :x: Flea market option
