from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert, stop!" "This is the virus police, we have surrounded an intruder")
button=Button(root,text="Scanning for virus", command=msg)
button.place(x=40, y=80)
root.mainloop()