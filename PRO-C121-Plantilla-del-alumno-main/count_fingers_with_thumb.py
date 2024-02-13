import cv2
import mediapipe as mp

cap = cv2.VideoCapture (0)
mp_hands = mp.solution.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
tipIds = [4,8,12,16,20]

#Define una función para contar los dedos
def countFingers(image, hand_landmarks, handNo=0):

    if hand_landmarks:
        #Obtén todos los puntos de referncia de la mano Primera mano Visible.
        landmarks = hand_landmarks[handNo].landmark
        #Cuenta los dedos
        fingers = []

        for lm_index in tipIds:
            #Obtén los valores y de la punta de los dedos y la parte inferior.
            fingers_tip_y = landmarks[lm_index].y
            fingers_bottom_y = landmarks[lm_index -2].y

            #Obtén los valores y de la punta del pulgar y la parte inferior.
            thumb_tip_x = landmarks[lm_index].x
            thumb_bottom_x = landmarks[lm_index -2].x

            #Verifica si algún un dedo esta abierto o cerrado.
            if lm_index !=4
                if fingers_tip_y < fingers_bottom_y:
                    fingers.append(1)
                    print("Dedo con id", lm_index, "está cerrado")

                    if fingers_tip_y > fingers_bottom_y:
                        fingers.append(0)
                        print("Dedo con id", lm_index, "esta cerrado")
                else:
                    if thumb_tip_x < thumb_bottom_x:
                        fingers.append(1)
                        print("PPULGAR está abierto")

                    if thumb_tip_x > thumb_bottom_x:
                        fingers.append(0)
                        print("PPULGAR está cerrado")


        #imprime (fingers)
        totalFingers = fingers.count(1)

        #Muestra el texto
        text = f'Fingers: {totalFingers}'

        cv2.putText(image, text, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)

#Define una función para
def drawHandLandMarks(image, hand_landmarks):