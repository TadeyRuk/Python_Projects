import cv2
import mediapipe as mp
"""
cap - capture variable for webcam
ret - True or False to tell me if the webcam is working or not
cap.read() - reads the frame of the webcam
imshow - Shows the window of the cap (capture variable)
waitKey(1) - waits for key pressed every 1ms 
cap.release() - frees the webcam so other apps can use it
cv2.flip() - basically it just flips the webcam horizontally if 1 is the flip_value

"""

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands= 2,
    min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_flip = cv2.flip(frame, 1) # variable to store the flipped camera frame

    rgb_frame = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    #Starting from this, this is the image pipeline of mediapipe hand detection
    if results.multi_hand_landmarks: # Idk why it says unreferenced but I think it's the IDE's fault
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame_flip, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    #until here

    cv2.imshow("Webcam Test", frame_flip) # just shows the window (Can be named anything I want)

    #waits for the user to press the 'q' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'): # gets the ascii code of q, ascii codes are needed for the program to read the key
        break

cap.release() # to remove webcam capture window
cv2.destroyAllWindows() # remove all windows na active
