import tkinter as tk
from tkinter import filedialog
import time
from tkinter.ttk import *
from audiobook import read
import os
root=tk.Tk()
root.state("zoomed")
root.configure(bg="pink")

def uploadFiles():
    filename = filedialog.askopenfilename()
    full_path = os.path.realpath(filename)
    print(full_path)
    pb1 = Progressbar(
        root, 
        orient="horizontal", 
        length=300, 
        mode='determinate'
        )
    pb1.place(x=550,y=350)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    tk.Label(root, text='File Uploaded Successfully!', anchor="center",bg="light green",font=("arial",50),fg="blue").place(x=420,y=350)
    button = tk.Button(root, text='PLAY NOW',highlightbackground="blue",width=20,height=2,command=lambda:read(filename))
    button.place(x=600,y=590)
    changeOnHover(button, "red", "blue")
    button2 = tk.Button(root, text='QUIT',highlightbackground="blue",width=20,height=2,command=stop)
    button2.place(x=600,y=700)
    changeOnHover(button2, "red", "blue")

def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        highlightbackground=colorOnHover))
 
    button.bind("<Leave>", func=lambda e: button.config(
        highlightbackground=colorOnLeave))

def stop():
    root.destroy()


welcome = tk.Label(text="Welcome To Audiobook",anchor="center",bg="light green",font=("arial",110,"bold"),fg="red").place(x=100,y=100)

button1 = tk.Button(root, text='UPLOAD',highlightbackground="blue",width=20,height=2, command=uploadFiles)
button1.place(x=600,y=480)
changeOnHover(button1, "red", "blue")

root.mainloop()


