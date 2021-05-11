import cv2
import numpy as np

# ! Global Variables
pts1 = np.zeros((4,2))
counter = 0
windowName = 'Main Image'
output_width, output_height = 300, 400

# * Function creation for getting the points where mouse clicked
def onClick(event,x,y,flag,img):
    global circle,counter                               # ! Accessing the Global Variables
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pts1[counter] = x,y
        counter = counter + 1
        cv2.circle(img,(x,y),4,(0,0,255),-1)
        cv2.putText(img,str(counter),(x-5,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,.5,(0,0,255))

# * Main Function
def main():
    global pts1, counter, output_width, output_height   # ! Accessing the Global Variables
    
    # * Getting the Image Location
    path = input('Enter the Image location = ')
    img = cv2.imread(path)
    imgC = img.copy()
    
    # * Creating the Window
    cv2.namedWindow(windowName)

    # * Binding the Event
    cv2.setMouseCallback(windowName,onClick,img)

    while True:
        # * Condition that click corners are clicked or not
        if counter == 4:
            pts1 = np.float32(pts1)
            pts2 = np.float32([[0,0],[output_width,0],[0,output_height],[output_width,output_height]])
            matix = cv2.getPerspectiveTransform(pts1,pts2)
            imgOut = cv2.warpPerspective(imgC,matix,(output_width,output_height))
            cv2.imshow('Result',imgOut)         # Display the resultent Output

        # * Display the Image
        cv2.imshow(windowName,img)

        # * Exit Pole: press 'ESC' to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()