#-*- coding: ibm852 -*-
"""
  Simple statistics application

  Inspired by:
  https://www.tutorialspoint.com/what-is-the-correct-way-to-implement-a-custom-popup-tkinter-dialog-box
  https://tkdocs.com/index.html

  Written by Janusz Opi�a and students of Python course 2025
"""

# Import required libraries
from tkinter import *
from tkinter import ttk
from tkinter import constants, messagebox

zad = 1
print("Loading zad 1/", zad); zad +=1
import obliczenia as T01

## Now lets create an instance of tkinter frame
win = Tk()
# Set the window size
win.geometry("615x190")
win.minsize(615,190)
win.maxsize(615,190)

def About():
  messagebox.showinfo('SuperSTAT', 'Program written by students of 2025 Python introductory class,\nver.: 2025/03/22.1')

def Quit(*event):
  quit()

def NoModule():
  messagebox.showinfo('ERROR', 'Module is improperly implemented, run directly')

# options for buttons
## for pack: button_opt = {'fill': constants.BOTH, 'padx': 15, 'pady': 5}
grid_opt = {'padx' : 15, 'pady' : 5}

# Create a Label widget
Mlabel  = Label(win, text="[ Select module ]", font=('Arial', 14))
Mlabel.grid(row=0, columnspan=5)

MStatus = Label(win, text="...", font=('Arial', 14))
MStatus.grid(row=5, columnspan=5)
#Mlabel.pack(pady=40)

# Create commands buttons
ttk.Button(win, text="[  Temat 01   ]", command=lambda: T01.click_fun(win, Mlabel)).grid(row=1, column=0, **grid_opt)
ttk.Button(win, text="[  Temat 02   ]", command=NoModule).grid(row=1, column=1, **grid_opt)
ttk.Button(win, text="[  Temat 03   ]", command=NoModule).grid(row=1, column=2, **grid_opt)
ttk.Button(win, text="[  Temat 04   ]", command=NoModule).grid(row=1, column=3, **grid_opt)
ttk.Button(win, text="[  Temat 05   ]", command=NoModule).grid(row=1, column=4, **grid_opt)

ttk.Button(win, text="[  Temat 06*  ]", command=NoModule).grid(row=2, column=0, **grid_opt)
ttk.Button(win, text="[  Temat 07*  ]", command=NoModule).grid(row=2, column=1, **grid_opt)
ttk.Button(win, text="[  Temat 08*  ]", command=NoModule).grid(row=2, column=2, **grid_opt)
ttk.Button(win, text="[  Temat 09*  ]", command=NoModule).grid(row=2, column=3, **grid_opt)
ttk.Button(win, text="[  Temat 10*  ]", command=NoModule).grid(row=2, column=4, **grid_opt)

ttk.Button(win, text="[  Temat 11*  ]", command=NoModule).grid(row=3, column=0, **grid_opt)
ttk.Button(win, text="[  Temat 12*  ]", command=NoModule).grid(row=3, column=1, **grid_opt)
ttk.Button(win, text="[  Temat 13*  ]", command=NoModule).grid(row=3, column=2, **grid_opt)
ttk.Button(win, text="[  Temat 14*  ]", command=NoModule).grid(row=3, column=3, **grid_opt)
ttk.Button(win, text="[  Temat 15*  ]", command=NoModule).grid(row=3, column=4, **grid_opt)

#=====================
ttk.Button(win, text="[ O programie: ]", command=About).grid(row=4,column=2, columnspan = 2 )
ttk.Button(win, text="[    Zamknij   ]", command=Quit).grid(row=4, column=3, columnspan = 2)
win.bind("<KeyPress-Escape>", Quit)
win.protocol("WM_DELETE_WINDOW", Quit)
# start interface:
win.mainloop()
## print(f"(Main)data = {data}") # global variable data is known to all madules
