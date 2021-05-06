import numpy as np
import cv2

def stackImage(scale,imglist):

    # Setting the Size
    height,width = imglist[0].shape[0:2]
    size = (int(width * scale),int(height * scale))
    
    for i in range(len(imglist)):
        if len(imglist[i].shape) == 2:
            imglist[i] = cv2.cvtColor(imglist[i],cv2.COLOR_GRAY2BGR)
        imglist[i] = cv2.resize(imglist[i],size)
    
    # stacking the output
    if len(imglist) == 3:
        stackimgs = np.hstack([imglist[0],imglist[1],imglist[2]])
    else:
        stackimgs = np.vstack([np.hstack([imglist[0],imglist[1],imglist[2]]),np.hstack([imglist[3],imglist[4],imglist[5]])])
    
    return stackimgs

    