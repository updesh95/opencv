import datetime

import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1208)
cap.set(4,720)

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_PLAIN
        text = 'Width:'+str(cap.get(3)) + ' Height:' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (10,50),font, 1, (0,255,123),1,cv2.LINE_AA)
        cv2.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF==ord('e'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
