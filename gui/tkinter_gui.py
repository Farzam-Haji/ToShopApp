import tkinter as tk
from backend.logic import fetch_monItems, months
from backend.database import CommonDB, MonthDB
from bidi.algorithm import get_display
import arabic_reshaper
from PIL import Image, ImageTk


def image_strech(canva, image, event):
	global resized_tk
	width = event.width
	height = event.height
	resized_img = image.resize((width,height))
	resized_tk = ImageTk.PhotoImage(resized_img)
	canva.create_image(0, 0, image = resized_tk, anchor='nw')




def switch_month(homFrame, monFrame):
	homFrame.forget()
	monFrame.tkraise()
	monFrame.pack(fill='both', expand=True)


def switch_home(homFrame, monFrame):
	monFrame.forget()
	homFrame.tkraise()
	homFrame.pack(fill='both', expand=True)


def convert(text):
		reshaped = arabic_reshaper.reshape(text)
		return get_display(reshaped)


def start_gui(mdb:MonthDB, cdb:CommonDB):

	# Basic config
	app = tk.Tk()
	app.title("ToShop App")
	app.geometry("400x500")

	# Menu
	menuBar = tk.Menu(app)
	app.config(menu = menuBar)

	menuMenu = tk.Menu(menuBar, tearoff=0)
	menuMenu.add_command(label="Home", command=lambda:switch_home(homeFrame, monthFrame))
	menuMenu.add_command(label="Common")
	menuMenu.add_separator()
	menuMenu.add_command(label="Exit", command = app.destroy)
	menuBar.add_cascade(label="Menu", menu=menuMenu)

	helpMenu = tk.Menu(menuBar, tearoff=0)
	helpMenu.add_command(label="Help")
	menuBar.add_cascade(label="Help", menu=helpMenu)

	# images
	paperimg = Image.open("assets/2.png")
	papertk = ImageTk.PhotoImage(paperimg)

	# Main frame config
	frame = tk.Frame(app)
	frame.pack(fill="both", expand=True)



	# Home frame
	homeFrame = tk.Frame(frame)

	## top
	topFrame = tk.Frame(homeFrame)

	topFrame.columnconfigure(0, weight=9)
	topFrame.columnconfigure(1, weight=1)

	tk.Label(topFrame, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
	tk.Button(topFrame, text="Common List").grid(row=0, column=1, sticky=tk.W+tk.E)
	tk.Button(topFrame, text="Help").grid(row=1, column=1, sticky=tk.W+tk.E)

	topFrame.pack(fill='x')

    ## bottom
	botFrame = tk.Frame(homeFrame)

	for i in range(3):
		botFrame.columnconfigure(i, weight=1)

	for i in range(4):
		botFrame.rowconfigure(i, weight=1)

	monlist = months(mdb)
	for i, month in enumerate(monlist):
		but = tk.Button(botFrame, text=convert(month), font=("Arial", 14), command=lambda:switch_month(homeFrame, monthFrame))
		but.grid(row=i // 3, column=i % 3, sticky="nsew")

	botFrame.pack(fill='both', expand=True)

	

	# Month frame
	monthFrame = tk.Frame(frame)
	# Canvas
	canvas = tk.Canvas(monthFrame, bd=0, highlightthickness=0, relief='ridge')
	canvas.pack(fill='both', expand=True)
	canvas.bind('<Configure>', lambda event:image_strech(canvas, paperimg, event))

	# Content
	innerFrame = tk.Frame(canvas)
	canvas.create_window(0,0, window=innerFrame, anchor='nw')

	
	items, cost = fetch_monItems(mdb,2)
	for i, item in enumerate(items):
		tk.Label(canvas, text=f"{i+1}. {item}", bg='#f5f5f5', bd=0).pack()

	tk.Label(canvas, text=f"cost= {str(cost)}", bg='#f5f5f5', bd=0).pack()
	# label = tk.Label(canvas, text="this is month frame", bg='#f5f5f5', bd=0) 
	# canvas.create_window(100, 50, window=label)
	#
	switch_home(homeFrame, monthFrame)





	app.mainloop()