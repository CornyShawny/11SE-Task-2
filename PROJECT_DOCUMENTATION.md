# **11SE Task 2 2025 - Typing Speed Tester**
### By Shawn

# **Sprint 1**
## **Requirements Definition**
### **Functional Requirements**
- **Data Retrieval:** The user needs to be able to view the randomised words for the typing test and their input as they type them which will end after the chosen amount of words are typed. The system should take the data of how much time the user took to type those words in the typing test and then calculate the words per minute.

- **User Interface:** The user should be able to view and type out the randomised words and interact with the button to try it again. There will also be an option to change how many words the user wants in the speed test. There should also be an exit button either on the user interface or just on the window to exit the application.

- **Data Display:** The user needs to be able to view their words per minute result after finishing the typing test, the amount of words they chose, as well as the time taken to type it.

### **Non-Functional Requirements**
- **Performance:** The user needs to be able to instantly register the user's input from the keyboard to ensure better precision and accuracy when measuring the WPM/typing speed.

- **Reliability:** The system should be very reliable, as any errors or inaccuracy when retrieving data will result in an inaccurate result for displaying the WPM.

- **Usability and Accessibility:** The system needs to be easy to navigate with minimalistic UI and display elements. The instructions on how to use/access the system will be in the README.md file attached with this project.

## **Determining Specifications**
### **Functional Specifications**
- **User Requirements:**
The user needs to be able to input/type letters of the given words into the system to be able to complete the typing test. The user also needs to be able to exit the application either by clicking on the exit button for the window, or click on a designated/custom button. They should be able to restart the typing test whenever they need (during or after the test).

- **Inputs & Outputs:** The system should accept keyboard inputs that the user types to do the typing test, as well as mouse (clicking) inputs to close the window. The system should output the randomised words that are for the typing test, and colour/highlight each letter when an input is received. After the typing test is completed, the system should output the statistics of the test (words per minute, how many words typed, and how much time it took for them to type it) and have a restart button at all times to either reset the run or the words.

- **Core Features:** The program needs to receive the inputs from the user, check if they are right, if not then there is a output (highlight of wrong letter) where the user needs to and at the end, needs to calculate the speed that the user typed.

- **User Interaction:** The user will interact with the system through an advanced GUI that is easy to navigate, with many buttons and text outputs to make it easier to use. A READ.ME file is attached with the program and it provides steps on how to use the typing speed test.

- **Error Handling:** Possible errors faced could be related to the API (dictionary) that is used by the system to provide randomised words for the typing test. Other errors could be something to do with the numbers being too long (wpm) which can be resolved by getting the result to round up or down. The system could also face calculation errors when it is calculating the wpm or processing the data.

### **Non-Functional Specifications**
- **Performance:** The system should perform tasks almost instantly, like updating the "Words Typed: " amount in real-time. This fast system response is required to maintain user engagement. The program can be ensured to be efficient by simplifying and correctly formatting code.

- **Useability / Accessibility:** To make the application more accessible, there could be options to change the font size, the font, or the highlight/font colours to improve visibility. To make the User Interface easier to use, the buttons should be clear and labelled to improve visibility as well.

- **Reliability:** Issues could include the inaccurate calculation of the wpm, the wpm being too long in decimals, or illogical calculation (words typed divided by 0 minutes). There could also be an issue when receiving the inputs from the user. These problems should be resolved and tested to ensure the reliability of the system.

### **Use Case**

**Actors:**

User (person who wants to test their typing speed)

**Preconditions:**

The application needs to be open and running, with the randomised words for the test loaded.

**Main Flow:**
1. The user opens the application
2. They select the configurations for the test.
3. They start typing after the words are loading.
4. The system collects the data from the typing and calculates the analytics.
5. After the user finishes, the data gathered from the test is displayed.

**Postconditions:**

The user is given results on their test, and is met with two buttons which either restart or exit the test.

## **Design**
### **Storyboard**
![Alt text](Images/Storyboard.png)

### **Data Flow Diagram: Level 0**
![Alt text](Images/Level0DFD.png)

### **Data Flow Diagram: Level 1**
![Alt text](Images/Level1DFD.png)

### **Gantt Chart**
![Alt text](Images/Gantt%20Chart.png)

## **Build and Test**
```
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb # theme for tkinter

root = tb.Window(themename="cyborg") # theme for tkinter
root.title("Typing Speed Test") # window title
root.geometry("1920x1080") # window size

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
```

## **Review**
### **End of Sprint Review Questions**
- **Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.** As of right now, my project is a GUI that contains a dropdown box which lets the user select how many words they want to test, and there is also a submit button for users to submit their choice. These features partly fulfill my functional and non-functional requirements.

- **Analyse the performance of your program against the key use-cases you identified.** The program works well and behaves as expected, but as the program just includes the simple GUI, the use cases are only partly fulfilled.

