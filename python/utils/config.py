import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(DATA_DIR, "models")

# Model files
YOLO_MODEL = os.path.join(MODELS_DIR, "yolov8n.pt")

# Detection outputs
DETECTIONS_DIR = os.path.join(DATA_DIR, "detections")
DETECTION_IMAGES_DIR = os.path.join(DETECTIONS_DIR, "images")  # Specific image directory
DETECTION_LOGS_DIR = os.path.join(DETECTIONS_DIR, "logs")
os.makedirs(DETECTION_LOGS_DIR, exist_ok=True)
os.makedirs(DETECTION_IMAGES_DIR, exist_ok=True)  # Creates both detections/ and images/

