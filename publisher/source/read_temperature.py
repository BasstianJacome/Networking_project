from tkinter import Tk
from publisher_gui import VerticalBarDisplay  # Importing the VerticalBarDisplay class from the GUI file

def print_temperature(value):
    print("Current Temperature:", value)

if __name__ == "__main__":
    root = Tk()
    app = VerticalBarDisplay(root)
    root.after(1000, lambda: print_temperature(app.value.get()))  # Print the temperature every second
    root.mainloop()
