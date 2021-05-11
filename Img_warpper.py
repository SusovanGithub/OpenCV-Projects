import cv2
import numpy as np

# ! Global Variables
pts1 = np.zeros((4,2))
counter = 0

# *
def onClick(event,x,y,flag,params):
    global circle,counter
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pts1[counter] = x,y
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        counter = counter + 1

cv2.setMouseCallback(windowName,onClick)

img = cv2.imread('images/book3.jpeg')

while True:
    if counter == 4:
        widht,height = 300,400
        pts1 = np.float32([pts1[0],pts1[1],pts1[2],pts1[3]])
        pts2 = np.float32([[0,0],[widht,0],[0,height],[widht,height]])
        matix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOut = cv2.warpPerspective(img,matix,(widht,height))
        cv2.imshow('Result',imgOut)
    
    cv2.imshow(windowName,img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()