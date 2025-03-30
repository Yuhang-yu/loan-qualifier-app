# code_00_window.py
import tkinter as tk

#create the main window
root = tk.Tk()
root.title("my first GUI window")

#create label
label = tk.Label(
    root,
    text = "hello, MGS3001 W01"
)
#lay out label
label.pack()
#run forever
root.mainloop()