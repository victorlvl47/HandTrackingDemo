import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "paintMenuImages"
myList = os.listdir(folderPath)
myList.sort()
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)

detector = htm.handDetector(detectionCon=0.85)

while True:
    success, img = cap.read()
    # flip the video, for more intuitive drawing
    img = cv2.flip(img, 1)

    # find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # check which fingers are up
        fingers = detector.fingersUp()
        print(fingers)

    # overlay the color selection
    img[0:122, 0:800] = header

    cv2.imshow("Image", img)
    cv2.waitKey(1)
