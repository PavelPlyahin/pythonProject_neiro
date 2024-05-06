
import cv2
import numpy as np

img = cv2.imread('Images/color_text.jpg')

new_image = np.zeros(img.shape, dtype='uint8')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (0, 0, 0), (255, 255, 255))
img = cv2.bitwise_not(img, img, mask)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 40, 0)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_image, con, -1, (0, 0, 255), 1)

ht, wt, chanel = new_image.shape
color_red = [0, 0, 255]
color_green = [0, 255, 0]
color_violet = [226, 43, 138]

for x in range(0, wt):
    for y in range(0, 166):
        yx = new_image[y, x]
        if not all(yx == color_red):
            continue
        new_image[y, x] = color_green

    for y in range(305, ht):
        yx = new_image[y, x]
        if all(color_red == yx):
            new_image[y, x] = color_violet

cv2.imwrite('pics/result.jpg', new_image)
cv2.imshow('result', new_image)
cv2.waitKey(0)
