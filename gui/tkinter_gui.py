import tkinter as tk
from backend.logic import fetch_monItems, months
from backend.database import CommonDB, MonthDB
from bidi.algorithm import get_display
import arabic_reshaper






class App(tk.Tk):
	def __init__(self, mdb:MonthDB, cdb:CommonDB):
		super().__init__()

		self.title("ToShop App")
		self.geometry("400x500")

		# Menu
		menuBar = tk.Menu(self)
		self.config(menu = menuBar)

		menuMenu = tk.Menu(menuBar, tearoff=0)
		menuMenu.add_command(label="Home")
		menuMenu.add_command(label="Common")
		menuMenu.add_separator()
		menuMenu.add_command(label="Exit", command = self.destroy)
		menuBar.add_cascade(label="Menu", menu=menuMenu)

		helpMenu = tk.Menu(menuBar, tearoff=0)
		helpMenu.add_command(label="Help")
		menuBar.add_cascade(label="Help", menu=helpMenu)

		mainFrame = tk.Frame(self)
		mainFrame.pack(fill="both", expand=True)

		self.frames = {"main":MainFrame(self, mainFrame, mdb), "month":MonthFrame(self, mainFrame, mdb)}
		self.show_frame("main")

	

	def show_frame(self, name):
		if name == "month":
			self.frames["main"].forget()
		else:
			self.frames["month"].forget()

		frame = self.frames[name]
		frame.tkraise()
		frame.pack(fill='both', expand=True)

	def convert(self, text):
		reshaped = arabic_reshaper.reshape(text)
		return get_display(reshaped)


class MainFrame(tk.Frame):
	def __init__(self, parrent, mainFrame, mdb):
		super().__init__(mainFrame)

		# Upper Frame
		topFrame = tk.Frame(self)

		topFrame.columnconfigure(0, weight=9)
		topFrame.columnconfigure(1, weight=1)

		tk.Label(topFrame, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
		tk.Button(topFrame, text="Common List").grid(row=0, column=1, sticky=tk.W+tk.E)
		tk.Button(topFrame, text="Help").grid(row=1, column=1, sticky=tk.W+tk.E)

		topFrame.pack(fill='x')

		# Bottom Frame
		botFrame = tk.Frame(self)

		for i in range(3):
			botFrame.columnconfigure(i, weight=1)

		for i in range(4):
			botFrame.rowconfigure(i, weight=1)

		monlist = months(mdb)
		for i, month in enumerate(monlist):
			but = tk.Button(botFrame, text=parrent.convert(month), font=("Arial", 14), command = lambda:parrent.show_frame("month"))
			but.grid(row=i // 3, column=i % 3, sticky="nsew")

		botFrame.pack(fill='both', expand=True)

		self.pack(fill='both', expand=True)

class MonthFrame(tk.Frame):
	def __init__(self, parrent, mainFrame, mdb):
		super().__init__(mainFrame)

		items, cost = fetch_monItems(mdb,2)
		for i, item in enumerate(items):
			tk.Label(self, text=f"{i+1}. {item}").pack()

		tk.Label(self, text=f"cost= {str(cost)}").pack()
		# monframe = tk.Frame(self)
		# tk.Label(monframe, text="month items").pack()
		# monframe.pack()


		self.pack(fill='both', expand=True)

