import cv2
import time

# A empty function
def empty(a):
    pass

# * Loading the classifier
face_cascade = cv2.CascadeClassifier('face_detect_cascade.xml')

# * Creating a Window
windowName = "Output"
cv2.namedWindow(windowName)

#  Creating the trackpad
# cv2.createTrackbar('Scale Factor',windowName,1.1,9,empty)
# cv2.createTrackbar('Min Neighbors',windowName,1,10,empty)

cam = cv2.VideoCapture(0)           # Creating the Webcam Instance
# address = 'http://192.168.0.101:8080/video'
# cam.open(address)

# Recording Starts
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
    
    # * Mirror the frame output
    frame = cv2.flip(frame,1)
    
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # # Getting the track bar values
    # scale = cv2.getTrackbarPos('Scale Factor',windowName) + 1     # Scale Factor
    # minNgh = cv2.getTrackbarPos('Min Neighbors',windowName)       # Min Neighbors

    scale = 1.09
    minNgh = 4

    # * Detecting the face
    faces = face_cascade.detectMultiScale(frameGray,scale,minNgh)
    # Creating a box outline for the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # * Adding the FPS in the Video
    fps = int(1/(time.time() - timer))          # Calculating the FPS
    cv2.putText(frame,                          # Adding the FPS to the frame 
                text=str(fps) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    
    # * Display the Frame
    cv2.imshow(windowName,frame)

    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()             # Destroing the windows