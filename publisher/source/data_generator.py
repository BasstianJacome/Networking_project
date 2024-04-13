import random

class DataGenerator:
    def __init__(self):
        self.packet_id = 0

    def generate_value(self):
        # Generate a random temperature value between 0 and 100
        temperature = round(random.uniform(0, 100), 2)
        return temperature

# Create an instance of DataGenerator
data_generator = DataGenerator()

# Generate a temperature value
temperature_value = data_generator.generate_value()

# Print the generated temperature value
print("Generated Temperature Value:", temperature_value)