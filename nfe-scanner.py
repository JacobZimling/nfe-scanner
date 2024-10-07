# ------------------------------------------------------------------------------
# Imports

import cv2
import pyzbar.pyzbar as pyzbar

# ------------------------------------------------------------------------------
# Setup

img = cv2.imread('channel.png')
cap = cv2.VideoCapture(0)

# ------------------------------------------------------------------------------
# Decode Image

# decodedObjects = pyzbar.decode(img)
# # print(decodedObjects)
#
# for obj in decodedObjects:
#     print("Data: ", obj.data)

# ------------------------------------------------------------------------------
# Video

while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
         print(obj.data.decode('utf-8'))

#        if len(obj) >= 1:
#            import webbrowser
#            webbrowser.open(obj.data.decode('utf-8'))
#            exit()

    key = cv2.waitKey(1)
    if key == 27:
        break