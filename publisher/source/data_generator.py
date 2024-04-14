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

import random
import time

start_id = 123  # Initial sequence number

def create_data():
    global start_id
    start_id += 1
    data = {
        'id': start_id,
        'year': random.randint(2000, 2023),
        'month': random.randint(1, 12),
        'day': random.randint(1, 28),  # Assuming February has 28 days for simplicity
        'date': None,  # Placeholder for date
        'latitude': round(random.uniform(-90, 90), 4),
        'longitude': round(random.uniform(-180, 180), 4),
        'winds': round(random.uniform(0, 10), 2) if random.random() > 0.1 else None,
        'humidity': round(random.uniform(0, 100), 2) if random.random() > 0.1 else None,
        'air_temp': round(random.uniform(17, 38), 2) if random.random() > 0.1 else None,
        'ss_temp': round(random.uniform(17, 40), 2) if random.random() > 0.1 else None
    }
    data['date'] = f"{data['year']}-{data['month']}-{data['day']}"

    # print(type(data)) # checking the type of data
    return data

def print_data(data):
    print("Data:")
    for key, value in data.items():
        print(f"{key}: {value}")

# Test the functions
if __name__ == "__main__":
    sample_data = create_data()
    print_data(sample_data)
