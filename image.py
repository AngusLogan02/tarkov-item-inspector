from PIL import Image
import mss
import numpy as np
def getCellsPIL():
    top = 261
    left = 8
    size = 64
    bruh = 0
    cell = []
    with mss.mss() as sct:
        for i in range(0,11):
            for j in range(0,10):
                sct_img = sct.grab({"top": top, "left": left, "width": size, "height": size})
                pilImage = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX"))
                cell.append(pilImage[None, :])
                bruh+=1
                left+=63
            left = 8
            top+=63
    return cell