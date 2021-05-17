import cv2
import numpy as np
import face_recognition

def empty(a):
    pass

# * Loading the Image
imgPath = input('Enter the Image Path = ')
img =  cv2.imread(imgPath)
img = cv2.resize(img,(500,550),interpolation=cv2.INTER_LINEAR)

# Creating a Gray scale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)

# Finding the landmarks of face from the image
landmarks = face_recognition.face_landmarks(img)[0]

# Getting the poins only for lips
points = landmarks['top_lip'] + landmarks['bottom_lip']
points = np.array(points)   # converting into numpy array

# Creating a Black background
bg = np.zeros_like(img)

# * Creating the Window
windowName = 'Output'        # Window Name
cv2.namedWindow(windowName)

# * Adding the Track pad
cv2.createTrackbar('R Value',windowName,0,255,empty)
cv2.createTrackbar('G Value',windowName,0,255,empty)
cv2.createTrackbar('B Value',windowName,0,255,empty)

while True:
    # Getting the track pad values
    r = cv2.getTrackbarPos('R Value',windowName)
    g = cv2.getTrackbarPos('G Value',windowName)
    b = cv2.getTrackbarPos('B Value',windowName)

    # Creating the Mask for lips
    mask = cv2.fillPoly(bg,[points],(b,g,r))
    mask = cv2.GaussianBlur(mask,(7,7),7)

    # Adding the Gray image and mask 
    colored_lip = cv2.addWeighted(imgGray,1,mask,.4,0)

    stackimg = np.hstack([img,colored_lip])

    # * Display
    cv2.imshow(windowName,stackimg)
    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break