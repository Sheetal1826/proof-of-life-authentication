import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indexes (MediaPipe)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EAR_THRESHOLD = 0.20   # blink sensitivity
BLINK_COUNT_REQUIRED = 1  # require at least 1 blink

blink_counter = 0


def eye_aspect_ratio(eye_points, landmarks):
    p1 = np.array([landmarks[eye_points[0]].x, landmarks[eye_points[0]].y])
    p2 = np.array([landmarks[eye_points[1]].x, landmarks[eye_points[1]].y])
    p3 = np.array([landmarks[eye_points[2]].x, landmarks[eye_points[2]].y])
    p4 = np.array([landmarks[eye_points[3]].x, landmarks[eye_points[3]].y])
    p5 = np.array([landmarks[eye_points[4]].x, landmarks[eye_points[4]].y])
    p6 = np.array([landmarks[eye_points[5]].x, landmarks[eye_points[5]].y])

    vertical1 = np.linalg.norm(p2 - p6)
    vertical2 = np.linalg.norm(p3 - p5)
    horizontal = np.linalg.norm(p1 - p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear


def check_face(frame):
    global blink_counter

    with mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                left_ear = eye_aspect_ratio(LEFT_EYE, face_landmarks.landmark)
                right_ear = eye_aspect_ratio(
                    RIGHT_EYE, face_landmarks.landmark)

                avg_ear = (left_ear + right_ear) / 2.0

                if avg_ear < EAR_THRESHOLD:
                    blink_counter += 1

                if blink_counter >= BLINK_COUNT_REQUIRED:
                    blink_counter = 0
                    return True

        return False
