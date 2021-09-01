import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

brushThickness = 15
eraserThickness = 50

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
# yellow #ffde59
# rgb(255, 222, 89)
drawColor = (89, 222, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)

detector = htm.handDetector(detectionCon=0.85)

# previous x/y-coordinate
xp, yp = 0, 0

# canvas where we will be drawing
imgCanvas = np.zeros((600, 800, 3), np.uint8)

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
        # print(fingers)

        # two fingers are up, selection mode
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("selection mode")
            # color selection or eraser
            if y1 < 122:
                # select yellow
                if 0<x1<175:
                    header = overlayList[0]
                    drawColor = (89, 222, 255)
                # select red
                elif 200 < x1 < 310:
                    header = overlayList[1]
                    # rgb(255, 22, 22)
                    drawColor = (22, 22, 255)
                # select blue
                elif 350 < x1 < 550:
                    header = overlayList[2]
                    # rgb(0, 74, 173)
                    drawColor = (173, 74, 0)
                # select eraser
                elif 590 < x1 < 800:
                    header = overlayList[3]
                    # white
                    drawColor = (0, 0, 0)

            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
            print("selection mode")

        # index finger is up, drawing mode
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)

            # for the first frame
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            # for the eraser, we make the brush bigger
            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            # we just draw normally
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1
            print('drawing mode')

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)


    # overlay the color selection
    img[0:122, 0:800] = header

    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)
