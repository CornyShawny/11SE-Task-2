import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter
from timeit import default_timer as timer
import random

class SpeedTypingTest:
    def __init__(self, root):
        """Initialise the main game window and variables."""
        self.root = tb.Window(themename="cyborg") # theme for tkinter
        self.root.title("Typing Speed Test") # window title
        self.root.geometry("1920x1080") # window size
        pass
    
    def setup_ui(self):
        """Set up the UI components such as labels, buttons, and text entry field."""
        
        pass
    
    def check_result(self):
        """Compare the user's input with the expected sentence and calculate the WPM."""
        pass
    
    def reset_test(self):
        """Reset the test with a new sentence and restart the timer."""
        pass



# title within the window
title = tb.Label(
    root,
    text = "Typing Speed Test",
    font = ("System", 48, "bold"),
    bootstyle = "light"
)
title.pack(pady=10)

# subheading welcoming the user to the app
subheading = tb.Label(
    root,
    text = "Welcome to the Typing Speed Test!!!",
    font = ("System", 32),
    bootstyle = "light"
)
subheading.pack(pady=10)

# subheading asking how many words for the test
howmanywords = tb.Label(
    root,
    text = "How many words?",
    font = ("System", 24),
    bootstyle = "light"
)
howmanywords.pack(pady=5)

# choices for word count
wordcountchoices = ["10", "25", "50", "100"]

# dropdown box to select word count
wordcount = ttk.Combobox(root, values = wordcountchoices)
wordcount.set("Select an option")
wordcount.pack(pady=10)

'''
function for selecting word count and outputting the choice into the console
'''
def on_select():
    selected_option = wordcount.get()
    print(f"You selected: {selected_option}")

# submit button to submit chosen word count
submit = tb.Button(root, text="Submit", command=on_select)
submit.pack(pady=10)

root.mainloop()

# add highscore (WPM)