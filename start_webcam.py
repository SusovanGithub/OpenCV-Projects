import cv2
import time

capture = cv2.VideoCapture(0)           # Creating the Webcam Instance

# Setting the Resolution
capture.set(3,640)                      # Width
capture.set(4,480)                      # Height

pretime = time.time()                   # Setting time


while True:
    isTrue, frame = capture.read()      # Reading the Frames
    
    newtime = time.time()               # Taking the Current time
    fps = int((newtime-pretime)*1000)   # Calculating the FPS
    # Display the FPS in video
    cv2.putText(frame,
                text=str(fps) + 'fps',
                org=(10,20),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    
    
    pretime = newtime                   # Set the previous time
    
    # Creating the Exit Pole
    cv2.imshow('Output',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()                       # Releasing the instance
cv2.destroyAllWindows()                 # Destroing the windows