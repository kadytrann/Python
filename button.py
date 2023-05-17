#import class library. renamed tkinter to tk
import tkinter as tk

#declaring function and output comes out as "Button clicked!"
def button_click():
    print("Button clicked!")
#Creating the root window and giving it a title of "Button Example"
root = tk.Tk()
root.title("Button Example")

#Create button object and calling class of tkinter and button. Adding 3 arguments, root, text, and event.
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()
#This keeps the function open and running
root.mainloop