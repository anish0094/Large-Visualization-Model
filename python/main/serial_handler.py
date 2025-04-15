import serial
from time import sleep

class ArduinoHandler:
    def __init__(self, port='COM3', max_retries=3):
        self.port = port
        self.max_retries = max_retries
        self.connection = None

    def connect(self):
        for attempt in range(self.max_retries):
            try:
                self.connection = serial.Serial(self.port, 9600, timeout=1)
                print(f"Connected to Arduino (Attempt {attempt + 1})")
                return True
            except serial.SerialException as e:
                print(f"Connection failed: {e}")
                sleep(2 * (attempt + 1))  # Exponential backoff
        return False

    def send_trigger(self):
        try:
            if not self.connection or not self.connection.is_open:
                self.connect()
            self.connection.write(b"REQUEST_TRIGGER\n")
            return self.connection.readline().decode().strip()
        except Exception as e:
            print(f"Error: {e}")
            self.connect()
            return None