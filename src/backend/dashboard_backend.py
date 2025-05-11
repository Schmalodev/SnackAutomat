import serial
import time

class DashboardBackend(): 

    arduino = None

    def __init__(self):
        try:
            self.arduino = serial.Serial("COM3", 9600)
            time.sleep(4)
            print("Connect")
        except Exception as e:
            print(e)            

    def rotation(self) -> None:
        if self.arduino:
            stand = "turn"
            self.arduino.write(stand.encode("utf-8"))
        else:
            print("Keine Verbindung")
