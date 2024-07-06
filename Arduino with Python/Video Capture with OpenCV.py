import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

while True:
    success, frame = capture.read()

    if success:
        cv2.imshow("capture image", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()