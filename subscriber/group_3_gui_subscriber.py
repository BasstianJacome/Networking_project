'''
Final Project - Group 3

Course and Section: COMP216-003 (2024-Winter)
Professor: Rissan Devaraja
Deadline: 2024-04-16

Amanda Yuri Monteiro Ike
Oluwatobiloba Abel
Rithin Peter
Vinicio Jacome Gomez
Yeshi Ngawang
'''


import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from queue import Queue
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import paho.mqtt.client as mqtt
from random import randint
from group_3_smtp import send_email
from datetime import datetime

class IoTDataSubscriber:
    _broker = 'localhost'
    _port = 1883

    def __init__(self, topic='TEMPERATURE'):
        self.sub_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"client_{randint(100, 200)}")
        self.topic = topic
        self.queue = Queue()

    def on_connect(self, client, userdata, flags, reason, properties):
        print(f"Connected with result code {reason}")
        client.subscribe(self.topic)

    # Function to check the quality of the data and send an email if there is any invalid value
    def data_quality_check(self, data, min_value=18, max_value=27):
        
        error_msg = []

        # check if data is null
        if data is None:
            error_msg.append("Data is None. Verify the IoT device to check if it is operational.")
            return False
        else:
            temperature = data['temperature']
            timestamp = data['timestamp']
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Check temperature value (null and if it is within the range of min and max degrees Celsius)
            if temperature is None:
                error_msg.append("Temperature value is None. Verify the IoT device to check if it is operational.")
            elif temperature < min_value or temperature > max_value:
                error_msg.append(f'Temperature value {temperature} is out of range. Min: {min_value} Max: {max_value}')
        
            # Check timestamp value (null and if it is bigger than the current time)
            if timestamp is None:
                error_msg.append("Timestamp is None. Verify the IoT device to check if it is operational.")
            # check if timestamp is bigger than the current time
            elif timestamp > current_time:
                error_msg.append(f'Timestamp is bigger than the current time ({current_time}). Verify the IoT device to check if it is operational.')
                
            # If error msg is not None, send email to the recipient with the error message
            if len(error_msg) > 0:
                print(error_msg)
                send_email('2024comp216group3@gmail.com', self.topic, error_msg, data)
                return False
            else:
                return True

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()}")
        payload = msg.payload.decode()
        data = json.loads(payload)

        if self.data_quality_check(data):
            self.queue.put(float(data['temperature']))

    def sub_connect(self):
        print(f'Connecting to {IoTDataSubscriber._broker} on port {IoTDataSubscriber._port}')
        self.sub_client.on_connect = self.on_connect
        self.sub_client.on_message = self.on_message
        self.sub_client.connect(IoTDataSubscriber._broker, IoTDataSubscriber._port)

    def block(self):
        self.sub_client.loop_forever()

class DisplayChart(Tk):
    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)

        
        sizer = Canvas(width=800, height=700)
        sizer.pack()

        self.list_values = []
        self.count_msg = 0

        self.create_styles()
        self.create_ui()

        self.iot_data_subscriber = IoTDataSubscriber()
        self.iot_data_subscriber.sub_connect()

        self.thread = Thread(target=self.data_consumer)
        self.thread.daemon = True
        self.thread.start()

        self.after(1000, self.update_chart)

    def create_styles(self):
        style = Style()
        style.configure('TFrame', padding=(2, 2, 6, 6))
        style.configure('Heading.TLabel', padding=(2, 2, 4, 4), font=('Arial', 16, 'bold', 'italic'), align='center')

    def create_ui(self):
        frame_header = Frame(self)
        frame_header.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.15)
        Button(frame_header, text='Exit', command=self.quit).place(relx=0.80, rely=0, relwidth=0.2, relheight=0.25)
        Label(frame_header, text='Temperature - Historical Data', style='Heading.TLabel').pack(expand=True)

        frame = Frame(self)
        frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.45)

        self.canvas_frame = Frame(frame)
        self.canvas_frame.place(relx=0, rely=0.35, relwidth=1, relheight=0.65)

    def exit_gui(self):
        #self.destroy()
        self.iot_data_subscriber.sub_client.disconnect()
        self.quit()

    def data_consumer(self):
        self.iot_data_subscriber.block()

    # Function to update the chart with the last 20 values from the subscriber's queue/list
    def update_chart(self):
        while not self.iot_data_subscriber.queue.empty():
            self.list_values.append(self.iot_data_subscriber.queue.get())
            self.count_msg += 1

        values_to_plot = self.list_values[-20:]  # Last 20 values
        plt.clf()
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.plot(range(len(values_to_plot)), values_to_plot, color='red', marker='o', linestyle='--')
        ax.set_xlabel('Index', labelpad=20)
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Line Chart - Historical Data')
        ax.set_xticks(range(len(values_to_plot)))        

        # Increment the x-axis by 1 to follow the index of the values from the subscriber
        if len(self.list_values) > 20:
            diff_len = len(self.list_values) - 20

            ax.set_xticklabels([i for i in range(diff_len, len(self.list_values))])
        else:
            ax.set_xticklabels([i for i in range(0, len(values_to_plot))])
        
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1) #.pack(side=TOP, fill=BOTH, expand=1)

        if hasattr(self, "canvas_widget"):
            self.canvas_widget.get_tk_widget().destroy()

        self.canvas_widget = canvas
        self.after(1000, self.update_chart)

# Main function
app = DisplayChart("Dynamic Display")
app.mainloop()
