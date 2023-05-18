#import class library tkinter and rename it to tk.
import tkinter as tk
from tkinter import ttk

#Create a function for selecting items
def on_select(event):

    #Create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Create root window object, call class of tkinter and change object's title
root = tk.Tk()
root.title("Bubble Tea")

#Create an array object called items
items = ["Classic", "Jasmine green tea", "Thai tea", "Matcha", "Brown sugar"]
#Create the combox box object, put the object in the root window and populate values.
combo_box = ttk.Combobox(root, values=items)

#The bind function will tie the selected item to the on_selected function.
combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the object to the screen with the Geometry manager.
combo_box.pack()

#mainloop keeps the root parent window visible
root.mainloop