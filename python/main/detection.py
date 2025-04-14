from ultralytics import YOLO
import cv2
from ..utils.config import YOLO_MODEL, DETECTIONS_DIR, DETECTION_IMAGES_DIR, DETECTION_LOGS_DIR
from datetime import datetime
import json
import os

class ObjectDetector:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL)
        self.last_results = None  # Track last detection results
        
    def track_objects(self, frame):
        self.last_results = self.model.track(frame, persist=True)  # Store results
        return self.last_results[0].plot() if self.last_results else frame

    def save_detection(self, frame, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save image
        img_path = os.path.join(DETECTION_IMAGES_DIR, f"{timestamp}.jpg")
        cv2.imwrite(img_path, frame)
        
        # Save metadata
        metadata = {
            "timestamp": timestamp,
            "image_path": img_path,
            "objects": [],
            "stats": {
                "total_objects": len(results[0].boxes),
                "inference_time": results[0].speed["inference"]
            }
        }
        
        for box in results[0].boxes:
            metadata["objects"].append({
                "type": self.model.names[int(box.cls)],
                "confidence": float(box.conf),
                "bbox": box.xyxy.tolist()[0] if box.xyxy.numel() > 0 else None,
                "track_id": int(box.id) if box.id else None
            })
        
        log_path = os.path.join(DETECTION_LOGS_DIR, f"{timestamp}.json")
        with open(log_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return img_path, log_path
    
