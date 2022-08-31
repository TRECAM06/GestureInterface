import cv2
import pickle
import time
import numpy as np

wCam, hCam = 1280, 720


cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0

while True:
    success, img = cap.read()

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img, f"FPS: {int(fps)}", (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)