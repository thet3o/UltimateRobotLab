import cv2
import mediapipe as mp
import time
import math
import numpy as np
from scipy.spatial import distance as dist

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, min_detection_confidence= self.detectionCon, min_tracking_confidence= self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            if len(self.results.multi_handedness) == 2:
                cv2.putText(img, 'Both Hands', (250, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 0.9,
                            (0, 255, 0), 2)
            elif len(self.results.multi_handedness) == 1:
                cv2.putText(img, 'Left', (250, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 0.9,
                            (0, 255, 0), 2)
            elif len(self.results.multi_handedness) == 0:
                cv2.putText(img, 'Right', (250, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 0.9,
                            (0, 255, 0), 2)
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            dThumbIndex = math.hypot((lmlist[4][1]-lmlist[8][1]),(lmlist[4][2]-lmlist[8][2]))
            dThumbMiddle = math.sqrt((lmlist[4][1]-lmlist[12][1])**2 + (lmlist[4][2]-lmlist[12][2])**2)
            dThumbRing = math.sqrt((lmlist[4][1]-lmlist[16][1])**2 + (lmlist[4][2]-lmlist[16][2])**2)
            dThumbLittle = math.sqrt((lmlist[4][1]-lmlist[20][1])**2 + (lmlist[4][2]-lmlist[20][2])**2)
            rr = np.interp(dThumbIndex, [50, 400], [0, 255])
            cv2.line(img, (lmlist[4][1], lmlist[4][2]), (lmlist[8][1], lmlist[8][2]), (0, rr, 255), 2)
            cv2.circle(img, (700, 250), 20, (120, rr, 50), cv2.FILLED)
            if dThumbIndex < 70:
                cv2.putText(img, "Idle", (lmlist[4][1], lmlist[4][2]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            elif dThumbMiddle < 70:
                cv2.putText(img, "Close hand", (lmlist[4][1], lmlist[4][2]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            elif dThumbRing < 70:
                cv2.putText(img, "Speak", (lmlist[4][1], lmlist[4][2]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()