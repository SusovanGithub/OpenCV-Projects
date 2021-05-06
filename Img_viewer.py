import cv2
import os

path = "images/"

for img_name in os.listdir(path):
    img = cv2.imread(path+img_name)
    print(img.shape)
    cv2.imshow('Output',img)
    cv2.waitKey(0)