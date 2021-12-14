import cv2
img = cv2.imread("data/1.png")
x1 = 8
x2 = 72
y1 = 261
y2 = 325
cell = []
img = cv2.imread("data/1.png")

for i in range(0, 11):
    for j in range(0,10):
        imgCropped = img[y1:y2, x1:x2].copy()
        cv2.imwrite("cell" + str(i) + "" + str(j) + ".png", imgCropped)
        x1 += 63
        x2 += 63
    x1 = 8
    x2 = 72
    y1 += 63
    y2 += 63
