import cv2
import numpy as np

photo = np.zeros((800, 800, 4), dtype='uint8')



cv2.circle(photo, (photo.shape[1] // 2, photo.shape[1] // 2), 350, (255, 255, 255), thickness=10)

cv2.ellipse(photo, center=(photo.shape[1] // 2, 400), axes=(200, 200), angle=0, startAngle=0, endAngle=180,
            color=(100, 255, 100), thickness=10)
cv2.ellipse(photo, center=(photo.shape[1] // 2, 400), axes=(150, 150), angle=0, startAngle=0, endAngle=180,
            color=(100, 255, 100), thickness=10)

cv2.line(photo, (550, photo.shape[0] // 4), (600, photo.shape[0] // 4), color=(0, 0, 255), thickness=10)
cv2.line(photo, (200, photo.shape[0] // 4), (250, photo.shape[0] // 4), color=(0, 0, 255), thickness=10)

cv2.line(photo, (250, photo.shape[0] // 4), (250, photo.shape[0] // 2), color=(255, 0, 0), thickness=10)
cv2.line(photo, (200, photo.shape[0] // 4), (200, photo.shape[0] // 2), color=(255, 0, 0), thickness=10)

cv2.line(photo, (600, photo.shape[0] // 4), (600, photo.shape[0] // 2), color=(255, 0, 0), thickness=10)
cv2.line(photo, (550, photo.shape[0] // 4), (550, photo.shape[0] // 2), color=(255, 0, 0), thickness=10)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
