import cv2
import numpy as np
import face_recognition
import os


def imageLoader(path='abc/'):
    encodeList = []
    for imgName in os.listdir(path):
        img = cv2.imread(path+imgName)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encode1 = []
img11 = cv2.imread('abc/a1.jpeg')
img11 = cv2.cvtColor(img11,cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(img11)[0]
encode1.append(encode)

img12 = cv2.imread('abc/a2.jpeg')
img12 = cv2.cvtColor(img12,cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(img12)[0]
encode1.append(encode)



encode2 = []
img21 = cv2.imread('abc/b1.jpeg')
img21 = cv2.cvtColor(img21,cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(img21)[0]
encode2.append(encode)

img22 = cv2.imread('abc/b2.jpeg')
img22 = cv2.cvtColor(img22,cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(img22)[0]
encode2.append(encode)

cam = cv2.VideoCapture(0)

while True:
    isTrue, frame = cam.read()

    frameC = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceLocs = face_recognition.face_locations(frameC)[0]
    encodeFaces = face_recognition.face_encodings(frameC,faceLocs)
    for faceLoc, encodeFace in zip(faceLocs,encodeFaces):
        match = face_recognition.compare_faces(encode1,encodeFace)
        y, h, w, x = faceLoc
        cv2.putText(frame,str(match),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,200),2)
    
    cv2.imshow('Output',frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cam.release()
cv2.destroyAllWindows()