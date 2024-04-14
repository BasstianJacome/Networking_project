import paho.mqtt.client as mqtt
import time
from data_packager import package_data
from tkinter import Tk
from publisher_gui import VerticalBarDisplay
import threading
from data_generator import DataGenerator

BROKER = 'localhost'
PORT = 1883
TOPIC = 'TEMPERATURE'

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f'Connected to broker with result code {reason_code}')

def on_publish(client, userdata, mid):
    print(f'Message published with MID: {mid}')

def update_temperature_value(value):
    global temperature_value
    temperature_value = value

def publish_message():
    data_generator.increment_packet_id()  # Increment packet ID
    packet_id = data_generator.packet_id  # Access the updated packet ID
    temperature_value = app.value.get()
    data = package_data(temperature_value, packet_id)
    print(f'Publishing temperature value: {temperature_value}, Packet ID: {packet_id}')
    print(f'Packaged data: {data}')
    client_pub.publish(TOPIC, data)
    threading.Timer(1, publish_message).start()  # Publish a message every second


client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='Publisher')
client_pub.on_connect = on_connect
client_pub.on_publish = on_publish
client_pub.connect(BROKER, port=PORT)
client_pub.loop_start()

root = Tk()
app = VerticalBarDisplay(root)
app.update_temperature = update_temperature_value

# Initialize DataGenerator instance
data_generator = DataGenerator()

# Start publishing messages
publish_message()

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Exiting...")
    client_pub.disconnect()
    root.destroy()

