import unittest
from python.main.nlp_handler import NLPProcessor
from python.main.detection import ObjectDetector
from python.main.serial_handler import ArduinoHandler

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.nlp = NLPProcessor()
        self.detector = ObjectDetector()
        self.arduino = ArduinoHandler()

    def test_queries(self):
        mock_results = [...]  # Create mock detection results
        self.assertEqual(
            self.nlp.process_query("count persons", mock_results),
            "2 person(s) detected"
        )
        
    def test_serial_reconnect(self):
        self.assertTrue(self.arduino.connect())
        
if __name__ == "__main__":
    unittest.main()