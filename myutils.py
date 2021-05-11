import numpy as np
import cv2
import os

# * Custom functions for a better support in Project utilisation

def stackImage(scale,imglist,row=1,col=None):
    '''
    this function stack the images 
    '''
    # Setting the Size for indivisual images
    height,width = imglist[0].shape[0:2]
    size = (int(width * scale),int(height * scale))

    # Converting all images in samle scale 
    for i in range(len(imglist)):
        if len(imglist[i].shape) == 2:
            imglist[i] = cv2.cvtColor(imglist[i],cv2.COLOR_GRAY2BGR)
        imglist[i] = cv2.resize(imglist[i],size)
    
    stackimgs = []

    # Stacking the Images 
    if col == None:
        stackimgs = np.hstack(imglist)
    else:
        for i in range(row):
            stackimgs.append(np.hstack(imglist[(col*i):(col*i+col)]))
        stackimgs = np.vstack(stackimgs)
    
    return stackimgs

if __name__ == "__main__":
    path = 'Assets/'
    img_list=[]
    for img_name in os.listdir(path):
        if '.gif' in img_name:      # Excluding the Other .gif files 
            continue
        img_list.append(cv2.imread(path+img_name))
    
    stackimg = stackImage(scale=.2, imglist=img_list, row=8, col=1)
    cv2.imshow('Stacked Output',stackimg)
    cv2.waitKey(0)