import cv2
from matplotlib.pyplot import pyplot as plt
img = cv2.imread("lena.jpg", -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BRG2RBG)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()