
# import cv2
# from cvzone.HandTrackingModule import HandDetector
# import numpy as np
# import math
# import time

# cap = cv2.VideoCapture(0)  # Corrected 'videoCapture' to 'VideoCapture'
# detector = HandDetector(maxHands=1)
# offset = 20
# imgSize = 300
# counter = 0

# folder = "C:/Users/manisha/OneDrive/Desktop/sign Language Detection/Data/I Love You"  # Corrected backslashes and escaped them
# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)
#     if hands:
#         hsnd = hands[0]
#         x, y, w, h = hands[0]['bbox']  # Corrected 'hands ['bbox']' to 'hands[0]['bbox']'
#         imgwhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # Corrected 'np.unit8' to 'np.uint8'

#         imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
#         imgCropShape = imgCrop.shape
#         aspectratio = h / w

#         if aspectratio > 1:
#             k = imgSize / h
#             wCal = math.ceil(k * w)
#             imgResize = cv2.resize(imgCrop, (wCal, imgSize))
#             imgResizeShape = imgResize.shape
#             wGap = math.ceil((imgSize - wCal) / 2)
#             imgwhite[:, wGap:wCal + wGap] = imgResize

#         else:
#             k = imgSize / w
#             hCal = math.ceil(k * h)
#             imgResize = cv2.resize(imgCrop, (imgSize, hCal))
#             imgResizeShape = imgResize.shape
#             hGap = math.ceil((imgSize - hCal) / 2)
#             imgwhite[hGap:hCal + hGap, :] = imgResize

#         cv2.imshow('ImageCrop', imgCrop)  # Corrected 'cv2.inshow' to 'cv2.imshow'
#         cv2.imshow('Imagewhite', imgwhite)  # Corrected 'cv2.inshow' to 'cv2.imshow'
#     cv2.imshow("Image", img)  # Corrected 'cv2.inshow' to 'cv2.imshow'
#     key = cv2.waitKey(1)
#     if key == ord('s'):
#         counter += 1
#         cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgwhite)
#         print(counter)
#     if key == ord('q'):  # Added a condition to exit when 'q' is pressed
#         break

# cap.release()  # Release the video capture
# cv2.destroyAllWindows()  # Close all OpenCV windows

import os
import cv2
import time
import uuid


index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1

print("Available camera indices:", arr)

IMAGE_PATH = 'CollectedImages'
labels = ['Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes']
number_imgs = 40

for label in labels:
    os.makedirs(os.path.join(IMAGE_PATH, label), exist_ok=True)  # Use exist_ok=True to avoid errors if directory exists
    cap = cv2.VideoCapture(0)  # Try changing 0 to a different index if you have multiple cameras
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    if not cap.isOpened():
        print("Cannot open webcam")  # Check if camera opened successfully
        exit()

    for imgnum in range(number_imgs):
        ret, frame = cap.read()

        if not ret:  # Check if a frame was successfully read
            print("Can't receive frame (stream end?). Exiting ...")
            break

        imgname = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()  # Close the display window