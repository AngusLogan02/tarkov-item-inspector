from PIL import Image
import mss
import numpy as np
def getCells():
    # each cell is a 64x64 pixel RGB image
    top = 261
    left = 8
    size = 64
    cell = []
    coord = []
    with mss.mss() as sct:
        for i in range(0,11):
            for j in range(0,10):
                sct_img = sct.grab({"top": top, "left": left, "width": size, "height": size})           # grab desired area of monitor (each cell)
                pilImage = np.array(Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX"))  # turn that image into a numpy array in the format RGB, instead of mss default BGRA
                cell.append(pilImage[None, :])  # reshape the pilImage numpy array to have a "None" value at the start, this is what the model requires
                coord.append((left+32, top+32))
                left+=63
            left = 8
            top+=63
    return cell, coord