import cv2

# img = cv2.imread('images/IMG_8531.jpg')
# cv2.imshow('Result', img)
# cv2.waitKey(0)


cap = cv2.VideoCapture('Videos/video_2022-11-03_09-03-32.mp4')
cap.set(3, 500)
cap.set(4, 300)
while True:
    sucsess, img = cap.read()
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break