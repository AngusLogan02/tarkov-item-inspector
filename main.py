import stateModel
import image
import mouse
import time
import keyboard
import os

#stateModel.train(550, 200)
print("Loading...")
model = stateModel.loadModel()
os.system("cls")
print("+----------------------------------------------------------------------------------------------+")
print("| Press 'Shift + T' to inspect from a trader's inventory, and 'Shift + Q' to quit the program. |")
print("| Ready to inspect.                                                                            |")
print("+--------------------------------------------------------------------------------------------- +")
print()

def trader():
    print("STARTING TRADER INSPECTION")
    cell, coord = image.getCellsTrader()
    for i in range(0, len(cell)):
        prediction = model.predict(cell[i])
        score = prediction[0]
        if score > 0.7:
            print("cell " + str(i) + " UNINSPECTED (" + str(int(score*100)) + "% certain)")
            mouse.middleMouse(coord[i][0], coord[i][1])
            time.sleep(0.6)
        else:
            print("cell " + str(i) + " already inspected (" + str(int((1-score)*100)) + "% certain)")

keyboard.add_hotkey("shift+t", lambda: trader())
keyboard.wait("shift+q")