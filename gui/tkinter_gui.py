import tkinter as tk
from backend.logic import months
from backend.database import CommonDB, MonthDB
from bidi.algorithm import get_display
import arabic_reshaper

def convert(text):
	reshaped = arabic_reshaper.reshape(text)
	return get_display(reshaped)

class App(tk.Tk):
	def __init__(self, mdb:MonthDB, cdb:CommonDB):
		super().__init__()
		self.title("ToShop App")
		self.geometry("400x500")

		menubar = tk.Menu(self)
		self.config(menu=menubar)
		#
		menumenu = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Menu", menu=menumenu)
		menumenu.add_command(label="Common")
		menumenu.add_separator()
		menumenu.add_command(label="Exit", command=self.destroy)
		#
		menuhelp = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Help", menu=menuhelp)
		menuhelp.add_command(label="Help")

		self.frames = {}
		for F in (MainFrame, MonthFrame):
			frame = F(self, self, mdb, cdb)
			self.frames[F.__name__] = frame
			frame.pack()

		self.show_frame("MainFrame")

	def show_frame(self, name):
		frame = self.frames[name]
		frame.tkraise()


class MainFrame(tk.Frame):
	def __init__(self, parent, controller, mdb, cdb):
		super().__init__(parent)

		topframe = tk.Frame()
		topframe.pack(fill='x')

		topframe.columnconfigure(0, weight=9)
		topframe.columnconfigure(1, weight=1)

		monLabel = tk.Label(topframe, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
		comButton = tk.Button(topframe, text="Common List").grid(row=0, column=1, sticky=tk.W+tk.E)
		helpButton = tk.Button(topframe, text="Help").grid(row=1, column=1, sticky=tk.W+tk.E)


		monthFrame = tk.Frame()
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







class MonthFrame(tk.Frame):
	def __init__(self, parent, controller, mdb, cdb):
		super().__init__(parent)

class CommonWindow(tk.Toplevel):
	pass





# def start_gui(mdb:MonthDB):
# 	root = tk.Tk()
# 	root.geometry("400x500")
# 	root.title("To Shop App")

# 	menubar = tk.Menu(root)
# 	#
# 	menumenu = tk.Menu(menubar, tearoff=0)
# 	menubar.add_cascade(label="Menu", menu=menumenu)
# 	menumenu.add_command(label="Common")
# 	menumenu.add_separator()
# 	menumenu.add_command(label="Exit", command=root.destroy)
# 	#
# 	menuhelp = tk.Menu(menubar, tearoff=0)
# 	menubar.add_cascade(label="Help", menu=menuhelp)
# 	menuhelp.add_command(label="Help")


# 	topframe = tk.Frame()
# 	topframe.pack(fill='x')

# 	topframe.columnconfigure(0, weight=9)
# 	topframe.columnconfigure(1, weight=1)

# 	monLabel = tk.Label(topframe, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
# 	comButton = tk.Button(topframe, text="Common List").grid(row=0, column=1, sticky=tk.W+tk.E)
# 	helpButton = tk.Button(topframe, text="Help").grid(row=1, column=1, sticky=tk.W+tk.E)


# 	monthFrame = tk.Frame(root)
# 	monthFrame.pack(fill='both', expand=True)

# 	for i in range(3):
# 		monthFrame.columnconfigure(i, weight=1)
# 	for i in range(4):
# 		monthFrame.rowconfigure(i, weight=1)

# 	monlist = months(mdb)
# 	for i, month in enumerate(monlist):
# 		row = i // 3 
# 		col = i % 3
# 		but = tk.Button(monthFrame, text=convert(month), font=("Arial", 14))
# 		but.grid(row=row, column=col, sticky="nsew")


# 	root.config(menu = menubar)
# 	root.mainloop()