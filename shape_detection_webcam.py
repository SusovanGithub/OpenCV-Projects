import cv2
import numpy as np

def empty(a):
    pass

def getContours(img,output_img):
    contours,hierachy =  cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        areaMin = cv2.getTrackbarPos('Min Area',windowName)
        area = cv2.contourArea(cnt)
        if area > areaMin:
            cv2.drawContours(output_img,cnt,-1,(255,0,255),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(output_frame, (x,y), (x+w,y+h), (0,255,0), 4)
            cv2.putText(output_frame, 
                        "Area :" + str(int(area)),
                        (x+w+20,y+20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        .7,
                        (0,255,0))


# creating the Tracpad
windowName = 'Object Detection'        # Window Name
cv2.namedWindow(windowName)         # Window Creation

# adding the Track pad
cv2.createTrackbar('Threshold 1',windowName,0,255,empty)
cv2.createTrackbar('Threshold 2',windowName,0,255,empty)
cv2.createTrackbar('Min Area',windowName,5000,30000,empty)


cam = cv2.VideoCapture(0)           # Creating the Webcam Instance

# address = 'http://192.168.0.100:4747/video'
# cam.open(address)


# Start Video Rolling
while True:
    isTrue, frame = cam.read()              # Reading the Frames
    frame = cv2.resize(frame,(640,480))
    
    # Mirror the image output
    # frame = cv2.flip(frame,1)

    output_frame = frame.copy()
    
    # Blurring the frame
    frameBlur = cv2.GaussianBlur(frame,(5,5),3)
    
    # converting into gray scale
    frameGray = cv2.cvtColor(frameBlur,cv2.COLOR_BGR2GRAY)

    # using the Canny
    threshold1 = cv2.getTrackbarPos('Threshold 1',windowName)
    threshold2 = cv2.getTrackbarPos('Threshold 2',windowName)
        
    frameCanny = cv2.Canny(frameGray,threshold1,threshold2)

    # diloation
    kernel = np.ones((5,5))
    frameDilate = cv2.dilate(frameCanny,kernel,iterations=1)
    
    getContours(frameDilate,output_frame)

    # Display
    cv2.imshow(windowName,output_frame)

    # Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()               # Releasing the instance
cv2.destroyAllWindows()     # Destroing the windows