import paho.mqtt.client as mqtt
import time
from data_generator import DataGenerator
from data_packager import package_data

# Initialize DataGenerator
data_generator = DataGenerator()

BROKER = 'mqtt.eclipseprojects.io'
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

for i in range (7):
    temperature_value = data_generator.generate_value()
    packet_id = data_generator.packet_id
    data = package_data(temperature_value, packet_id)
    client_pub.publish('TEMPERATURE', data)
    print(f'Publishing {temperature_value} to Topic: TEMPERATURE')
    print(f'Packaged Data: {data}')
    time.sleep(2)

client_pub.disconnect()