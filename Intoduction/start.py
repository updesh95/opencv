import cv2

img = cv2.imread('lena.jpg', 0)

print(img)# if the file is not found the img will be None,else it will show an array
cv2.imshow('image', img)
k = cv2.waitKey(delay=0)
if k==27: # escape key
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()