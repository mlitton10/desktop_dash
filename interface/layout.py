import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from utils import get_screen_size


class Dashboard(Window):
    def __init__(self, themename='darkly'):
        super().__init__(themename="darkly")

        self.title("DesktopDash")

        screen_width, screen_height = get_screen_size()

        self.geometry("{}x{}".format(int(screen_width * 0.9), int(screen_height * 0.9)))

        w = tk.Label(self, text='Hello World')
        w.grid(row=0, column=0, padx=20, pady=20)
        button = tk.Button(self, text='Stop', width=25, command=self.destroy)
        button.grid(row=0, column=1, padx=20, pady=20)

        pass


if __name__ == "__main__":
    desktop_dash = Dashboard()
    desktop_dash.mainloop()