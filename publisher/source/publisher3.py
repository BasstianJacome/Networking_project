import paho.mqtt.client as mqtt
import time
from data_packager import package_data
from tkinter import Tk
from publisher_gui import VerticalBarDisplay
from data_generator import DataGenerator

BROKER = 'mqtt.eclipseprojects.io'
PORT = 1883
TOPIC = 'TEMPERATURE'

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected to broker with result code {reason_code}')

def on_publish(client, userdata, mid):
    print(f'Message published with MID: {mid}')

def update_temperature_value(value):
    global temperature_value
    temperature_value = value

client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='Publisher')
client_pub.on_connect = on_connect
client_pub.on_publish = on_publish
client_pub.connect(BROKER, port=PORT)
client_pub.loop_start()

# Initialize GUI
root = Tk()
app = VerticalBarDisplay(root)

# Register the callback function to update temperature_value whenever it changes in the GUI
app.update_temperature = update_temperature_value

packet_id = 1  # Initial packet ID

try:
    while True:
        # Get the temperature value
        temperature_value = app.value.get()

        # Package the temperature value
        data = package_data(temperature_value, packet_id)

        # Publish the temperature value
        print(f'Publishing temperature value: {temperature_value}')
        print(f'Packaged data: {data}')
        client_pub.publish(TOPIC, data)

        # Increment packet_id for the next iteration
        packet_id += 1

        time.sleep(1)

        # Update the GUI to handle events and update the temperature value
        root.update()

except KeyboardInterrupt:
    print("Exiting...")
    client_pub.disconnect()
    root.destroy()
