#Imports
import tkinter as tk
import pyautogui as pg

#Creating the window
root = tk.Tk()
root.geometry("250x550")
root.overrideredirect(True)
root.resizable(False, False)

simpleAC = tk.Frame(root, bg="#181818", highlightbackground="#787b7d", highlightthickness=1)
simpleAC.pack(expand=1, fill="both")

# Placing the window in the center of the screen
def place_center():
    root.update_idletasks()
    global x, y
    reso = pg.size()
    rx = reso[0]
    ry = reso[1]
    x = int((rx/2) - (root.winfo_width()/2))
    y = int((ry/2) - (root.winfo_height()/2))
    root.geometry(f"+{x}+{y}")
    
place_center()

#Titlebar move window funtionality
lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
    
root.bind('<Button-1>', SaveLastClickPos)

def moveWindow(event):
    root.geometry(f"+{event.x - lastClickX + root.winfo_x()}+{event.y - lastClickY + root.winfo_y()}")

#Close Window Button Functionality
def closeWindow(event):
    root.destroy()

def hoverCloseE(event):
    closeButton.config(fg="#0abdd1")
    
def hoverCloseL(event):
    closeButton.config(fg="white")

#Minimize Window Functionality
def miniWindow(event):
    root.state("withdrawn")
    root.overrideredirect(False)
    root.state('iconic')
    
def uniminiWindow(event):
    root.overrideredirect(True)
    root.state("normal")
    
root.bind("<Map>", uniminiWindow)

def hoverMiniE(event):
    miniButton.config(fg="#0abdd1")
    
def hoverMiniL(event):
    miniButton.config(fg="white")

#Creating the title bar
titleBar = tk.Frame(simpleAC, bg="#202020")
titleBar.pack(expand=0, side="top", fill="x")
titleBar.bind("<B1-Motion>", moveWindow)

title = tk.Label(titleBar, text="</ScriptClicker>", justify="right", fg="white", bg="red", font=("Sans-serif 15"), pady=2)
title.pack(side="left", expand=0, fill="x")

closeButton = tk.Label(titleBar, text='X', fg="white", bg="#202020", font=("Sans-serif 15"), cursor="hand2")
closeButton.pack(side="right")
closeButton.bind("<Button-1>", closeWindow)
closeButton.bind("<Enter>", hoverCloseE)
closeButton.bind("<Leave>", hoverCloseL)

miniButton = tk.Label(titleBar, text='_', fg="white", bg="#202020", font=("Sans-serif 15"), cursor="hand2")
miniButton.pack(side="right")
miniButton.bind("<Button-1>", miniWindow)
miniButton.bind("<Enter>", hoverMiniE)
miniButton.bind("<Leave>", hoverMiniL)

root.mainloop()