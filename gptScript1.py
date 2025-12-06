import mediapipe as mp
import cv2
import time
import numpy as np

mp_hands = mp.solutions.hands

# Store previous values for velocity + acceleration
prev_pos = None         # np.array([x,y,z])
prev_vel = None         # np.array([vx,vy,vz])
prev_t = None

def compute_derivatives(curr_pos, prev_pos, prev_vel, curr_t, prev_t):
    # Default zero values for first frame
    if prev_pos is None:
        return np.zeros(3), np.zeros(3)  # velocity, acceleration

    dt = curr_t - prev_t
    if dt <= 0:
        return np.zeros(3), np.zeros(3)

    # Velocity
    vel = (curr_pos - prev_pos) / dt

    # Acceleration
    if prev_vel is None:
        acc = np.zeros(3)
    else:
        acc = (vel - prev_vel) / dt

    return vel, acc

cap = cv2.VideoCapture(1)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    #global prev_pos, prev_vel, prev_t

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        # MediaPipe expects RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        curr_t = time.time()

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]

            # ---- GET INDEX FINGER TIP POSITION (normalized) ----
            tip = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            curr_pos = np.array([tip.x, tip.y, tip.z])

            # ---- COMPUTE VELOCITY & ACCELERATION ----
            vel, acc = compute_derivatives(curr_pos, prev_pos, prev_vel, curr_t, prev_t)

            # ---- PRINT OR USE VALUES ----
            print(f"Position: {curr_pos}")
            print(f"Velocity: {vel}")
            print(f"Acceleration: {acc}")
            print("------")

            # Update histories
            prev_pos = curr_pos
            prev_vel = vel
            prev_t = curr_t

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

