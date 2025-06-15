import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter
from timeit import default_timer as timer
import random

# word pool for the typing test
WORDS = ["hi", "bye", "dog", "cat", "he", "her", "she", "him", "them", "they", 
         "school", "teacher", "student", "deputy", "sheriff", "police", "car",
         "truck", "bike", "bicycle", "when", "was", "then"]

# main window
root = tb.Window(themename="cyborg") # theme for tkinter
root.title("Typing Speed Test") # window title
root.geometry("1280x720") # window size
root.configure(bg="#121212") # set background colour

# title within the window
title = tb.Label(root, text = "Typing Speed Test", font = ("System", 48, "bold"), bootstyle = "light")
title.pack(pady=10)

# subheading welcoming the user to the app
subheading = tb.Label(root, text = "Welcome to the Typing Speed Test!!!",  font = ("System", 28), bootstyle = "light")
subheading.pack(pady=20)

# subheading asking how many words for the test
howmanywords = tb.Label(root, text = "How many words?", font = ("System", 20), bootstyle = "light")
howmanywords.pack(padx=5)

# choices for word count
wordcountchoices = ["10", "25", "50", "100"]

# dropdown box to select word count
wordcount = ttk.Combobox(root, values = wordcountchoices, font=("System", 14))
wordcount.set("Select an option")
wordcount.pack(padx=10)

# display words
words_display = tb.Label(root, text="", font=("System", 22, "bold"), bootstyle="light")
words_display.pack(pady=15)

# text entry (to type)
text_entry = tb.Entry(root, font=("System", 16), bootstyle="light")
text_entry.pack(pady=10)
text_entry.config(state="disabled") # disabled until started

# timer label
timer_label = tb.Label(root, text="Time: 0.0 sec", font=("System", 20), bootstyle="light")
timer_label.pack(pady=10)

# label to display wpm results
result_label = tb.Label(root, text="", font=("System", 22), bootstyle="light")
result_label.pack(pady=10)

# start typing timer
start_time = None
running_timer = None

def generate_words():
    """generate and display a random set of words from word pool"""
    num_words = int(wordcount.get()) if wordcount.get().isdigit() else 0 # validate input
    if num_words:
        words_display.config(text=" ".join(random.choices(WORDS, k=num_words))) # random select words
        text_entry.config(state="normal")
        text_entry.delete(0, tk.END)
        text_entry.focus()

def update_timer():
    """updates the timer label every 100ms"""
    global start_time, running_timer
    if start_time:
        elapsed_time = timer() - start_time  # calculate run time
        timer_label.config(text=f"Time: {elapsed_time:.1f} sec")  # update display
        running_timer = root.after(100, update_timer)  # update every 100ms

def start_typing(event=None):
    """starts the timer when user begins typing"""
    global start_time, running_timer
    if start_time is None: # makes sure timer only starts once
        start_time = timer()
        update_timer()

def end_typing():
    """calculate and display words per minute (WPM) when user submits"""
    global start_time, running_timer
    if start_time:
        elapsed_time = timer() - start_time  # total typing duration
        wpm = round(len(text_entry.get().split()) / (elapsed_time / 60))  # calculate WPM
        result_label.config(text=f"Your speed: {wpm} WPM")  # display results
        root.after_cancel(running_timer)  # stop the timer

# buttons
tb.Button(root, text="Generate Words", command=generate_words, bootstyle="success").pack(pady=10)
tb.Button(root, text="Submit", command=end_typing, bootstyle="danger").pack(pady=15)

# typing automatically starts timer
text_entry.bind("<Key>", start_typing)

root.mainloop()

# add highscore (WPM)