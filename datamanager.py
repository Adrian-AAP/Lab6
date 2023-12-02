import time
import random
from eventmanager import EventManager

class RealTimeDataManager:
    def __init__(self):
        self.data_antigua = {"temperatura": 25.0, "humedad": 60.0}
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(1)
            self.generate_real_time_data()

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

    def notificar_cambio(self, event, data):
        self.event_manager.notify(event, data)

    def actualizar_data(self):
        self.data_antigua["temperatura"] = self.data["temperatura"]
        self.data_antigua["humedad"] = self.data["humedad"]

    def encontrar_cambio(self):
        return self.data != self.data_antigua


