import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter
from timeit import default_timer as timer
import random

# word pool for the typing test
WORDS = ["hi", "bye", "dog", "cat", "he", "her", "she", "him", "them", "they", "school", "teacher", "student", "deputy", "sheriff", "police", "car", "truck", "bike", "bicycle", "when", "was", "then"]

# main window
root = tb.Window(themename="cyborg") # theme for tkinter
root.title("Typing Speed Test") # window title
root.geometry("1280x720") # window size
root.configure(bg="#121212")

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
    font = ("System", 28),
    bootstyle = "light"
)
subheading.pack(pady=20)

# subheading asking how many words for the test
howmanywords = tb.Label(
    root,
    text = "How many words?",
    font = ("System", 20),
    bootstyle = "light"
)
howmanywords.pack(pady=5)

# choices for word count
wordcountchoices = ["10", "25", "50", "100"]

# dropdown box to select word count
wordcount = ttk.Combobox(root, values = wordcountchoices)
wordcount.set("Select an option")
wordcount.pack(pady=10)

# display words
words_display = tb.Label(root, text="", font=("System", 22, "bold"), bootstyle="light")
words_display.pack(pady=15)

# text entry (to type)
text_entry = tb.Entry(root, font=("System", 22), bootstyle="light")
text_entry.pack(pady=10)
text_entry.config(state="disabled") # disabled until started

# label to display wpm results
text_entry = tb.Entry(root, font=("System", 22), bootstyle="light", state="disabled", width=50)
text_entry.pack(pady=10)

# start typing timer
start_time = None

def generate_words():
    """generate and display a random set of words"""
    num_words = int(wordcount.get()) if wordcount.get().isdigit() else 0
    words_display.config(text=" ".join(random.choices(WORDS, k=num_words))) if num_words else None
    text_entry.config(state="normal")
    text_entry.delete(0, tk.END)
    text_entry.focus()

def start_typing():
    """starts the timer when user begins typing"""
    global start_time
    start_time = timer()

def end_typing():
    """calculate and display wpm"""
    global start_time
    if start_time:
        wpm = round(len(text_entry.get().split()) / ((timer() - start_time) / 60))
        result_label.config(text=f"Your speed: {wpm} WPM")

# buttons
tb.Button(root, text="Generate Words", command=generate_words, bootstyle="success").pack(pady=10)
tb.Button(root, text="Start Typing", command=start_typing, bootstyle="primary").pack(pady=10)
tb.Button(root, text="Submit", command=end_typing, bootstyle="danger").pack(pady=15)

root.mainloop()

# add highscore (WPM)