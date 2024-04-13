# data_packager.py

import json
from datetime import datetime

def package_data(value, packet_id):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'value': value,
        'timestamp': timestamp,
        'packet_id': packet_id
        # Add any other metadata you need
    }
    return json.dumps(data)
