import mediapipe as mp
import cv2
import time
import numpy as np
from math import sqrt

# * Creating the Webcam Instance
cam = cv2.VideoCapture(0)           
address = 'http://192.168.0.101:8080/video'
cam.open(address)

isTrue, frame = cam.read()
# ! Important Varables
color = (255,0,0)
canvas = np.zeros_like(frame)
output = frame.copy()
shape = canvas.shape
xp = yp = ''
thickness = 5

# * Functions

mpHands = mp.solutions.hands
hands   = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

def get_landmarks(handLM,imgshape):
    lm_list = []
    for ids, lm in enumerate(handLM.landmark):
        h, w, _ = imgshape
        lm_list.append([int(w*lm.x),int(h*lm.y)])
    return lm_list

def check_selection(x,y):
    global color,thickness
    h, w, c = shape
    
    # Creating the Menu Options
    menu = np.ones((80,w,c),dtype=np.int8) * 255
    menu[20:60,50:100]  = (255,0,0)
    menu[20:60,150:200] = (0,255,0)
    menu[20:60,250:300] = (0,0,255)
    menu[20:60,350:400] = (255,0,255)
    menu[20:60,450:500] = (255,255,0)
    frame[:80,:] = menu[:,:]
    cv2.putText(frame,
                text='Eraser',
                org=(535,50),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=.7,
                color=(0,0,0),
                thickness=2)

    # Chceking which Menu item is selected 
    if x>=50 and x<=100 and y>=20 and y<=60:
        color = (255,0,0)
        thickness = 5
    elif x>=150 and x<=200 and y>=20 and y<=60:
        color = (0,255,0)
        thickness = 5 
    if x>=250 and x<=300 and y>=20 and y<=60:
        color = (0,0,255)
        thickness = 5
    elif x>=350 and x<=400 and y>=20 and y<=60:
        color = (255,0,255)
        thickness = 5
    elif x>=450 and x<=500 and y>=20 and y<=60:
        color = (255,255,0)
        thickness = 5
    elif x>=550 and x<=600 and y>=20 and y<=60:
        color = (0,0,0)
        thickness = 20


# * Start the Video
while True:
    timer = time.time()             # Getting the time
    isTrue, frame = cam.read()      # Reading the Frames
        
    # Mirror the frame output
    frame = cv2.flip(frame,1)

    # Converting into RBG space
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # Getting the Hand deatils
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        handLM = results.multi_hand_landmarks[0]
        
        # converting the hand landmarks in a python list    
        lm_list = get_landmarks(handLM,shape)

        # all 5 fingers tips
        x0, y0 = lm_list[4] 
        x1, y1 = lm_list[8]
        x2, y2 = lm_list[12]
        x3, y3 = lm_list[16]
        x4, y4 = lm_list[20]

        # * Checking of the Modes
        if lm_list[6][1] >= y1 and lm_list[10][1] >= y2 and lm_list[14][1] <= y3 and lm_list[18][1] <= y4:
            # * Selection Mode

            # index finger tip position updation
            xp = yp = ''

            # merging the canvas to the frame
            frame = cv2.bitwise_or(frame,canvas)

            # Creating the marker
            mid_x = (x1+x2)//2
            mid_y = (y1+y2)//2
            
            # checking which color is selectied
            check_selection(mid_x,mid_y)

            # display the marker
            cv2.circle(frame,(mid_x,mid_y),10,color,-1)

            # display the Mode Details
            cv2.putText(frame,
                        text="Selction Mode",
                        org=(10,470),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=.7,
                        color=(10,0,200),
                        thickness=2)
        
        elif lm_list[6][1] >= y1 and lm_list[10][1] <= y2 and lm_list[14][1] <= y3 and lm_list[18][1] <= y4:
            ix, iy = lm_list[5]
            dist = sqrt( pow((ix-x0),2) + pow((iy-y0),2) )
            if dist<=37.0:
                # * Draw Mode
                if xp != '' and yp != '':
                    # drawing into the canvas
                    cv2.line(canvas,(x1,y1),(xp,yp),color,thickness)
                
                # index finger tip position updation
                xp = x1
                yp = y1
                
                # merging the canvas to the frame
                output = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
                _, output = cv2.threshold(output,1,255,cv2.THRESH_BINARY_INV)
                output = cv2.cvtColor(output,cv2.COLOR_GRAY2BGR)

                frame = cv2.bitwise_and(frame,output)
                frame = cv2.bitwise_or(frame,canvas)

                # display the marker
                cv2.circle(frame,(x1,y1),10,color,2)

                # display the Mode Details
                cv2.putText(frame,
                            text="Draw Mode",
                            org=(10,470),
                            fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=.7,
                            color=(10,0,200),
                            thickness=2)
            else:
                # * Hover Mode

                # index finger tip position updation
                xp = yp = ''
                
                # merging the canvas to the frame
                frame = cv2.bitwise_or(frame,canvas)
                
                # display the marker
                cv2.circle(frame,(x1,y1),10,color,2)

                # display the Mode Details
                cv2.putText(frame,
                            text="Hover Mode",
                            org=(10,470),
                            fontFace=cv2.FONT_HERSHEY_DUPLEX,
                            fontScale=.7,
                            color=(10,0,200),
                            thickness=2)
        
        elif lm_list[6][1] >= y1 and lm_list[10][1] >= y2 and lm_list[14][1] >= y3 and lm_list[18][1] <= y4:
            # * Clear The Canvas
            canvas = np.zeros_like(frame)
            # display the Mode Details
            cv2.putText(frame,
                        text="Clear Mode",
                        org=(10,470),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=.7,
                        color=(10,0,200),
                        thickness=2)
        
        else:
            # * Undefined Gesture Mode
            
            # index finger tip position updation
            xp = yp = ''

            # merging the canvas to the frame
            frame = cv2.bitwise_or(frame,canvas)
            
            # display the Mode Details
            cv2.putText(frame,                    
                        text="Undefined Gesture",
                        org=(10,470),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=.7,
                        color=(10,0,200),
                        thickness=2)
        
        # * Draw the hand Land marks
        # mpDraw.draw_landmarks(frame,handLM,mpHands.HAND_CONNECTIONS)
    
    else:
        # If can't detect the Hand 
        # merging the canvas to the frame
        frame = cv2.bitwise_or(frame,canvas)

        # display the error massage
        cv2.putText(frame,                    
            text="Unable To Detect",
            org=(10,470),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=.7,
            color=(10,0,200),
            thickness=2)


    # * Adding the FPS in Video
    fps = int(1/(time.time()-timer))        # Calculating the FPS
    cv2.putText(frame,                      # Adding the FPS to the frame
                text=str(fps) + 'fps',
                org=(580,470),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=.6,
                color=(255,255,0),
                thickness=1)
    
    # *  Display the Frame
    cv2.imshow('Air Canvas', frame)

    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()                       # Releasing the instance
cv2.destroyAllWindows()             # Destroing the windows