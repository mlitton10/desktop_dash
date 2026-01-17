import tkinter as tk
import ttkbootstrap as ttk


class WeatherDisplayFrame(ttk.Frame):
    def __init__(self, master):
        # This is a template frame for a weather display. Fake data for now
        super().__init__(master)

        weather_dict = {'My Home': {'Temperature': '54', 'Precip': 0, 'Wind': 10}}
        title = ttk.Label(self, text=list(weather_dict.keys())[0])
        title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        for i, (name, value) in enumerate(weather_dict[list(weather_dict.keys())[0]].items()):
            name_label = ttk.Label(self, text=name)
            name_label.grid(row=i+1, column=0, padx=10, pady=10, sticky='ew')

            value_label = ttk.Label(self, text=value)
            value_label.grid(row=i+1, column=1, padx=10, pady=10, sticky='ew')
        pass
    pass