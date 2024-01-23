from tkinter import *
# a GUI toolkit
from tkinter.ttk import *
# tkinter module, used for creating the graphical user interface.

from time import strftime
# Imports the strftime function from the time module, which will be used to retrieve and format the current time.


root = Tk()
# Creates a Tkinter window. The Tk() function initiates the main window.
root.title("Digital Clock")
# Sets the title of the created window to "Digital Clock".

def time():
    string = strftime('%H:%M:%S %p')
    # hours, minutes, seconds, and AM/PM.
    label.config(text=string)
    # Updates the text content of the Label component with the time obtained.
    label.after(1000, time)
    # Calls the time() function every second (1000 milliseconds) to update the time.
    
label = Label(root, font=("ds-digital", 80), background="black", foreground="pink")
# Creates a Label component where the time will be displayed. This label is placed in the root window.
label.pack(anchor="center")
# Positions the label in the center of the window.

time()
# Initiates the function time() to start updating and displaying the time

mainloop()
# Runs the GUI application, enabling it to remain open and responsive to user interactions until it's manually closed. This keeps the window running and the program operational until the user decides to close it.
    