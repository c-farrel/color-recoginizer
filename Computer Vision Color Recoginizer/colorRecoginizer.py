#import libraries
import numpy as np
import pandas as pd
import cv2

#define and read image
img = cv2.imread("Computer Vision Color Recoginizer\colors.jpg")

#teach program to recoginize colors
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('Computer Vision Color Recoginizer\colors.csv', names=index, header=None)

#define global variables
clicked = False #hold if image is clicked
r = g = b = xpos = ypos = 0 #iniatialize x and y positions, and rgb vlues to zero

#function to recoginize colors
#called when section of image double clicked
#returns color name and rgb values
def recoginize_color(R, G, B):
    minimun = 1000
    for i in range(len(csv)): #loop through color names file
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"])) #total RGB vaules
        if (d<=minimun):
            minimun = d
            cname = csv.loc[i, "color_name"] #get color name from colors list
    return cname

#function for what happens when double clicked
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #check if second mouse click
        global b, g, r, xpos, ypos, clicked #declare global variables in function
        clicked = True #image has been clicked

        #get x, y coordinates of where image clicked
        xpos = x
        ypos = y

        #get rgb values from image coordinates
        b,g,r = img [y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#create application window
#image window will be image file opened as a new windo

    #open image as window
cv2.namedWindow('Color Recoginiton App')

    #call mouse click function, adds funcionality to application
cv2.setMouseCallback('Color Recoginiton App', mouse_click)

#create application
#application will return name and rgb values of section of image when double clicked

    #while loop to run application
while(1): #infinite loop
    cv2.imshow('Color Recoginiton App', img)
    if (clicked):

        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills entire rectangle
        #create a box of selected color to display color name and rgb values
        cv2.rectangle(img, (20,20), (750,60), (b,g,r), -1)

        #create string to displal name and rgb values of color
            #=color name R=(rval) G=(gval) B=(bval)
        text = recoginize_color(r,g,b) + ' R =' + str(r) + ' G =' + str(g) + ' B =' + str(b)

        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        #add string created above to box created above in white text
        cv2.putText(img, text, (50, 50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)

        #if color is bright, display text in back of it can be read
        if (r+g+b >= 600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        #set clicked to false
        #while aplication is running, if image double clicked again, if atatement will repeal
        clicked = False

    #break loop to exit application
    #user can exit applicaiton by pressing 'esc'
    #cv2.waitKey(20) = wait 20 milliseconds
    #cv2.waitKey(20)&0xFF - get int less than 225 that corresponds to ascii value for key
    #27 is ascii decimal value for esc key
    if cv2.waitKey(20) & 0xFF==27:
        break

#close window
cv2.destroyAllWindows()
