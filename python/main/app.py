import cv2
from python.main.serial_handler import ArduinoHandler
from python.main.detection import ObjectDetector
from python.main.nlp_handler import NLPProcessor
from python.utils.config import DETECTIONS_DIR

def main():
    # Initialize components
    arduino = ArduinoHandler()
    detector = ObjectDetector()
    nlp = NLPProcessor()
    
    if not arduino.connect():
        return

    cap = cv2.VideoCapture(0)
    print("System ready. Commands: [t]rigger, [q]uit")

    while True:
        key = input("> ").strip().lower()
        
        if key == 't':
            # Get trigger from Arduino
            if arduino.send_trigger() == "TRIGGER_AI":
                ret, frame = cap.read()
                if ret:
                    # Detect and track
                    annotated = detector.track_objects(frame)
                    detector.save_detection(annotated, detector.last_results)
                    cv2.imshow("Detection", annotated)
                    
                    # Switch to terminal for query input
                    print("\nDetection complete. You can now ask queries:")
                    print("Examples: 'count persons', 'list objects', etc.")
                    print("Press [Enter] with empty input to return to detection mode")
                    
                    while True:
                        query = input("Query > ").strip()
                        if not query:  # Empty input returns to detection mode
                            break
                        print(nlp.process_query(query, detector.last_results))
        
        elif key == 'q':
            break

        # Refresh display
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
