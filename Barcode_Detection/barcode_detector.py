import cv2
import numpy as np
from pyzbar.pyzbar import decode

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)           

# * Start the Video
while True:
    isTrue, frame = cam.read()      # Reading the Frames
    
    # * Detecting and decoding the barcodes
    for code in decode(frame):
        # * Decoding the data from barcode and putting into the frame
        data = code.data.decode('utf-8')    # Getting the data from the barcode
        x, y = code.rect[0:2]           # Getting the cordinates of the barcode
        cv2.putText(img = frame,            # Printing the data into the frame    
                    text = str(data),
                    org = (x,y-5),
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale= .75,
                    color = (50,205,0),
                    thickness = 2)

        # * Ceating the boundinng box
        bound_pts = np.array(code.polygon,np.int32)   # Getting the polygon lines
        bound_pts = bound_pts.reshape((-1,1,2))       # Reshaping the points
        cv2.polylines(img = frame,                    # Drawing the Polygon lines into he frame 
                      pts = [bound_pts],
                      isClosed = True, 
                      color = (240,70,255),
                      thickness = 2)

    # *  Display the Frame
    cv2.imshow('Output',frame)
    
    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()             # Destroing the windows
