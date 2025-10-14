import cv2
import mediapipe as mp
import numpy as np
import math
import json
import os

# --- CONFIG ---
SAVE_PATH = "registered_postures.json"
TOLERANCE = 0.50  # 10% tolerance

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# --- LOAD POSTURES ---
if os.path.exists(SAVE_PATH):
    with open(SAVE_PATH, "r") as f:
        registered_postures = json.load(f)
    print(f"📂 Loaded {len(registered_postures)} postures from {SAVE_PATH}")
else:
    registered_postures = {}
    print("⚠️ No saved postures found! Press 's' to register some first.")

def vector_angle(a, b):
    dot = np.dot(a, b)
    norm = np.linalg.norm(a) * np.linalg.norm(b)
    if norm == 0:
        return 0.0
    return math.acos(np.clip(dot / norm, -1.0, 1.0))

def get_finger_angles(hand_landmarks):
    """Return list of angles (radians) for each fingertip relative to wrist vector."""
    lm = hand_landmarks.landmark
    wrist = np.array([lm[0].x, lm[0].y, lm[0].z])
    finger_tips = [4, 8, 12, 16, 20]  # thumb → pinky
    ref_vec = np.array([lm[9].x, lm[9].y, lm[9].z]) - wrist
    angles = []
    for tip in finger_tips:
        tip_vec = np.array([lm[tip].x, lm[tip].y, lm[tip].z]) - wrist
        angles.append(vector_angle(ref_vec, tip_vec))
    return np.array(angles)

def compare_postures(current_angles):
    """Return (best_match_name, distance) or (None, None) if no match."""
    matches = []
    for name, ref_angles in registered_postures.items():
        ref = np.array(ref_angles)
        # Avoid division by zero by adding small epsilon
        diff_ratio = np.abs((current_angles - ref) / (ref + 1e-6))
        if np.all(diff_ratio < TOLERANCE):
            dist = np.linalg.norm(current_angles - ref)
            matches.append((name, dist))
    if matches:
        best = min(matches, key=lambda x: x[1])
        return best[0], best[1]
    return None, None

cap = cv2.VideoCapture(0)
print("👉 Press 's' to register a posture (saved to JSON).")
print("👉 Recognition runs automatically.")
print("👉 Press 'ESC' to exit.\n")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    detected_label = None

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            if handedness.classification[0].label == 'Right':
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                angles = get_finger_angles(hand_landmarks)

                # Compare to known postures
                if registered_postures:
                    label, dist = compare_postures(angles)
                    if label:
                        detected_label = label
                        cv2.putText(frame, f"{label} ({dist:.3f})",
                                    (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 255, 0), 3)

                # Register new posture if requested
                key = cv2.waitKey(1) & 0xFF
                if key == ord('s'):
                    print("\nDetected angles (radians):", np.round(angles, 3))
                    name = input("Enter name for this posture: ")
                    registered_postures[name] = angles.tolist()
                    with open(SAVE_PATH, "w") as f:
                        json.dump(registered_postures, f, indent=4)
                    print(f"✅ Registered posture '{name}' and saved.")
                    print("Current postures:", list(registered_postures.keys()))

    # Display window
    cv2.imshow("Right Hand Posture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
