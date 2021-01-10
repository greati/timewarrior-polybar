import tkinter as ttk
import timew

timew = timew.TimeWarrior()

win = ttk.Tk()
win.title("Start tracking")
lbl = ttk.Label(win, text = "Tag: ").grid(column = 0, row = 0)
def click():
    tag = name.get()
    if tag is not None and tag != "":
        timew.start(tags=[tag])
        win.quit()
name = ttk.StringVar()
nameEntered = ttk.Entry(win, width = 12, textvariable = name)
nameEntered.grid(column = 1, row = 0)
nameEntered.focus_set()
button = ttk.Button(win, text = "Start", command = click).grid(row = 1, column=0, sticky="nesw", columnspan=2)
win.mainloop()
