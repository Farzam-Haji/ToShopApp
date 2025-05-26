
import tkinter as tk
from tkinter import ttk
from backend.logic import add_monCost, del_monItem, fetch_comItems, fetch_monItems, months
from backend.database import CommonDB, MonthDB
from bidi.algorithm import get_display
import arabic_reshaper
from PIL import Image, ImageTk


# def image_strech(canva, image, event):
# 	global resized_tk
# 	width = event.width
# 	height = event.height
# 	resized_img = image.resize((width,height))
# 	resized_tk = ImageTk.PhotoImage(resized_img)
# 	canva.create_image(0, 0, image = resized_tk, anchor='nw')


# Variable for selected month
global MonthInteger
MonthInteger = 1

def handle_delete(mdb, entry, textbox):
    itemindex = int(entry.get())
    mitems = fetch_monItems(mdb, MonthInteger)[0]
    if 1 <= itemindex <= len(mitems):
        item = mitems[itemindex - 1]
        del_monItem(mdb, MonthInteger, item)
        entry.delete(0, tk.END)
        refresh_month(textbox, mdb)
    else:
        entry.delete(0, tk.END)
        print("invalid index")


# def find_month_item(mdb, itemindex):
# 	ind = int(itemindex)-1
# 	mitems = fetch_monItems(mdb, MonthInteger)[0]
# 	if ind > len(mitems) or ind < 0:
# 		return error
# 	else:
# 		return mitems[ind]


def refresh_common(text:tk.Text, cdb):
	text.delete('1.0', tk.END)
	text.insert(tk.END, "Month Items:\n\n")

	citems, ccost = fetch_comItems(cdb)
	for i, item in enumerate(citems):
		text.insert(tk.END, f"{i+1}. {item}\n")

	text.insert(tk.END, f"\n\n\n*Estimated Cost: {ccost}*")

def refresh_month(text:tk.Text, mdb):
	text.delete('1.0', tk.END)
	text.insert(tk.END, "Month Items:\n\n")

	mitems, mcost = fetch_monItems(mdb, MonthInteger)
	for i, item in enumerate(mitems):
		text.insert(tk.END, f"{i+1}. {item}\n")

	text.insert(tk.END, f"\n\n\n*Estimated Cost: {mcost}*")

def switch_month(homFrame, monFrame, mdb, text:tk.Text, *monthInt):
	global MonthInteger
	if monthInt:
		MonthInteger = monthInt[0]
		
	homFrame.forget()
	monFrame.tkraise()

	# Adding the items in textbox
	refresh_month(text, mdb)
	monFrame.pack(fill='both', expand=True)


def switch_home(homFrame, monFrame):
	# MonthInteger = 0
	monFrame.forget()
	homFrame.tkraise()
	homFrame.pack(fill='both', expand=True)


def convert(text):
		reshaped = arabic_reshaper.reshape(text)
		return get_display(reshaped)

