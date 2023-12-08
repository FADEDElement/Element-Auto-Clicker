#Imports
from customtkinter import *
import pyautogui as pg
from PIL import Image, ImageTk

#Making the Base Window
root = CTk()
root.geometry("250x550")
root.resizable(False, False)

#Center program in monitor
def place_center():
    global x, y
    reso = pg.size()
    rx = reso[0]
    ry = reso[1]
    x = int((rx/2) - (root.winfo_width()/2))
    y = int((ry/2) - (root.winfo_height()/2))
    root.geometry(f"+{x}+{y}")
place_center()

#Titlebar move window funtionality
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
root.bind('<Button-1>', SaveLastClickPos)

def moveWindow(event):
    root.geometry(f"+{event.x - lastClickX + root.winfo_x()}+{event.y - lastClickY + root.winfo_y()}")

#Close window functionality
def closeWindow(event):
    root.destroy()

def hoverCloseE(event):
    close.configure(image=closeimg_hover)
    
def hoverCloseL(event):
    close.configure(image=closeimg)
    
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
    minimize.configure(image=miniimg_hover)
    
def hoverMiniL(event):
    minimize.configure(image=miniimg)

#Loading TitleBar Images
logoimg = ImageTk.PhotoImage(Image.open("src\\frontend\\res\logo\scriptclicker.png"))
closeimg = ImageTk.PhotoImage(Image.open("src\\frontend\\res\icons\close.png"))
closeimg_hover = ImageTk.PhotoImage(Image.open("src\\frontend\\res\icons\close_hover.png"))
miniimg = ImageTk.PhotoImage(Image.open("src\\frontend\\res\icons\minimize.png"))
miniimg_hover = ImageTk.PhotoImage(Image.open("src\\frontend\\res\icons\minimize_hover.png"))

#Building the Titlebar
titleBar = CTkFrame(root, bg_color="#202020")
titleBar.pack(expand=0, side="top", fill="x")
titleBar.bind("<B1-Motion>", moveWindow)

logo = CTkLabel(titleBar, image=logoimg, text="")
logo.pack(side="left", padx=5)

title = CTkFrame(titleBar, fg_color="transparent")
title.pack(side="left", padx=3)

#Parts of Title
titleP1 = CTkLabel(title, text="</", text_color="#0abdd1", font=("Sans-serif", 15))
titleP1.grid(column=0, row=0)
titleP1.bind("<B1-Motion>", moveWindow)

titleP2 = CTkLabel(title, text="ScriptClicker", text_color="white", font=("Sans-serif", 15))
titleP2.grid(column=1, row=0)
titleP2.bind("<B1-Motion>", moveWindow)

titleP3 = CTkLabel(title, text=">", text_color="#0abdd1", font=("Sans-serif", 15))
titleP3.grid(column=2, row=0)
titleP3.bind("<B1-Motion>", moveWindow)

#Title Bar Buttons
close = CTkLabel(titleBar, image=closeimg, text="")
close.pack(side="right", padx=3)
close.bind("<Button-1>", closeWindow)
close.bind("<Enter>", hoverCloseE)
close.bind("<Leave>", hoverCloseL)

minimize = CTkLabel(titleBar, image=miniimg, text="")
minimize.pack(side="right", padx=3)
minimize.bind("<Button-1>", miniWindow)
minimize.bind("<Enter>", hoverMiniE)
minimize.bind("<Leave>", hoverMiniL)

#Closing Window Creation
root.mainloop()