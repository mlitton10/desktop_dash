import tkinter as tk
import ttkbootstrap as ttk



class Panel(ttk.Frame):
    def __init__(self, master, panel_name):
        super().__init__(master, padding=(3,3,12,12))

        self.title_text = ttk.Label(self, text=panel_name, font=('Arial', 80))
        self.title_text.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')

class WeatherPanel(Panel):
    def __init__(self, master, weather_dict, panel_name='Weather Forecast'):
        super().__init__(master, panel_name)

        self.display_1 = WeatherDisplayFrame(self, weather_dict)
        self.display_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.display_2 = WeatherDisplayFrame(self, weather_dict)
        self.display_2.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.display_3 = WeatherDisplayFrame(self, weather_dict)
        self.display_3.grid(row=1, column=2, padx=10, pady=(10, 0), sticky="nsew")


class WeatherDisplayFrame(ttk.Frame):
    def __init__(self, master, weather_dict):
        # This is a template frame for a weather display. Fake data for now
        super().__init__(master)

        title = ttk.Label(self, text=list(weather_dict.keys())[0], font=('Arial', 50), justify='center')
        title.grid(row=0, column=0, padx=40, pady=10, sticky='ew', columnspan=2)

        for i, (name, value) in enumerate(weather_dict[list(weather_dict.keys())[0]].items()):
            name_label = ttk.Label(self, text=name, font=('Arial', 20), justify='center')
            name_label.grid(row=i + 1, column=0, padx=40, pady=10, sticky='ew')

            value_label = ttk.Label(self, text=value, justify='center', font=('Arial', 20))
            value_label.grid(row=i + 1, column=1, padx=40, pady=10, sticky='ew')
        pass

    pass
