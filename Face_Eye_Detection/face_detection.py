import cv2
import time

# * Loading the classifier
face_cascade = cv2.CascadeClassifier(cv2.haarcascades+'haarcascade_frontalface_default.xml')

# * Creating a Window
windowName = "Face Detection"
cv2.namedWindow(windowName)

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)

# Recording Starts
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
    
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # converting into gray scale

    # * Detecting the face
    scale = 1.09
    minNgh = 4
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