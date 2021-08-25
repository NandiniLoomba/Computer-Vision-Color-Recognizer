import numpy as np
import pandas as pd
import cv2


#csv file contains color details like color names, their hex value, rgb values
columns=["color","colorName","hex","R","G","B"]
df=pd.read_csv("Project1\Resources\ColorDetails.csv",names=columns)
img=cv2.imread("Project1\Resources\Colors.jpeg")

clicked=False
r=g=b=xpos=ypos=0

#if we provide rgb values to this function then this function finds the nearest possible color
#in the csv file
def ColorRecognizer(R,G,B):
    minimum=100000
    
    for i in range(len(df)):
        p=abs(df.loc[i,'R']-R) + abs(df.loc[i,'G']-G) + abs(df.loc[i,'B']-B)
        if p<minimum:
            minimum=p
            name=df.loc[i,'colorName']

    return name    
    

#if we double click our mouse on the image then this function stores the x and y coordinates,
# and rgb values at the point so that we can find the exact color name and display the same
def decide_color(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked=True
        xpos,ypos=x,y
        # y=width and x=height
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

        
#Mouse Callback Function
#A callback function is the function which will get executed whenever the event happens, 
# so basically the callback function have a same syntax definition wherever it is used but 
# can differ in what it does as it totally depends on what instruction are written in it. 
# So in Mouse Callback Function we are declaring a Callback function having five parameters. 
# The first parameter event holds the value of the type of event such as left button click, 
# right button click, etc. The second and thrid parameter x, y are the coordinates of the pointer.

cv2.namedWindow("Picture")
cv2.setMouseCallback("Picture",decide_color)    


while (1):
    cv2.imshow("Picture",img)
    cv2.rectangle(img,(10,20),(750,60),(b,g,r),-1) #-1 fills the rectange
    text=ColorRecognizer(r,g,b)+ "  R = " + str(r) + "  G = "+ str(g) + "  B = "+ str(b)
    cv2.putText(img,text,(25,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

    if((r+g+b)>700):
        cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA) 
    clicked=False   
    if cv2.waitKey(1) & 0xFF==ord('n'):
        break  


    