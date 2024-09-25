from tkinter import Tk, Label
import time

root = Tk()
root.title("DIGITAL CLOCK")

def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    display_clock.config(text=display_time)
    root.after(200, present_time)

display_clock = Label(root, font=("calibri",50), bg="black", fg="blue")
display_clock.pack()

present_time()
root.mainloop()