def open_common(master, cdb):
	top = tk.Toplevel(master)
	top.title("Common")
	top.geometry("400x500")

	topframe = tk.Frame(top)
	topframe.pack(fill='both', expand=True)

	for i in range (5):
		topframe.rowconfigure(i, weight=1)
		topframe.columnconfigure(i, weight=1)
	topframe.rowconfigure(0, weight=2)

	textframe = tk.Frame(topframe)
	textframe.grid(row=0, column=0, rowspan=2, columnspan=5, sticky='nsew')

	texbox = tk.Text(textframe, relief='groove', bd=0, bg='#f5f5f5')
	texbox.pack(fill='both', expand=True)

	vscroll = tk.Scrollbar(texbox, command=texbox.yview)
	vscroll.pack(side=tk.RIGHT, fill=tk.Y)
	texbox.configure(yscrollcommand=vscroll.set)

	texbox.insert(tk.END, "Common Items:\n\n")

	citems, cprice = fetch_comItems(cdb)
	for i, item in enumerate(citems):
		texbox.insert(tk.END, f"{i+1}. {item}\n")

	texbox.insert(tk.END, f"\n\n\n*Estimated Cost: {cprice}*")

	ttk.Separator(topframe, orient=tk.VERTICAL).grid(column=2, row=2, sticky='ns')
	ttk.Separator(topframe, orient=tk.HORIZONTAL).grid(column=0, row=3, columnspan=5, sticky='ew')

	addcostBut = tk.Button(topframe, text="Add Cost", font=("",9))
	addcostBut.grid(row=2, column=0, sticky='ew')
	addcostEntry = tk.Entry(topframe, width=10)
	addcostEntry.grid(row=2, column=1, sticky='ew')

	delItemBut = tk.Button(topframe, text="Remove", font=("",9))
	delItemBut.grid(row=2, column=3, sticky='ew')
	delItemEntry = tk.Entry(topframe, width=10)
	delItemEntry.grid(row=2, column=4, sticky='ew')

	addItemBut = tk.Button(topframe, text="Add Item", font=("",9))
	addItemBut.grid(row=4, column=0, sticky='ew')
	addItemEntry = tk.Entry(topframe)
	addItemEntry.grid(row=4, column=1, columnspan=4, sticky='ew')


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
	menuMenu.add_command(label="Common", command=lambda:open_common(app, cdb))
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



	# Month frame
	monthFrame = tk.Frame(frame)
	# Grid configuration
	for i in range (5):
		monthFrame.columnconfigure(i, weight=1)
		monthFrame.rowconfigure(i, weight=1)
	monthFrame.rowconfigure(0, weight=2)

	# Text box for items	
	textFrame = tk.Frame(monthFrame)
	textFrame.grid(row=0, column=0, rowspan=2, columnspan=5, sticky='nsew')

	textbox = tk.Text(textFrame, relief='groove', bd=0, bg='#f5f5f5')
	textbox.pack(fill='both', expand=True)

	verticalScroll = tk.Scrollbar(textbox, command=textbox.yview)
	verticalScroll.pack(side=tk.RIGHT, fill=tk.Y)
	textbox.configure(yscrollcommand=verticalScroll.set)

	textbox.insert(tk.END, "Month Items:\n\n")

	# Buttons and entries for controlling the item list
	ttk.Separator(monthFrame, orient=tk.VERTICAL).grid(column=2, row=2, sticky='ns')
	ttk.Separator(monthFrame, orient=tk.HORIZONTAL).grid(column=0, row=3, columnspan=5, sticky='ew')
	ttk.Separator(monthFrame, orient=tk.VERTICAL).grid(column=3, row=4, sticky='ns')

	addcostBut = tk.Button(monthFrame, text="Add Cost", font=("",9), command=lambda: (
		add_monCost(mdb, MonthInteger, addcostEntry.get()),
		addcostEntry.delete(0, tk.END),
		refresh_month(textbox, mdb)
		)
	)
	addcostBut.grid(row=2, column=0, sticky='ew')
	addcostEntry = tk.Entry(monthFrame, width=10)
	addcostEntry.grid(row=2, column=1, sticky='ew')

	delItemBut = tk.Button(monthFrame, text="Remove", font=("",9), command=lambda: handle_delete(mdb, delItemEntry, textbox))
	delItemBut.grid(row=2, column=3, sticky='ew')
	delItemEntry = tk.Entry(monthFrame, width=10)
	delItemEntry.grid(row=2, column=4, sticky='ew')

	addItemBut = tk.Button(monthFrame, text="Add Item", font=("",9))
	addItemBut.grid(row=4, column=0, sticky='ew')
	addItemEntry = tk.Entry(monthFrame)
	addItemEntry.grid(row=4, column=1, columnspan=2, sticky='ew')

	addCommonBut = tk.Button(monthFrame, text="Add Common", font=("", 9))
	addCommonBut.grid(row=4, column=4, sticky='ew')



	# Home frame
	homeFrame = tk.Frame(frame)

	## top
	topFrame = tk.Frame(homeFrame)

	topFrame.columnconfigure(0, weight=9)
	topFrame.columnconfigure(1, weight=1)

	tk.Label(topFrame, text="Months", font=("Arial", 20)).grid(row=0, column=0, rowspan=2)
	tk.Button(topFrame, text="Common List", command=lambda:open_common(app, cdb)).grid(row=0, column=1, sticky=tk.W+tk.E)
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
		but = tk.Button(botFrame, text=convert(month), font=("Arial", 14), command=lambda m=i+1: switch_month(homeFrame, monthFrame, mdb, textbox, m))
		but.grid(row=i // 3, column=i % 3, sticky="nsew")

	botFrame.pack(fill='both', expand=True)




	switch_home(homeFrame, monthFrame)
	app.mainloop()