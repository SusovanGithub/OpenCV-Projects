import cv2
import time

cam = cv2.VideoCapture(0)           # Creating the Webcam Instance

address = 'http://192.168.0.101:4747/video'
cam.open(address)

pretime = time.time()                   # Setting time


while True:
    isTrue, frame = cam.read()      # Reading the Frames

    # frame = cv2.resize(frame,(640,480))

    # Mirror the image output
    frame = cv2.flip(frame,1)

    # Converting into gray space
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Display the FPS in video
    newtime = time.time()               # Taking the Current time
    fps = int((newtime-pretime)*1000)   # Calculating the FPS
    cv2.putText(frame,                  # text adding to the frame 
                text=str(fps) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    pretime = newtime                   # Set the previous time

    # Creating the Exit Pole
    cv2.imshow('Output',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()                 # Destroing the windows