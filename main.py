import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter
from timeit import default_timer as timer
import random

# word pool for the typing test
with open("words.txt") as f:
    WORDS = f.read().split()

class Base:
    """base class to share"""
    def __init__(self):
        # start typing timer
        self._start_time = None
        self._running_timer = None
    
    def reset_timer(self, ui):
        """resets timer and UI"""
        self._start_time = None
        ui.time_label.config(text="Time: 0.0 sec")

    def get_start_time(self):
        """getter method for start time"""
        return self._start_time
    
    def set_start_time(self, value):
        """setter method for updating start time"""
        self._start_time = value

class Function(Base):
    """functions for the typing test"""
    def __init__(self):
        super().__init__() # inherit attributes from base class

    def toggle_fullscreen(self, ui):
        """toggles fullscreen mode on or off"""
        state = ui.root.attributes('-fullscreen')
        ui.root.attributes('-fullscreen', not state) # switch state

    def update_timer(self, ui):
        """updates timer every 100ms"""
        if self.get_start_time():
            elapsed_time = timer() - self.get_start_time() # calculate elapsed time
            ui.time_label.config(text=f"Time: {elapsed_time:.1f} sec") # update display
            self._running_timer = ui.root.after(100, lambda: self.update_timer(ui)) # recursive update

    def start_typing(self, event, ui):
        """starts timer when typing begins"""
        if self.get_start_time() is None:
            self.set_start_time(timer()) # store start time
            self.update_timer(ui) # begin tracking time

    def calculate_wpm(self, ui):
        """calculates and displays wpm"""
        if self.get_start_time():
            elapsed_time = timer() - self.get_start_time() # calculate elapsed time
            wpm = round(len(ui.text_entry.get().split()) / (elapsed_time / 60)) # calculate wpm
            ui.result_label.config(text=f"Your speed: {wpm} WPM") # display wpm results

            if self._running_timer:
                ui.root.after_cancel(self._running_timer) # stop timer

    def generate_words(self, ui):
            """generates and displays random set of words"""
            num_words = int(ui.word_count.get()) if ui.word_count.get().isdigit() else 0 # ensure input valid
            if num_words:
                ui.word_display.config(text=" ".join(random.choices(WORDS, k=num_words))) # select words
                ui.text_entry.config(state="normal") # enable text entry
                ui.text_entry.delete(0, tk.END) # clear previous entry
                ui.text_entry.focus() # focus on text box
                self.reset_timer(ui) # reset timer when generating new words

class UI:
    """all the ui for the typing test"""
    def __init__(self, root, logic):
        """Initialize UI elements and bind user interactions."""
        self.root = root # main tkinter window
        self.logic = logic

        # app title
        self.title = tb.Label(root, text="Typing Speed Test", font=("Century", 48, "bold"), bootstyle="light")
        self.title.pack(pady=10)

        # subheading 
        self.subheading = tb.Label(root, text="Welcome to the Typing Speed Test!!!", font=("Century", 24), bootstyle="light")
        self.subheading.pack(pady=10)

        # word count prompt
        self.how_many_words = tb.Label(root, text="How many words?", font=("Century", 20), bootstyle="light")
        self.how_many_words.pack(padx=5)

        # entry box to input number of words
        self.word_count = ttk.Entry(root, font=("Century", 16))
        self.word_count.pack(padx=10)
        self.word_count.focus()

        # display generated words
        self.word_display = tb.Label(root, text="", font=("Century", 16, "bold"), bootstyle="light", wraplength=1200)
        self.word_display.pack(pady=10)

        # typing text box
        self.text_entry = tb.Entry(root, font=("Century", 16), bootstyle="light", width=50)
        self.text_entry.pack(pady=5)
        self.text_entry.config(state="disabled") # starts disabled

        # keybinds
        self.text_entry.bind("<Key>", lambda event: self.logic.start_typing(event, self)) # starts timer when typing begins
        self.text_entry.bind("<Return>", lambda event: self.logic.calculate_wpm(self)) # submit test when after using "enter" key
        
        # timer display
        self.time_label = tb.Label(root, text="Time: 0.0 sec", font=("Century", 20), bootstyle="light")
        self.time_label.pack(pady=5)

        # wpm result display
        self.result_label = tb.Label(root, text="", font=("Century", 20), bootstyle="light")
        self.result_label.pack(pady=5)

        # button to generate words
        self.generate = tb.Button(root, text="Generate Words", command=lambda: self.logic.generate_words(self), bootstyle="success")
        self.generate.pack(pady=5)

        # generate words using "enter" key instead of the button
        self.word_count.bind("<Return>", lambda event: self.logic.generate_words(self))

        # submit button
        self.submit = tb.Button(root, text="Submit", command=lambda: self.logic.calculate_wpm(self), bootstyle="danger")
        self.submit.pack(pady=5)

        # exit button
        self.exit = tb.Button(root, text="Exit", command=root.quit, bootstyle="danger")
        self.exit.pack(pady=100)

        # fullscreen button
        self.fullscreen = tb.Button(root, text="Toggle Fullscreen", command=lambda: self.logic.toggle_fullscreen(self), bootstyle="primary")
        self.fullscreen.pack(pady=5)

class Main:
    """main app connecting functions and UI"""
    def __init__(self, root):
        self.root = root
        self.logic = Function()
        self.ui = UI(root, self.logic)

# run application
root = tb.Window(themename="cyborg")
app = Main(root)
root.mainloop()

# add highscore (WPM)