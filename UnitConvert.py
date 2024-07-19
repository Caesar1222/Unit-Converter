from tkinter import *
from tkinter import ttk

def calculateFtoM(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def calculateFtoC(*args):
    try:
        value = float(fahrenheit.get())
        celsius.set(int(value - 32)*(5/9))
    except ValueError:
        pass

def calculatelbtokg(*args):
    try:
        value = float(pound.get())
        kilogram.set(int(value)* (0.45359237))
    except ValueError:
        pass


root = Tk()
root.title("Unit Converter")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

### Converting Feet to Meters ###

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=1, row=1, sticky=(E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=4, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculateFtoM).grid(column=5, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Feet").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="=").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Meters").grid(column=5, row=1, sticky=W)

### Converting Fahrenheit to Celsius ###

fahrenheit = StringVar()
fahrenheit_entry = ttk.Entry(mainframe, width= 7, textvariable=fahrenheit)
fahrenheit_entry.grid(column=1, row=3, sticky=(E))

celsius = StringVar()
ttk.Label(mainframe, textvariable=celsius).grid(column=4, row=3, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculateFtoC).grid(column=5, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Fahrenheit").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="=").grid(column=3, row=3, sticky=E)
ttk.Label(mainframe, text="Celsius").grid(column=5, row=3, sticky=W)

### Converting Pounds to Kilograms

pound = StringVar()
pound_entry = ttk.Entry(mainframe, width= 7, textvariable=pound)
pound_entry.grid(column=1, row=5, sticky=(E))

kilogram = StringVar()
ttk.Label(mainframe, textvariable=kilogram).grid(column=4, row=5, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculatelbtokg).grid(column=5, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Pounds").grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="=").grid(column=3, row=5, sticky=E)
ttk.Label(mainframe, text="Kilograms").grid(column=5, row=5, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=8, pady=8)

feet_entry.focus()
root.bind("<Return>", calculateFtoM)

root.mainloop()