- **Assess the quality of your code in terms of readability, structure, and maintainability.** For my code, it is well organised and readable as it has code comments and docstrings, but right now it is pretty simple.

- **Explain the improvements that should be made in the next stage of development.** The next improvements for my code would be to develop further and add more features to both the code and GUI such as generating words, being able to do the test and recieve inputs, and calculating the wpm.

## **Launch**
### **README.md**
```
# Typing Speed Test

This Python program allows you to test your typing speed with a test. You can choose how ever many words you want, and the program will generate the chosen amount in random words, which then you have to type all of them to finish the test. This program uses 'ttkbootstrap' for tkinter themes.

## Features
- Able to choose your desired amount of words
- Generates random words
- Tests your typing speed
- Processes and displays your test results (wpm, time taken, words typed etc.)

## Requirements
To run this program, you need to install the following dependencies:

- `ttkbootstrap` for tkinter themes

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```

### **requirements.txt**
```
ttkbootstrap
```

# **Sprint 2**
## **Design**
### **Structure Chart**
![Alt text](Images/Structure%20Chart.png)

### **Pseudocode**
#### **root.mainloop()**
```
BEGIN root.mainloop()
    WHILE app is running
        IF user enters word count AND clicks "Generate Words" THEN
            generate_words()
        ELSEIF user clicks "Submit" THEN
            end_typing()
        ELSEIF user clicks "Exit" THEN
            quit app
        ELSEIF user starts typing AND timer not running THEN
            start_typing()
        ENDIF
    ENDWHILE
END root.mainloop()
```

#### **generate_words()**
```
BEGIN generate_words()
    GET word count
    IF valid THEN
        SELECT that amount of random words
        DISPLAY selected words
        ENABLE text input
        FOCUS text input
    ENDIF
END generate_words()
```

#### **end_typing()**
```
BEGIN end_typing()
    IF timer running THEN
        CALCULATE time elapsed
        COUNT typed words
        wpm = (words / time) × 60
        DISPLAY wpm
        STOP timer
    ENDIF
END end_typing()
```

### **Flowcharts**
#### **root.mainloop()**
![alt text](Images/root.mainloop().png)

#### **generate_words()**
![alt text](Images/generate_words().png)

#### **end_typing()**
![alt text](Images/end_typing().png)

## **Build and Test**
```
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
```

## **Review**
### **End of Sprint Review Questions**
- **Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.** My program is mostly effective at meeting the functional and non-functional requirements from my planning. I have implemented the word generating, time ticking, wpm calculating, and some more buttons to exit, generate words, and submit the typed words.

- **Analyse the performance of your program against the key use-cases you identified.** The program works well and mostly meets the use cases, though it still needs to be refined as it is not perfect yet.

- **Assess the quality of your code in terms of readability, structure, and maintainability.** My code is easy to read as there are docstrings and comments for most of the code, and the structure is ordered well with lines to seperate different parts of the code. I believe the names of my variables are fine as of right now but might need changing in the future to avoid overlapping.

- **Explain the improvements that should be made in the next stage of development.** The improvements that should be made would probably be some usability and accessibility features like being able to press enter after finishing typing instead of the submit button, or something like a scroll bar if the amount of words gets too much. Another big feature to add would be a highscore or an accuracy test for the typing test to check the percentage accuracy of what the user has typed.

## **Launch**
### **README.md**
```
# Typing Speed Test

This Python program allows you to test your typing speed with a test. You can choose how ever many words you want, and the program will generate the chosen amount in random words, which then you have to type all of them to finish the test. This program uses 'ttkbootstrap' for tkinter themes.

## Features
- Able to choose your desired amount of words
- Generates random words
- Tests your typing speed
- Processes and displays your test results (wpm, time taken, words typed etc.)

## Requirements
To run this program, you need to install the following dependencies:

- `ttkbootstrap` for tkinter themes

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```

### **requirements.txt**
```
ttkbootstrap
```

# **Sprint 3**
## **Design**

## **Build and Test**
```
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
```

## **Review**
### **End of Sprint Review Questions**
- **Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.** I have implemented OOP features into my code, basically a rewrite of my old code, therefore also including all features in the functional and non-functional requirements, such as the ui and display.

- **Analyse the performance of your program against the key use-cases you identified.** The program performs well and the output is as expected, but I have realised that if the number of generated words is too high, the words could flood the window, or crash the application, so I need to add some restrictions. Overall, the program works well, but there needs to be some changes and fixes. 

- **Assess the quality of your code in terms of readability, structure, and maintainability.** My code is well organised and very readable, and it is even better now with OOP implemented. The code includes docstrings and code comments to explain what that specific part of code does and what it's for.

- **Explain the improvements that should be made in the next stage of development.** The only improvements that should be made are to make small improvements like making the UI look better by rearranging the UI elements, changing the colours, or changing the size. I should also add error handling, and implement restrictions into the code.

## **Launch**

# **Sprint 4**
## **Design**

## **Build and Test**

## **Review**

## **Launch**
