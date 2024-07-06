import cv2
import mediapipe as mp
import pyfirmata2
import time
import math

board = pyfirmata2.Arduino("COM3")

ledPin = board.get_pin("d:6:p")

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands = 1)

while True:
    ledPin.write(0.5)
    success, frame = capture.read()

    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(frame)

        if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    
                handLandmarks = result.multi_hand_landmarks[0]
                thumbTip = handLandmarks.landmark[4]
                indexTip = handLandmarks.landmark[8]

                distance = math.sqrt((thumbTip.x - indexTip.x)**2 + (thumbTip.y - indexTip.y)**2)
                
                ledPin.write(distance)

        cv2.imshow("capture image", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()