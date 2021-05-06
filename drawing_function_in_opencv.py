import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros((500,500,3),np.uint8)
img = cv2.line(img,(0,0),(255,255), (0,0,255),23)
img = cv2.arrowedLine(img,(0,100),(340,340),(0,255,0),23)

img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
img = cv2.circle(img,(447,63),63,(0,255,255),-1)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'OpenCv',(10,500),font,4,(0,123,233),10,cv2.LINE_AA)
cv2.imshow("image",img)


if cv2.waitKey(0) == ord('e'):
    cv2.destroyAllWindows()