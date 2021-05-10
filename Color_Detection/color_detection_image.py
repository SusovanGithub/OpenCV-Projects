import cv2
import pandas as pd
import sys

# * Read the .csv file which have name of the colors
colorName_df = pd.read_csv('color_name.csv')

# !Global Variables
isClick = False
color = (0,0,0)

# * Helping functions
def getColorName(r,g,b):
    '''
    this function find the color name from the color_name.csv file using the R,G,B values
    '''
    minimum = 10000
    for i in range(len(colorName_df)):
        d = abs(r- int(colorName_df.loc[i,"R"])) + abs(g- int(colorName_df.loc[i,"G"]))+ abs(b- int(colorName_df.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            color_name = colorName_df.loc[i,"Name"]
    return color_name

def onclick(event,x,y,flag,params):
    """
    this function find the coordinate and rgb value and the name of the color
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b,g,r = img[y,x]
        global color,isClick,color_name
        isClick = True
        color = (int(b),int(g),int(r))

# * Loading the Image from the given path
path = input('Enter the Path os the Image = ')
img = cv2.imread(path)

# * Creating a Window
windowName = 'Color Detection'    
cv2.namedWindow(windowName)

# * Binding a event
cv2.setMouseCallback(windowName,onclick)

while True:
    temp = img.copy()       # creating a copy of the image
    
    # * Display the color name on the Image
    if isClick == True:
        cv2.rectangle(temp,(30,20),(550,50),color,-1)   # creating a rectangle of the same color
        b,g,r = color
        color_name = getColorName(r,g,b)                # Finding the name of the color
        # print the color name into the Image
        text = f'{color_name} R:{r} G:{g} B:{b}'        
        cv2.putText(temp, text, (40,45), cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    # * Display
    cv2.imshow(windowName,temp)
    
    # * Creating the Exit Pole
    if cv2.waitKey(1) & 0xFF == 27:     # 27 is the ascii of thr Esc button
        break

cv2.destroyAllWindows()     # Destroing the windows