import stateModel
import image
import mouse
import time

# stateModel.train(550, 200)

model = stateModel.loadModel()
cell, coord = image.getCells()
for i in range(0, len(cell)):
    prediction = model.predict(cell[i])
    score = prediction[0]
    if score > 0.7:
        print("cell " + str(i) + " UNINSPECTED (" + str(int(score*100)) + "% certain)")
        mouse.middleMouse(coord[i][0], coord[i][1])
        time.sleep(0.6)
    else:
        print("cell " + str(i) + " already inspected (" + str(int((1-score)*100)) + "% certain)")