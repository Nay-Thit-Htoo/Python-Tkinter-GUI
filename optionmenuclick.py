import tkinter as tk
OptionList=[
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer"
]
root=tk.Tk()
root.geometry('100x200')
variable=tk.StringVar(root)
variable.set(OptionList[0])

opt=tk.OptionMenu(root,variable,*OptionList)
opt.config(width=90,font=('ZawgyiOne',12))
opt.pack(side="top")

labeltest=tk.Label(text="",font=("ZawgyiOne",12),fg='red')
labeltest.pack(side="top")

def callback(*args):
    labeltest.config(text=variable.get())

variable.trace("w",callback)
root.mainloop()
