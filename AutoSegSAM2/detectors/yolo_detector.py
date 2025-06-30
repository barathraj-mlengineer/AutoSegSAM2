from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Replace with your custom model if needed

def detect_faces_hands(image):
    results = model(image)
    boxes = []
    for box in results[0].boxes:
        label = results[0].names[int(box.cls)]
        if label in ['person', 'face', 'hand']:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            boxes.append((x1, y1, x2, y2))
    return boxes
