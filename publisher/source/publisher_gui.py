import tkinter as tk
from tkinter import messagebox


class VerticalBarDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("Vertical Bar Display")

        self.temperature = 18  # Initialize temperature variable
        self.value = tk.DoubleVar()
        self.value.set(self.temperature)

        self.bar = tk.Canvas(master, width=20, height=200, bg="white")
        self.bar.pack(pady=10)
        self.update_bar()

        self.entry = tk.Entry(master, textvariable=self.value)
        self.entry.pack(pady=5)

        self.update_button = tk.Button(master, text="Update Temperature", command=self.update_temperature)
        self.update_button.pack(pady=5)

        info_label = tk.Label(master, text="Indoor Temperature (°C)\nLow: 18°C, Normal: 22-25°C, High: 40°C",
                              justify="left")
        info_label.pack()

    def update_bar(self):
        # Update the bar
        value = self.value.get()
        self.bar.delete("all")
        bar_height = (value - 18) * 10
        self.bar.create_rectangle(5, 200 - bar_height, 15, 200, fill="blue")

    def update_temperature(self):
        new_temp = self.entry.get()
        try:
            new_temp = float(new_temp)
            if 18 <= new_temp <= 40:
                self.value.set(new_temp)
                self.update_bar()
                print("Updated temperature value:", new_temp)  # Add this line to print the updated temperature
            else:
                messagebox.showerror("Error", "Temperature must be between 18°C and 40°C.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numerical value for temperature.")

    def get_temperature(self):
        return self.temperature


if __name__ == "__main__":
    root = tk.Tk()
    app = VerticalBarDisplay(root)
    root.mainloop()
