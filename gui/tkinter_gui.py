import tkinter as tk
from backend.logic import months
from backend.database import MonthDB
from bidi.algorithm import get_display
import arabic_reshaper

def convert(text):
	reshaped = arabic_reshaper.reshape(text)
	return get_display(reshaped)


def start_gui(mdb:MonthDB):
	root = tk.Tk()
	root.geometry("400x500")
	root.title("To Shop App")

	menubar = tk.Menu(root)
	#
	menumenu = tk.Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Menu", menu=menumenu)
	menumenu.add_command(label="Common")
	menumenu.add_separator()
	menumenu.add_command(label="Exit", command=root.destroy)
	#
	menuhelp = tk.Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Help", menu=menuhelp)
	menuhelp.add_command(label="Help")


	topframe = tk.Frame()
	topframe.pack(fill='x')

	topframe.columnconfigure(0, weight=9)
	topframe.columnconfigure(1, weight=1)

	monLabel = tk.Label(topframe, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
	comButton = tk.Button(topframe, text="Common List").grid(row=0, column=1, sticky=tk.W+tk.E)
	helpButton = tk.Button(topframe, text="Help").grid(row=1, column=1, sticky=tk.W+tk.E)


	monthFrame = tk.Frame(root)
	monthFrame.pack(fill='both', expand=True)

	for i in range(3):
		monthFrame.columnconfigure(i, weight=1)
	for i in range(4):
		monthFrame.rowconfigure(i, weight=1)

	monlist = months(mdb)
	for i, month in enumerate(monlist):
		row = i // 3 
		col = i % 3
		but = tk.Button(monthFrame, text=convert(month), font=("Arial", 14))
		but.grid(row=row, column=col, sticky="nsew")


	root.config(menu = menubar)
	root.mainloop()