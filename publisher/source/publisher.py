# publisher.py

import paho.mqtt.client as mqtt
import time
from DataGenerator import DataGenerator
from Data_packager import package_data

# Initialize DataGenerator
data_generator = DataGenerator()

# Initialize MQTT client
client = mqtt.Client()
client.connect("broker.example.com", 1883)

# Publish data at regular intervals
while True:
    # Generate temperature value
    temperature_value = data_generator.generate_value()

    # Package data
    packet_id = data_generator.packet_id
    data = package_data(temperature_value, packet_id)

    # Publish data to broker
    client.publish("temperature_topic", data)

    time.sleep(1)  # Adjust interval as needed

