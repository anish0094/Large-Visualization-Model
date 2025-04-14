import serial
from time import sleep
from python.utils.config import BASE_DIR

class ArduinoHandler:
    def __init__(self, port='COM3', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        
    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to Arduino on {self.port}")
            return True
        except serial.SerialException as e:
            print(f"Connection failed: {e}")
            return False

    def send_trigger(self):
        try:
            self.connection.write(b"REQUEST_TRIGGER\n")
            return self.connection.readline().decode().strip()
        except Exception as e:
            print(f"Trigger error: {e}")
            self.connect()  # Reconnect
            return None