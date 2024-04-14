from tkinter import Tk
from publisher_gui import VerticalBarDisplay


class DataGenerator:
    def __init__(self):
        self.packet_id = 0


def print_temperature(value):
    print("Current Temperature:", value)


if __name__ == "__main__":
    root = Tk()
    app = VerticalBarDisplay(root)


    # Define a function to continuously update and print the temperature value
    def update_and_print_temperature():
        temperature_value = app.value.get()
        print_temperature(temperature_value)
        root.after(1000, update_and_print_temperature)  # Schedule the next update


    # Start the continuous update and print loop
    update_and_print_temperature()

    root.mainloop()
