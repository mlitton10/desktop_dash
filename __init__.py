import tkinter as tk


def get_screen_size():
    root = tk.Tk()
    # set the window to be transparent or "iconic" to avoid it flashing on screen
    root.attributes('-alpha', 0)
    # Alternatively, you can use root.state('iconic') for a similar effect

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.destroy()  # Close the small Tkinter window that was created
    return screen_width, screen_height
