import stateModel
import image

#stateModel.train(550, 20)

model = stateModel.loadModel()
cell = image.getCells()
for i in range(0, len(cell)):
    prediction = model.predict(cell[i])
    score = prediction[0]
    if score > 0.7:
        print("UNINSPECTED (" + str(int(score*100)) + "% certain)")
    else:
        print("already inspected (" + str(int((1-score)*100)) + "% certain)")