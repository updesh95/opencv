#HSV
#Hue coreesponds to the color components(base pigment) hence by selectinh
# a range of hue you can select any color.(0-360)
# Saturation is the amount of color (depth of the pigment)
#Value is basically the brightness of the color.

import cv2

import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0);
cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower Hue","Tracking", 0, 255,nothing)
cv2.createTrackbar("Lower Saturation","Tracking", 0, 255,nothing)
cv2.createTrackbar("Lower Value","Tracking", 0, 255,nothing)
cv2.createTrackbar("Upper Hue","Tracking", 255, 255,nothing)
cv2.createTrackbar("Upper Saturation","Tracking", 255, 255,nothing)
cv2.createTrackbar("Upper Value","Tracking", 255, 255,nothing)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("Lower Hue","Tracking")
    ls = cv2.getTrackbarPos("Lower Saturation", "Tracking")
    lv = cv2.getTrackbarPos("Lower Value", "Tracking")

    uh = cv2.getTrackbarPos("Upper Hue", "Tracking")
    us = cv2.getTrackbarPos("Upper Saturation", "Tracking")
    uv = cv2.getTrackbarPos("Upper Value", "Tracking")


    l_b = np.array([lh,ls,lv])# lower blue color
    u_b = np.array([uh, us, uv])# Upper blue color

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()