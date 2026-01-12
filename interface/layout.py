import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import get_screen_size

root = ttk.Window(themename="darkly")
root.title("DesktopDash")

screen_width, screen_height = get_screen_size()

root.geometry("{}x{}".format(screen_width, screen_height))

w = tk.Label(root, text='Hello World')
w.pack()

root.mainloop()