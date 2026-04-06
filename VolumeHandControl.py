import cv2
import numpy as np
import time
import HandTrackingModule as htm


#################################################
wCam, hCam = 640, 480
 #################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDectector(detectionCon=0.7)



while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cv2.circle(img, (x1,y1), 25, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 20, (255,0,255), cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 60), cv2.FONT_HERSHEY_COMPLEX, 0.9, (60,255,60), 2)

    cv2.imshow('img',img)
    cv2.waitKey(1)