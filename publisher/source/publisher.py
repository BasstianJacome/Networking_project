# publisher.py

import paho.mqtt.client as mqtt
import time
from data_generator import DataGenerator
from data_packager import package_data

# Initialize DataGenerator
data_generator = DataGenerator()

# Define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")

def on_publish(client, userdata, mid):
    print("Message published")

# Initialize MQTT client with callback functions
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to broker

# We need to implement the broker 
client.connect("BROKER_NEEDED", 1883)

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
