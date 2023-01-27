from tkinter import *
from tkinter import font 
from helper import *
import constants, tkinterWidgets, helper

global label

constants.root.geometry(constants.screensize)

constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))
constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.bind("<Motion>", motion)


# Tkinter Widgets Placement
tkinterWidgets.layoutEdit.place(anchor= NW)
tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)

# we need to still get the posisions of all of the edited buttons

# Idea buttons
tkinterWidgets.settings.place(anchor = N, relx = 0.35, rely = 0.3)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.15)
tkinterWidgets.timerButton.place(anchor = N, relx = 0.95, rely = 0.20)
tkinterWidgets.googleButton.place(anchor = N, relx = 0.95, rely = 0.3)
tkinterWidgets.canvasButton.place(anchor = N, relx = 0.95, rely = 0.35)
tkinterWidgets.skywardButton.place(anchor = N, relx = 0.95, rely = 0.4)
tkinterWidgets.cleverButton.place(anchor = N, relx = 0.95, rely = 0.45)

tkinterWidgets.frame.pack()
tkinterWidgets.notes.place(anchor = N, relx = 0.5, rely = 0.5)

#calander labels
sunday = Label(constants.root, text = "Sunday")
sunday.place(anchor = N, relx = 0.2, rely = 0.15)

monday = Label(constants.root, text = "Monday")
monday.place(anchor = N, relx = 0.3, rely = 0.15)

tuesday = Label(constants.root, text = "Tuesday")
tuesday.place(anchor = N, relx = 0.4, rely = 0.15)

wednesday = Label(constants.root, text = "Wednesday")
wednesday.place(anchor = N, relx = 0.5, rely = 0.15)

thursday = Label(constants.root, text = "Thursday")
thursday.place(anchor = N, relx = 0.6, rely = 0.15)

friday = Label(constants.root, text = "Friday")
friday.place(anchor = N, relx = 0.7, rely = 0.15)

saturday = Label(constants.root, text = "Saturday")
saturday.place(anchor = N, relx = 0.8, rely = 0.15)









fonts = list(font.families())


# Below is stuff to find all font and find the one we love best

# def update(): 
#     label.config(font = (fonts[constants.index], 10))
#     print(f"Current Font: {fonts[constants.index]}")
#     label.after(2000, update)
#     constants.index += 1
        
# with open("fonts.txt", "a") as file:
#     [file.write(i) for i in fonts]

# root = Tk() 

# label = Label(root, text = "Hello, World")
# label.place(anchor = N, relx = 0.5, rely = 0.5)
# label.after(2000, update)

# root.mainloop()
constants.root.mainloop()   