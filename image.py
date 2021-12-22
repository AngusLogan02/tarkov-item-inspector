import cv2
import mss
import numpy as np
#img = cv2.imread("data/raw/6.png")
def getCells():
    with mss.mss() as sct:
        img = np.array(sct.grab(sct.monitors[1]))
        img = np.flip(img[:, :, :3], 2)  # 1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 2
        x1 = 8
        x2 = 72
        y1 = 261
        y2 = 325
        cell = []

        for i in range(0, 11):
            for j in range(0,10):
                imgCropped = img[y1:y2, x1:x2].copy()
                #cv2.imwrite("cell" + str(i) + str(j) + ".png", imgCropped)
                cell.append(imgCropped)
                x1 += 63
                x2 += 63
            x1 = 8
            x2 = 72
            y1 += 63
            y2 += 63
    cell = np.array(cell)
    cell = cell[None, :]
    return cell