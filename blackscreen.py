import cv2 
import numpy 
import time

fourcc =  cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi' , fourcc  , 20.0 , (640,480))

cam = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60) : 
    ret,bg = cam.read()

bg = np.flip(bg,axis = 1)

while(cam.isOpened())  : 
    ret,img = cam.read()

    if not ret : 
        break 
    
    img = np.flip(img,axis  = 1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR)

    lower_black = np.array([104,153,70])
    upper_black = np.array([30,30,0])
    mask = cv2.inRange(hsv , lower_black , upper_black)

    mask = cv2.morphologyEx(mask , cv2MORPH_OPEN , np.once((3,3),np.uint8))
    mask = cv2.morphologyEx(mask , cv2_MORPH_DILATE , np.once((3,3),np.uint8))

    res = cv2.bitwice_and(bg,bg,mask = mask)

    f = bg - res 
    f = np.where(f == 0 , image  , f)

    output = cv2.addWeighted(res , 1 , res , 1 , 0)
    output_file.write(output)

    cv2.iamshow('World is colorful' , output)
    cv2.waitkey(1)

cam.release()
out.release()
cv2.destroyAllwindows()
