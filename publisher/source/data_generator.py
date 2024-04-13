import random

class DataGenerator:
    def __init__(self):
        self.packet_id = 0

    def generate_value(self):
        # Generate a random temperature value between 0 and 100
        temperature = round(random.uniform(0, 100), 2)
        return temperature
