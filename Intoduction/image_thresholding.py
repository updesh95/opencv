#Thresholding is a very popular segmentation technique
# Separating an object from its background
# Comparing each pixel of an image with a threshold value

import cv2
import numpy as np

img= cv2.imread("lena.jpg",0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2  = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
cv2.imshow("image", img)
cv2.imshow("threshod", th1)
cv2.imshow("threshod2", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()