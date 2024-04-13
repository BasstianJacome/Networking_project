import time
from random import uniform

import paho.mqtt.client as mqtt

BROKER = 'mqtt.eclipseprojects.io'
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connection Rason Code: {reason_code}')

def on_publish(client, userdata, mid, reason_code, properties):
    print(f'Publish Reason Code {reason_code} for Message ID: {mid}')

def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print(f'Connection Closed Reason Code {reason_code}')
    client_pub.loop_stop()

client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='Temperature')
client_pub.on_connect = on_connect
client_pub.on_publish=on_publish
client_pub.on_disconnect=on_disconnect
client_pub.connect(BROKER, port=PORT)
client_pub.loop_start()


for i in range (7):
    random_value = uniform (10.0,32.0)
    client_pub.publish('COMP216-TEMP', random_value)
    print(f'Publishing {random_value} to Topic: COMP216-TEMP')
    time.sleep(2)

client_pub.disconnect()
