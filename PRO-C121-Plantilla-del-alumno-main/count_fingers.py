import cv2

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

