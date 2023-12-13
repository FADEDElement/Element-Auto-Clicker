#Imports
from customtkinter import *

class scriptClicker(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

if __name__ == "__main__":
    scApp = scriptClicker()
    scApp.mainloop()