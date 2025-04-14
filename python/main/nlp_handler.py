class NLPProcessor:
    @staticmethod
    def process_query(query, results):
        query = query.lower()
        if not results or not results[0].boxes:
            return "No objects detected"
            
        if "count" in query:
            if "person" in query:
                count = sum(box.cls == 0 for box in results[0].boxes)
                return f"{count} person(s) detected"
            elif "car" in query:
                count = sum(box.cls == 2 for box in results[0].boxes)
                return f"{count} car(s) detected"
            else:
                return f"{len(results[0].boxes)} objects detected"
                
        elif "list" in query:
            obj_types = [results[0].names[int(box.cls)] for box in results[0].boxes]
            return "Detected: " + ", ".join(set(obj_types))
            
        return "Try: 'count persons' or 'list objects'"