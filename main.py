import tkinter as tk
import ttkbootstrap as tb # theme for tkinter

root = tb.Window(themename="cyborg") # theme for tkinter
root.title("Typing Speed Test") # window title
root.geometry("1920x1080") # window size

tb.Label(
    root,
    text = "Typing Speed Test",
    font = ("System", 48, "bold",),
    bootstyle = "light"
    ).pack(pady=10)

root.mainloop()