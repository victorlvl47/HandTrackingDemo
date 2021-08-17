import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0

# use webcam
cap = cv2.VideoCapture(0)

# open a video file
# cap = cv2.VideoCapture('> PATH TO VIDEO HERE <') 

detector = htm.handDetector()

while True:
    success, img = cap.read()

    img = detector.findHands(img)

    # For resizing
    # down_width = 896
    # down_height = 672
    # down_points = (down_width, down_height)

    lmList = detector.findPosition(img)
    if len(lmList) !=0:
        print(lmList[4])
  
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
   
    cv2.putText(img, str(int(fps)), (10, 70), 
            cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    # resized image
    # resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
                                
