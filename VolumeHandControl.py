import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # for middle circle
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Colors
        # B, G, R
        # rgb(35, 105, 177)
        # #C1AA77
        # rgb(193, 170, 119)

        cv2.circle(img, (x1, y1), 15, (119, 170, 193), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (119, 170, 193), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), 
            (199, 170, 193), 3)
        # middle circle
        cv2.circle(img, (cx, cy), 15, (119, 170, 193), cv2.FILLED)

        # length between index and thumb
        length = math.hypot(x2 - x1, y2 - y1)
        print(length)

        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), 
                cv2.FILLED)

    # Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), 
        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
