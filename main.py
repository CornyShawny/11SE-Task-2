import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter
from timeit import default_timer as timer
import random

# word pool for the typing test
with open("words.txt") as f:
    WORDS = f.read().split()

# main window
root = tb.Window(themename="cyborg") # theme for tkinter
root.title("Typing Speed Test") # window title
root.attributes('-fullscreen', True) # fullscreen

# title within the window
title = tb.Label(root, text = "Typing Speed Test", font = ("Century", 24, "bold"), bootstyle = "light")
title.pack(pady=10)

# subheading welcoming the user to the app
subheading = tb.Label(root, text = "Welcome to the Typing Speed Test!!!",  font = ("Century", 14), bootstyle = "light")
subheading.pack(pady=10)

# subheading asking how many words for the test
howmanywords = tb.Label(root, text = "How many words?", font = ("Century", 10), bootstyle = "light")
howmanywords.pack(padx=5)

# entry box for word count
wordcount = ttk.Entry(root, font=("Century", 8))
wordcount.pack(padx=10)
wordcount.focus()

# display words
words_display = tb.Label(root, text="", font=("Century", 8, "bold"), bootstyle="light", wraplength=1200)
words_display.pack(pady=10)

# text entry (to type)
text_entry = tb.Entry(root, font=("Century", 8), bootstyle="light", width=50)
text_entry.pack(pady=5)
text_entry.config(state="disabled") # disabled until started

# timer label
time = tb.Label(root, text="Time: 0.0 sec", font=("Century", 10), bootstyle="light")
time.pack(pady=5)

# label to display wpm results
results = tb.Label(root, text="", font=("Century", 10), bootstyle="light")
results.pack(pady=5)

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
        text_entry.focus() # focuses on the entry box (you can start typing without clicking on the box)

def update_timer():
    """updates the timer label every 100ms"""
    global start_time, running_timer
    if start_time:
        elapsed_time = timer() - start_time  # calculate run time
        time.config(text=f"Time: {elapsed_time:.1f} sec")  # update display
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
        results.config(text=f"Your speed: {wpm} WPM")  # display results
        root.after_cancel(running_timer)  # stop the timer

# buttons
generate = tb.Button(root, text="Generate Words", command=generate_words, bootstyle="success")
generate.pack(pady=5)

submit = tb.Button(root, text="Submit", command=end_typing, bootstyle="danger")
submit.pack(pady=5)

exit = tb.Button(root, text="Exit", command=root.quit, bootstyle="danger")
exit.pack(pady=100)

# typing automatically starts timer
text_entry.bind("<Key>", start_typing)

root.mainloop()

# add highscore (WPM)