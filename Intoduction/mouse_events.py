import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_ITALIC
        strxy = str(x)+', '+ str(y)
        cv2.putText(img,strxy, (x,y), font, 1, (234,200,22),1)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_ITALIC
        strbgr = str(blue) + ', '+str(green) + ', '+str(red)
        cv2.putText(img, strbgr, (x,y), font,1,(123,31,12),1)
        cv2.imshow("image", img)

#img = np.zeros((2512,512,3),np.uint8)
img= cv2.imread("lena.jpg")
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
