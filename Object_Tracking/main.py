import cv2
import time

# * Helping Functions
def printText(frame,massage):
    '''
    This function print the 'massage' to the video frame
    frame:   this is the img on which massage will be printed
    massage: the text that will be printed
    '''
    cv2.putText(frame,
                text='Status:' + massage,
                org=(10,60),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=.8,
                color=(0,100,255),
                thickness=2)

def drawBox(frame,bbox):
    '''
    This function draw a box out side the object
    frame: this is the img on which box will be drawn
    bbox:  coordinates of the drawn box 
    '''
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,0),2)
    printText(frame,"Tracking")

# * Creating Window
windowName = "Tracker Window"
cv2.namedWindow(windowName)

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)           
address = 'http://192.168.0.101:4747/video'
cam.open(address)

# * Creating and Initializing the Tracker
tracker = cv2.legacy_TrackerKCF.create()        # Creating the tracker
isTrue, frame = cam.read()                      # Reading the First frame                     
bbox = cv2.selectROI(windowName,frame,False)    # Selecting the ROI(object)
tracker.init(frame,bbox)                        # Initializing the tracker

# * Video Rolling
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames    
    
    # * Tracking the object and adding the info to the frame
    isFound, bbox = tracker.update(frame)
    if isFound:
        drawBox(frame,bbox)
    else:
        printText(frame,'Lost')
        
    # * Adding the FPS in the Video
    fps = int(1/(time.time() - timer))          # Calculating the FPS
    cv2.putText(frame,                          # Adding the FPS to the frame 
                text=str(int(fps)) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=.8,
                color=(255,0,0),
                thickness=2)

    # * Display the Frame
    cv2.imshow(windowName,frame)

    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                   # Releasing the instance
cv2.destroyAllWindows()         # Destroing all Windows