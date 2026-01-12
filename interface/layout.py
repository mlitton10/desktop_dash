import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
root.title("DesktopDash")
root.geometry("500x300")

w = tk.Label(root, text='Hello World')
w.pack()

root.mainloop()