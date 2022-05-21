import streamlit as st
from threading import Thread
import numpy as np
from tests import handTrackingModule as htM
import cv2
from scipy.spatial import distance as dist
import time
import math
import body_controller as bc

def handTracking():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = htM.handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            thumbPinkyDist = dist.euclidean([lmlist[4][1], lmlist[4][2]], [lmlist[17][1],lmlist[17][2]])
            thumbPinkyRobot = np.interp(thumbPinkyDist, [250, 600], [0, 180])
            indexWristDist = dist.euclidean([lmlist[8][1], lmlist[8][2]], [lmlist[0][1],lmlist[0][2]])
            indexWristRobot = np.interp(indexWristDist, [250, 600], [0, 180])
            middleWristDist = dist.euclidean([lmlist[12][1], lmlist[12][2]], [lmlist[0][1],lmlist[0][2]])
            middleWristRobot = np.interp(middleWristDist, [250, 600], [0, 180])
            ringWristDist = dist.euclidean([lmlist[16][1], lmlist[16][2]], [lmlist[0][1],lmlist[0][2]])
            ringWristRobot = np.interp(ringWristDist, [250, 600], [0, 180])
            pinkyWristDist = dist.euclidean([lmlist[20][1], lmlist[20][2]], [lmlist[0][1],lmlist[0][2]])
            pinkyWristRobot = np.interp(pinkyWristDist, [250, 600], [0, 180])
            
            lthumb = int(thumbPinkyRobot)
            lindex = int(indexWristRobot)
            lmiddle = int(middleWristRobot)
            lring = int(ringWristRobot)
            lpinky = int(pinkyWristRobot)
            
            bc.lM.move_finger(1, lthumb)
            bc.lM.move_finger(2, lindex)
            bc.lM.move_finger(3, lmiddle)
            bc.lM.move_finger(4, lring)
            bc.lM.move_finger(5, lpinky)
            
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
handTracking()