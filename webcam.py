import cv2
import time

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)           
address = 'http://192.168.0.101:8080/video'
cam.open(address)

# * Start the Video
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
        
    # Mirror the frame output
    frame = cv2.flip(frame,1)

    # Converting into gray space
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # * Adding the FPS in Video
    fps = int(1/(time.time()-timer))        # Calculating the FPS
    cv2.putText(frame,                      # Adding the FPS to the frame
                text=str(fps) + 'fps',
                org=(10,30),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=1,
                color=(255,0,0),
                thickness=2)
    
    # *  Display the Frame
    cv2.imshow('Output',frame)
    
    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()             # Destroing the windows