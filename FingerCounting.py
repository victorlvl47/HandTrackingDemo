import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

# get images
folderPath = "FingerImages"
myList = os.listdir(folderPath)
myList = sorted(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        
        # index to pinky finger
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        # print(totalFingers)

        # display hand image
        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]

        #92629e
        # rgb(146, 98, 158)
        cv2.rectangle(img, (20, 225), (200, 300), (158, 98, 146), 
            cv2.FILLED)
        #e1e1de
        # rgb(225, 225, 222)
        cv2.putText(img, 'fingers: ' + str(totalFingers), 
            (20, 275), cv2.FONT_HERSHEY_PLAIN, 2, 
            (222, 225, 225), 2)

    # fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (450, 50), 
        cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
