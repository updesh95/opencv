import numpy as np
import cv2
img = cv2.imread("lena.jpg",1)
img2 = cv2.imread("lena_copy.png",1)
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
#loc = img[280:340,330:390]
#img[273:333,100:160] = loc
#final = cv2.add(img,img2);
final = cv2.addWeighted(img,.9,img2,.1,0)
cv2.imshow("image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()