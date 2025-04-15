import cv2
import time
from ultralytics import YOLO
from collections import defaultdict

class VideoAnalyzer:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.frame_history = defaultdict(list)
        self.next_id = 1  # Counter for assigning IDs when tracking fails

    def process_stream(self, video_path=0):
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: 
                break
            
            results = self.model.track(frame, persist=True)
            self._update_history(results)
            yield frame, results

    def _update_history(self, results):
        timestamp = time.time()
        if results and results[0].boxes:
            for box in results[0].boxes:
                # Assign temporary ID if tracking fails
                obj_id = int(box.id) if box.id else self.next_id
                self.next_id += 1
                
                self.frame_history[obj_id].append({
                    "timestamp": timestamp,
                    "type": self.model.names[int(box.cls)],
                    "bbox": box.xyxy[0].tolist() if box.xyxy is not None else [],
                    "confidence": float(box.conf)
                })
            
            # Prune old entries (keep last 60s)
            self.frame_history = {
                k: [v for v in entries if timestamp - v["timestamp"] < 60]
                for k, entries in self.frame_history.items()
            }