import json
from datetime import datetime

def package_data(temperature_value, packet_id):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a dictionary to represent the data
    data = {
        "timestamp": timestamp,
        "temperature": temperature_value,
        "packet_id": packet_id
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)

    return json_data
