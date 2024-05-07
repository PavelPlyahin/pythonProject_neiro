# Техническое задание:
# Вся программа должна работать с видеопотоком (не с 1 картинкой).
# Для распознавания глаз используйте каскад Хаара, который находится в свободном доступе - GitHub OpenCV.
# Глаза должны быть размыты так, чтобы были видны только их очертания (рекомендуется разное размытие по осям x и y)
# Область глаз должна быть шире чем сами глаза (как в примере).
# Область глаз должна быть чёрно-белого формата (как в примере).
# Поставленную задачу можно решить как с применением масок, так и без них.

import cv2
import numpy as np

capture = cv2.VideoCapture('videos/veb_cam.mp4')
search_face = cv2.CascadeClassifier('XML_file/face.xml')
search_eyes = cv2.CascadeClassifier('XML_file/eyes.xml')

while True:
    success, img = capture.read()
    eye_frame = np.zeros(img.shape, np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = search_face.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=6)

    for (x, y, w, h) in faces:
        eyes = search_eyes.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
        if len(eyes) >= 1:
            ex1, ey1, ew1, eh1 = eyes[0]
            ex2, ey2, ew2, eh2 = eyes[1]

            if eyes[0][0] < eyes[1][0]:

                eyes = cv2.rectangle(img, (x, ey1), (x + w, ey1 + eh2), (128, 128, 128), thickness=3)
                cut_eye = eyes[ey1:ey1 + eh2, x:x + w]
                cut_eye = cv2.GaussianBlur(cut_eye, (99,89), 0)
                img[ey1:ey1 + eh2, x:x + w] = cut_eye

    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyWindow()