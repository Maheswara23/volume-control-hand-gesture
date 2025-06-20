import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

#########################
wCam, hCam = 640, 480
#########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cTime = 0
pTime = 0
detector = htm.HandDetector()

device = AudioUtilities.GetSpeakers()
interface = device.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volumeRange = volume.GetVolumeRange()
minVol = volumeRange[0]
maxVol = volumeRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        #print(length)

        # Hand Range 15 - 150
        # Volume Range -63.5 - 0
        vol = np.interp(length, [15, 150], [minVol, maxVol])
        volBar = np.interp(length, [15, 150], [400, 150])
        volPer = np.interp(length, [15, 150], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 15:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), ( 0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), ( 0, 255, 0), cv2.FILLED)
    cv2.putText(img, f"{int(volPer)} %", (40, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS:{int(fps)}", (40,50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)