import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255),-1)
img2  = cv2.imread("lena.jpg")
print(img2.shape)
bitadd = cv2.bitwise_and(img1,img2)
cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
cv2.imshow("bitadd", bitadd)
cv2.waitKey(0)
cv2.destroyAllWindows()