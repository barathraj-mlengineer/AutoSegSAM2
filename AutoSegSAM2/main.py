import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

# Initialize Mediapipe modules
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def run_pipeline(image_pil):
    # Convert PIL image to OpenCV format
    image = np.array(image_pil.convert('RGB'))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Create a copy to draw on
    annotated_image = image.copy()

    # Face Detection
    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(annotated_image, detection)

    # Hand Detection
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Convert back to PIL Image and return
    output_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(output_image)
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

# Initialize Mediapipe modules
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def run_pipeline(image_pil):
    # Convert PIL image to OpenCV format
    image = np.array(image_pil.convert('RGB'))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Create a copy to draw on
    annotated_image = image.copy()

    # Face Detection
    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(annotated_image, detection)

    # Hand Detection
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Convert back to PIL Image and return
    output_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(output_image)
