class NLPProcessor:
    @staticmethod
    def process_query(query, results):
        query = query.lower()
        if not results or not results[0].boxes:
            return "No objects detected"

        # Extract objects data
        objects = [
            {
                "type": results[0].names[int(box.cls)],
                "confidence": float(box.conf),
                "bbox": box.xyxy[0].tolist() if hasattr(box.xyxy, '__iter__') else None,
                "track_id": int(box.id) if box.id else None
            } for box in results[0].boxes
        ]

        # Query processing
        if "count" in query:
            if "person" in query:
                count = sum(1 for obj in objects if obj["type"] == "person")
                return f"{count} person(s) detected"
            elif "car" in query:
                count = sum(1 for obj in objects if obj["type"] == "car")
                return f"{count} car(s) detected"
            return f"Total objects: {len(objects)}"

        elif "find" in query:
            color, obj_type = query.replace("find", "").strip().split()
            filtered = [
                obj for obj in objects 
                if obj["type"] == obj_type 
                # Add color filtering logic here
            ]
            return f"Found {len(filtered)} {color} {obj_type}(s)"

        elif "where is" in query:
            obj_type = query.replace("where is", "").strip()
            locations = [
                f"{obj['type']} at {obj['bbox']}" 
                for obj in objects 
                if obj["type"] == obj_type
            ]
            return "\n".join(locations) if locations else "Not found"

        elif "list all" in query:
            return "\n".join(f"{obj['type']} (ID: {obj['track_id']})" for obj in objects)

        return "Try: count persons | find red cars | where is person | list all"
    


class VideoNLP:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def answer(self, query):
        query = query.lower()
        
        if "show" in query:
            if "moving" in query:
                return self._get_moving_objects()
            elif "parked" in query:
                return self._get_stationary_objects()
        
        elif "count" in query:
            return f"Total objects: {len(self.analyzer.frame_history)}"
        
        elif "where is" in query:
            obj_type = query.split("where is")[1].strip()
            return self._locate_object(obj_type)
        
        return "Try: 'count objects', 'show moving cars', 'where is person'"

    def _get_moving_objects(self):
        # Implement movement analysis using frame_history
        pass