import cv2
import pandas as pd
import sys

# * Read the .csv file which have name of the colors
colorName_df = pd.read_csv('color_name.csv')

# !Global Variable Creation
isClick = False
color = (0,0,0)

# * Getting the name ofthe color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(colorName_df)):
        d = abs(R- int(colorName_df.loc[i,"R"])) + abs(G- int(colorName_df.loc[i,"G"]))+ abs(B- int(colorName_df.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            color_name = colorName_df.loc[i,"Name"]
    return color_name

# * Creating the color finding function
def onclick(event,x,y,flag,params):
    """
    this function find the coordinate and rgb value and the name of the color
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        b,g,r = img[y,x]
        global color,isClick,color_name
        isClick = True
        color = (int(b),int(g),int(r))
        
# * Creating a Window
windowName = 'Output'    
cv2.namedWindow(windowName)

# * Binding a event
cv2.setMouseCallback(windowName,onclick)

if __name__ == "__main__":
    path = sys.argv[1]
    img = cv2.imread(path)
    
    while True:
        # creating a copy
        temp = img.copy()

        # * Display the color name on the screen
        if isClick == True:
            cv2.rectangle(temp,(30,20),(550,50),color,-1)   # creating a rectangle of the same color
            b,g,r = color
            color_name = getColorName(r,g,b)                # Finding the name of the color
            # print the color name into the Frame 
            text = f'{color_name} R:{r} G:{g} B:{b}'        
            cv2.putText(temp, text, (40,45), cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

        # * Display
        cv2.imshow(windowName,temp)

        # * Creating the Exit Pole
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()     # Destroing the windows