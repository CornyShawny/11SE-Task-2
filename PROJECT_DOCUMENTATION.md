# **11SE Task 2 2025 - Typing Speed Tester**
### By Shawn

# **Sprint 1**
## **Requirements Definition**
### **Functional Requirements**
Consider the following elements when developing your functional requirements.

- **Data Retrieval:** What does the user need to be able to view in the system?

The user needs to be able to view the randomised words for the typing test and their input as they type them which will end after the chosen amount of words are typed. The system should take the data of how much time the user took to type those words in the typing test and then calculate the words per minute.

- **User Interface:** What is required for the user to interact with the system?

The user should be able to view and type out the randomised words and interact with the button to try it again. There will also be an option to change how many words the user wants in the speed test. If there is an error made while typing, the user cannot progress until the error is resolved (they type the right character). There should also be an exit button either on the user interface or just on the window to exit the application.

- **Data Display:** What information does the user need to obtain from the system? What needs to be output for the user?

The user needs to be able to view their words per minute result after finishing the typing test, the amount of words they chose, as well as the time taken to type it.

### **Non-Functional Requirements**
Consider the following elements when developing your non-functional requirements:

- **Performance:** How well does the system need to perform? 

The user needs to be able to instantly register the user's input from the keyboard to ensure better precision and accuracy when measuring the WPM/typing speed.

- **Reliability:** How reliable does the system and data need to be?

The system should be very reliable, as any errors or inaccuracy when retrieving data will result in an inaccurate result for displaying the WPM.

- **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

The system needs to be easy to navigate with minimalistic UI and display elements. The instructions on how to use/access the system will be in the README.md file attached with this project.

## **Determining Specifications**
### **Functional Specifications**
What does the system actually NEED to do?

- **User Requirements**
    - What does the user need to be able to do? List all specifications here.

The user needs to be able to input/type letters of the given words into the system to be able to complete the typing test. The user also needs to be able to exit the application either by clicking on the exit button for the window, or click on a designated/custom button. They should be able to restart the typing test whenever they need (during or after the test).

- **Inputs & Outputs**
    - What inputs will the system need to accept and what outputs will it need to display?

The system should accept keyboard inputs that the user types to do the typing test, as well as mouse (clicking) inputs to close the window. The system should output the randomised words that are for the typing test, and colour/highlight each letter when an input is received. After the typing test is completed, the system should output the statistics of the test (words per minute, how many words typed, and how much time it took for them to type it) and have a restart button at all times to either reset the run or the words.

- **Core Features**
    - At its core, what specifically does the program need to be able to do?

The program needs to receive the inputs from the user, check if they are right, if not then there is a output (highlight of wrong letter) where the user needs to and at the end, needs to calculate the speed that the user typed.

- **User Interaction**
    - How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?

The user will interact with the system through an advanced GUI that is easy to navigate, with many buttons and text outputs to make it easier to use. A READ.ME file is attached with the program and it provides steps on how to use the typing speed test.

- **Error Handling**
    - What possible errors could you face that need to be handled by the system?

Possible errors faced could be related to the API (dictionary) that is used by the system to provide randomised words for the typing test. Other errors could be something to do with the numbers being too long (wpm) which can be resolved by getting the result to round up or down. The system could also face calculation errors when it is calculating the wpm or processing the data.

### **Non-Functional Specifications**
- **Performance**
    - How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?

The system should perform tasks almost instantly, like updating the "Words Typed: " amount in real-time. This fast system response is required to maintain user engagement. The program can be ensured to be efficient by simplifying and correctly formatting code.

- **Useability / Accessibility**
    - How might you make your application more accessible? What could you do with the User Interface to improve usability?

To make the application more accessible, there could be options to change the font size, the font, or the highlight/font colours to improve visibility. To make the User Interface easier to use, the buttons should be clear and labelled to improve visibility as well.

- **Reliability**
    - What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Illogical calculation? Menu navigation going to wrong places?

Issues could include the inaccurate calculation of the wpm, the wpm being too long in decimals, or illogical calculation (words typed divided by 0 minutes). There could also be an issue when receiving the inputs from the user. These problems should be resolved and tested to ensure the reliability of the system.

### **Use Case**
A use case in software development is a structured description of how a user (or system) interacts with a software application to achieve a specific goal. It defines:

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

## **Review**

## **Launch**

# **Sprint 2**
## **Design**

## **Build and Test**

## **Review**

## **Launch**

# **Sprint 3**
## **Design**

## **Build and Test**

## **Review**

## **Launch**

# **Sprint 4**
## **Design**

## **Build and Test**

## **Review**

## **Launch**
