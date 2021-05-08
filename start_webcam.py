import cv2
import time

cam = cv2.VideoCapture(0)           # Creating the Webcam Instance

# Setting the Resolution
cam.set(3,640)                      # Width
cam.set(4,480)                      # Height


while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
    
    # Adding the FPS in the Video
    fps = int(1/(time.time()-timer))        # Calculating the FPS
    cv2.putText(frame,                      # Adding the FPS to the frame
                text=str(fps) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    
    # Display the Frame
    cv2.imshow('Output',frame)
    
    # Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cam.release()                       # Releasing the instance
cv2.destroyAllWindows()             # Destroing the windows