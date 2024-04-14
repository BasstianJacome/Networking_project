'''
LAB 11 - Group 3

Course and Section: COMP216-003 (2024-Winter)
Professor: Rissan Devaraja
Deadline: 2024-03-30

Amanda Yuri Monteiro Ike
Oluwatobiloba Abel
Rithin Peter
Vinicio Jacome Gomez
Yeshi Ngawang
'''


import paho.mqtt.client as mqtt
import json

# from group_3_data_generator import print_data

BROKER = 'localhost'
PORT = 1883
# TOPIC = 'TEMP-COMP216'
TOPIC = 'TEMPERATURE'


# Define Callback functions
def on_connect(client, userdata, flags, rc, properties=None):
    print(f'Connected with result code {rc}')


def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(payload)
    data = json.loads(payload)
    print("Received data:")
    print(f"Timestamp: {data['timestamp']}")
    print(f"Temperature: {data['temperature']}")
    print(f"Packet ID: {data['packet_id']}")



def on_disconnect(client, userdata, rc, properties=None):
    print(f'Disconnected with result code {rc}')


# Create Subscriber client instance and implement callback functions
client_sub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='COMP-216-Group3_Sub')
# client_sub.on_connect = on_connect
client_sub.on_message = on_message
# client_sub.on_disconnect = on_disconnect

# Connect to broker
client_sub.connect(BROKER, PORT)
client_sub.subscribe(TOPIC)

# Start the loop
client_sub.loop_forever()

