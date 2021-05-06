import cv2
import time

face_cascade = cv2.CascadeClassifier('face_detect_cascade.xml')

cam = cv2.VideoCapture(0)           # Creating the Webcam Instance

pretime = time.time()               # Setting time  

while True:
    isTrue, frame = cam.read()      # Reading the Frames
    
    # Mirror the frame output
    frame = cv2.flip(frame,1)

    # Adding the FPS in video
    newtime = time.time()               # Taking the Current time
    fps = int(1/(newtime-pretime))      # Calculating the FPS
    pretime = newtime                   # Set the previous time
    cv2.putText(frame,                  # text adding to the frame 
                text=str(fps) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    
    # Detecting the face
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    # Creating a box outline for the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the Frame
    cv2.imshow('Output',frame)
    
    # Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()                 # Destroing the windows