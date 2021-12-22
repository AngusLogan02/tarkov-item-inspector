import stateModel
import image
import cv2

#stateModel.train(550, 20)

model = stateModel.loadModel()
cell = image.getCells()
test = cell[0]
prediction = model.predict(test)
score = prediction[0]
if score > 0.7:
    print("UNINSPECTED (" + str(int(score*100)) + "% certain)")
else:
    print("already inspected (" + str(int((1-score)*100)) + "% certain)")