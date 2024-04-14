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
import time
from data_generator import create_data
from data_packager import package_data

# Initialize DataGenerator
data_generator = create_data()

BROKER = 'localhost'
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connection Rason Code: {reason_code}')

def on_publish(client, userdata, mid, reason_code, properties):
    print(f'Publish Reason Code {reason_code} for Message ID: {mid}')

def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print(f'Connection Closed Reason Code {reason_code}')
    client_pub.loop_stop()

client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='Sebastian')
client_pub.on_connect = on_connect
client_pub.on_publish=on_publish
client_pub.on_disconnect=on_disconnect
client_pub.connect(BROKER, port=PORT)
client_pub.loop_start()
'''
for i in range(7):
    data = create_data()  # Generate sample data directly
    temperature_value = data['air_temp']  # Extract temperature value from sample data
    packet_id = data['id']  # Extract packet ID from sample data
    packaged_data = package_data(temperature_value, packet_id)
    client_pub.publish('TEMPERATURE', packaged_data)
    print(f'Publishing {temperature_value} to Topic: TEMPERATURE')
    print(f'Packaged Data: {packaged_data}')
    time.sleep(2)
'''



while True:
    data = create_data()  # Generate sample data directly
    temperature_value = data['air_temp']  # Extract temperature value from sample data
    packet_id = data['id']  # Extract packet ID from sample data
    packaged_data = package_data(temperature_value, packet_id)
    client_pub.publish('TEMPERATURE', packaged_data)
    print(f'Publishing {temperature_value} to Topic: TEMPERATURE')
    print(f'Packaged Data: {packaged_data}')
    time.sleep(1)  # Wait for 1 second before publishing the next data



client_pub.disconnect()