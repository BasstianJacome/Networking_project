import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from data_generator import create_data
from data_packager import package_data
from random import randint
from paho.mqtt.client import Client, CallbackAPIVersion

class PublisherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MQTT Publisher")
        self.create_widgets()
        self.client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='Yeshi')
        self.client_pub.connect("localhost", 1883)
        self.running = False

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.publish_button = ttk.Button(self.frame, text="Start Publishing", command=self.start_publishing)
        self.publish_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.stop_button = ttk.Button(self.frame, text="Stop Publishing", command=self.stop_publishing)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.clear_button = ttk.Button(self.frame, text="Clear Display", command=self.clear_display)
        self.clear_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.status_label = ttk.Label(self.frame, text="", anchor="center")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")

        self.result_text = tk.Text(self.frame, height=10, width=50)
        self.result_text.grid(row=2, column=0, columnspan=3, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.result_text.yview)
        self.scrollbar.grid(row=2, column=3, pady=5, sticky="ns")
        self.result_text.config(yscrollcommand=self.scrollbar.set)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=0)
        self.frame.rowconfigure(2, weight=1)

    def start_publishing(self):
        self.status_label.config(text="Publishing data...")
        self.running = True
        self.publish_data()

    def stop_publishing(self):
        self.status_label.config(text="Stopped publishing")
        self.running = False
     

    def publish_data(self):
        if not self.running:
            return
        data = create_data()
        temperature_value = data['air_temp']
        packet_id = data['id']
        timestamp = data.get('date', 'N/A')  # Get timestamp or 'N/A' if not present
        wind = data.get('winds', 'N/A')
        humidity = data.get('humidity')
        packaged_data = package_data(temperature_value, packet_id)
        self.client_pub.publish('TEMPERATURE', packaged_data)  # Publish data to the 'TEMPERATURE' topic
        display_text = f'Temperature: {temperature_value}°C\n'
        display_text += f'Timestamp: {timestamp}\n'
        display_text += f'Packet ID: {packet_id}\n'
        display_text += f'Wind: {wind} km/h\n'
        display_text += f'Humidity: {humidity}\n\n'
        self.result_text.insert(tk.END, display_text)
        self.root.after(1000, self.publish_data)

    def clear_display(self):
        self.result_text.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PublisherGUI(root)
    root.mainloop()
