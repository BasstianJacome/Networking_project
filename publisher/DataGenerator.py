# data_generator.py

import random
import json
from datetime import datetime

class DataGenerator:
    def __init__(self):
        self.pattern = 'stock'  # Default pattern
        self.packet_id = 0

    def set_pattern(self, pattern):
        self.pattern = pattern

    def generate_value(self):
        if self.pattern == 'stock':
            # Generate random stock value
            value = random.uniform(50, 200)  # Example range
        elif self.pattern == 'temperature':
            # Generate random temperature
            value = random.uniform(10, 30)  # Example range
        else:
            # Handle unknown pattern
            value = None

        self.packet_id += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps({'value': value, 'timestamp': timestamp, 'packet_id': self.packet_id})
