#Imports
from customtkinter import *
import pyautogui as pg
from PIL import Image
from ctypes import windll

#Taskbar icon Setup (For use if overrideredirect is used)
GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080

def set_appwindow():
    global hasstyle
    if not hasstyle:
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.withdraw()
        root.after(100, lambda:root.wm_deiconify())
        hasstyle=True

#Making the Base Window
root = CTk()
root.geometry("250x550")
root.resizable(False, False)
root.title("Script Clicker")
root.iconbitmap('src\\frontend\\res\\logo\\scriptclicker_32.ico')
root.overrideredirect(True)

scwin = CTkFrame(root, fg_color="#181818")
scwin.pack(fill="both", expand="1")

#Place program in center
def place_center():
    global x, y
    reso = pg.size()
    rx = reso[0]
    ry = reso[1]
    x = int((rx/2) - (root.winfo_width()/2))
    y = int((ry/2) - (root.winfo_height()/2))
    root.geometry(f"+{x}+{y}")
place_center()

#Place program on top
root.attributes('-topmost',True)
root.attributes('-topmost',False)

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

#Minimize and Unminize Functionality
def miniWindow(event):
    global hasstyle
    root.update_idletasks()
    root.overrideredirect(False)
    root.state("iconic")
    hasstyle = False
    
def unminiWindow(event):
    root.update_idletasks()
    root.overrideredirect(True)
    set_appwindow()
    root.state("normal")

def hoverMiniE(event):
    minimize.configure(image=miniimg_hover)
    
def hoverMiniL(event):
    minimize.configure(image=miniimg)

#Loading TitleBar Images
logoimg = CTkImage(light_image=Image.open("src\\frontend\\res\\logo\\scriptclicker_24.png"))
closeimg = CTkImage(light_image=Image.open("src\\frontend\\res\\icons\\close.png"))
closeimg_hover = CTkImage(light_image=Image.open("src\\frontend\\res\\icons\\close_hover.png"))
miniimg = CTkImage(light_image=Image.open("src\\frontend\\res\\icons\\minimize.png"))
miniimg_hover = CTkImage(light_image=Image.open("src\\frontend\\res\\icons\\minimize_hover.png"))

#Building the Titlebar
titleBar = CTkFrame(scwin, bg_color="#202020")
titleBar.pack(expand=0, side="top", fill="x")
titleBar.bind("<B1-Motion>", moveWindow)
titleBar.bind("<Map>",unminiWindow)

logo = CTkLabel(titleBar, image=logoimg, text="")
logo.pack(side="left", padx=5)

title = CTkFrame(titleBar, fg_color="transparent")
title.pack(side="left", padx=3)

#Parts of Title
titleP1 = CTkLabel(title, text="</", text_color="#07BCD0", font=("Sans-serif", 15))
titleP1.grid(column=0, row=0)
titleP1.bind("<B1-Motion>", moveWindow)

titleP2 = CTkLabel(title, text="ScriptClicker", text_color="white", font=("Sans-serif", 15))
titleP2.grid(column=1, row=0)
titleP2.bind("<B1-Motion>", moveWindow)

titleP3 = CTkLabel(title, text=">", text_color="#07BCD0", font=("Sans-serif", 15))
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

#Set Taskbar Icon
hasstyle = False
root.update_idletasks()
root.withdraw()
set_appwindow()

#Window Element - CPS Counter
cpsCounter = CTkFrame(scwin, fg_color="transparent")
cpsCounter.pack()

displayCPS = CTkLabel(cpsCounter, text="000", text_color="#07BCD0")
displayCPS.pack()

lblcps = CTkLabel(cpsCounter, text="CPS", text_color="white")
lblcps.pack()

#Click Interval Functionality
def clickInt():
    print("radiobutton toggled, current value:", clickIntType.get())

#Window Element - Click Interval
clickIntFrame = CTkFrame(scwin, fg_color="transparent")
clickIntFrame.pack()

lblClickInt0 = CTkFrame(clickIntFrame, fg_color="transparent")
lblClickInt0.pack()
lblClickIntP1 = CTkLabel(lblClickInt0, text="$", text_color="#07BCD0", font=("Sans-serif", 15))
lblClickIntP1.grid(column=0, row=0)
lblClickIntP2 = CTkLabel(lblClickInt0, text="Click Interval", text_color="white", font=("Sans-serif", 15))
lblClickIntP2.grid(column=1, row=0)

clickIntType = StringVar(value="miliseconds")
milisecIntOp = CTkRadioButton(clickIntFrame, text="Miliseconds", command=clickInt, variable=clickIntType, value="miliseconds")
milisecIntOp.pack()
cpsIntOp = CTkRadioButton(clickIntFrame, text="CPS", command=clickInt, variable=clickIntType, value="cps")
cpsIntOp.pack()

minClickInt = CTkEntry(clickIntFrame)
minClickInt.pack()

lbldash = CTkLabel(clickIntFrame, text="-")
lbldash.pack()

maxClickInt = CTkEntry(clickIntFrame)
maxClickInt.pack()

#Window Element - Repeat


#End of Window Creation
root.mainloop()