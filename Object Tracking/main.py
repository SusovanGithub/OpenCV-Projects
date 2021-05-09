import cv2
import time


def printText(frame,massage):
    # Adding the Massage to the frame
    cv2.putText(frame, 
                text='Status:' + massage,
                org=(10,60),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=.8,
                color=(0,100,255),
                thickness=2)

def drawBox(frame,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,0),2)
    printText(frame,"Tracking")

# * Creating Window
windowName = "Output"
cv2.namedWindow(windowName)

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)           
address = 'http://192.168.0.100:4747/video'
cam.open(address)

# * Tracker Adding
tracker = cv2.legacy_TrackerKCF.create()

# Reading the First frame
isTrue, frame = cam.read()                      
# Mirror the frame output
frame = cv2.flip(frame,1)

bbox = cv2.selectROI(windowName,frame,False)
tracker.init(frame,bbox)

# * Video Rolling
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
        
    # Mirror the frame output
    frame = cv2.flip(frame,1)

    # * Tracking the object
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