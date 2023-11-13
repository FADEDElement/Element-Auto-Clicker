import tkinter

root = tkinter.Tk()
root.geometry("500x350")

frame = tkinter.Frame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tkinter.Label(master=frame, text="Hello World")
label.pack(pady=12, padx=10)

root.mainloop()