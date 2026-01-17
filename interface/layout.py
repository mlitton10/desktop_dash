import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from utils import get_screen_size
from widget import WeatherDisplayFrame

class Dashboard(Window):
    def __init__(self, themename='darkly'):
        super().__init__(themename="darkly")

        self.title("DesktopDash")

        screen_width, screen_height = get_screen_size()

        self.geometry("{}x{}".format(int(screen_width * 0.9), int(screen_height * 0.9)))

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        weather_dict = {'My Home': {'Temperature': '54', 'Precip': 0, 'Wind': 10}}
        self.display_1 = WeatherDisplayFrame(self, weather_dict)
        self.display_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.display_2 = WeatherDisplayFrame(self, weather_dict)
        self.display_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.display_3 = WeatherDisplayFrame(self, weather_dict)
        self.display_3.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")

        self.button = ttk.Button(self, text="my button", command=self.destroy)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

        pass


if __name__ == "__main__":
    desktop_dash = Dashboard()
    desktop_dash.mainloop()