import cv2
import numpy as np
import face_recognition
import os

###  Functions
def imageLoader(path='training_images/'):
    '''
    this function load the train images from the given path.
    here every images is a class and at the time of comparing
    current image is coparied with the every train images.
    the class name will the name of the Image here
    '''
    encodeList = []
    classNames = []
    for imgName in os.listdir(path):
        img = cv2.imread(path+imgName)                      # Loading The Image
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)           # Converting into RGB Scale
        encode = face_recognition.face_encodings(img)[0]    # encoding the main face from the Image
        classNames.append(imgName.split('.')[0])
        encodeList.append(encode)
    return classNames, encodeList

### Programe Starts
classNames, trainEncodeList = imageLoader()      # Loading and Encoding All Train Images
print('Loading of Training Images Complete ....')
print('Number of Faces found = ',len(classNames))
print('Names = ',classNames)

cam = cv2.VideoCapture(0)                   # Creating WebCam Instance

# * State Rolling
while True:
    isTrue, frame = cam.read()                          # reading the frames

    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)    # creating a RBG Scale copy
    
    # * Getting the location of the Faces from the frame
    currentFaceLocs = face_recognition.face_locations(frameRGB)
    # * Encoding the Faces
    currentEncodeFaces = face_recognition.face_encodings(frameRGB,currentFaceLocs)
    
    # * Looping throw the all Faces in the frame for match
    for currentFaceLoc, currentEncodeFace in zip(currentFaceLocs,currentEncodeFaces):
        
        # Creating a bounding box of the face
        y, w, h, x = currentFaceLoc
        cv2.rectangle(frame,(x,y),(w,h),(0,255,0),2)

        # Comparing the Image
        match = face_recognition.compare_faces(trainEncodeList,currentEncodeFace)
        faceDis = face_recognition.face_distance(trainEncodeList,currentEncodeFace)
        
        # Finding the minimun distance position
        pos = np.argmin(faceDis)
        # Condition if true then print the class name or print 'Not Match'
        if match[pos]:
            cv2.putText(frame,str(classNames[pos]),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,200,0),2)
        else:
            cv2.putText(frame,'Not Match',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,.5,(50,0,250),2)
    
    # * Display
    cv2.imshow('Output',frame)
    
    # * Exit Pole: Press 'ESC' for exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()               # Release the WebCam
cv2.destroyAllWindows()     # Destroy all Windows