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

while True:
    success, img = cap.read()

    # overlay the selection menu
    img[0:122, 0:800] = header

    cv2.imshow("Image", img)
    cv2.waitKey(1)
