import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import get_screen_size



class Dashboard:
    def __init__(self):
        root = ttk.Window(themename="darkly")
        root.title("DesktopDash")

        screen_width, screen_height = get_screen_size()

        root.geometry("{}x{}".format(int(screen_width*0.9), int(screen_height*0.9)))

        w = tk.Label(root, text='Hello World')
        w.pack()
        button = tk.Button(root, text='Stop', width=25, command=root.destroy)
        button.pack()
        root.mainloop()

        pass


if __name__=="__main__":
    desktop_dash = Dashboard()
