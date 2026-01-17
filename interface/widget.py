import tkinter as tk
import ttkbootstrap as ttk


class WeatherDisplayFrame(ttk.Frame):
    def __init__(self, master, weather_dict):
        # This is a template frame for a weather display. Fake data for now
        super().__init__(master)

        title = ttk.Label(self, text=list(weather_dict.keys())[0], font=('Arial',50))
        title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        for i, (name, value) in enumerate(weather_dict[list(weather_dict.keys())[0]].items()):
            name_label = ttk.Label(self, text=name)
            name_label.grid(row=i+1, column=0, padx=10, pady=10, sticky='ew')

            value_label = ttk.Label(self, text=value)
            value_label.grid(row=i+1, column=1, padx=10, pady=10, sticky='ew')
        pass
    pass