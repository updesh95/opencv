# MT are some simple operation based on image shape
# Morphological transformation are normally performed on binary images
# A kernel is used which tells how to change the value of any given pixel
# by combining it with different amounts of the neighboring pixels

import cv2
import numpy as np
from matplotlib import pyplot as plt
img =  cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(mask, kernel)
titles = ['image', 'mask', "kernel"]
images = [img, mask, kernel]
#opening ===> erosion first then dilation
#closign ===> Closing then dilation
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()