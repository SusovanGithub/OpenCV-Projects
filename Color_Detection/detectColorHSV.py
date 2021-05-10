import cv2
import numpy as np

def empty(a):
    pass

# * creating the Window
windowName = 'Color Detection in HSV Space'     # Window Name
cv2.namedWindow(windowName)                     # Window Creation

# * Adding the Track pad
cv2.createTrackbar('HUE min',windowName,0,179,empty)
cv2.createTrackbar('HUE max',windowName,179,179,empty)
cv2.createTrackbar('SAT min',windowName,0,255,empty)
cv2.createTrackbar('SAT max',windowName,255,255,empty)
cv2.createTrackbar('Value min',windowName,0,255,empty)
cv2.createTrackbar('Value max',windowName,255,255,empty)

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)

# * Start Video Rolling
while True:
    isTrue, frame = cam.read()              # Reading the Frames
  
    # * Converting the frame in HSC color space
    framehsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # * Getting the track bar Values  
    h_min = cv2.getTrackbarPos('HUE min',windowName)
    h_max = cv2.getTrackbarPos('HUE max',windowName)
    s_min = cv2.getTrackbarPos('SAT min',windowName)
    s_max = cv2.getTrackbarPos('SAT max',windowName)
    v_min = cv2.getTrackbarPos('Value min',windowName)
    v_max = cv2.getTrackbarPos('Value max',windowName)

    # creating the lower and upper range
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # creating the mask
    mask = cv2.inRange(framehsv,lower,upper)

    # result output
    result = cv2.bitwise_and(frame,frame,mask=mask)

    # stacking the output
    stackimgs = np.hstack([frame,result])

    # * Display
    cv2.imshow(windowName,stackimgs)
    
    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()               # Releasing the instance
cv2.destroyAllWindows()     # Destroing the windows