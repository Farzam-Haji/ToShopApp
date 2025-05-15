from .database import CommonDB, MonthDB

# shared
def fetch_comItems(cdb:CommonDB):
	itstr, itcost = cdb.get_items()
	itlist = itstr.split("/./")
	itlist.pop()
	return itlist, itcost

def fetch_monItems(mdb:MonthDB, month):
	itstr, itcost = mdb.get_items(month)
	itlist = itstr.split("/./")
	itlist.pop()
	return itlist, itcost

def add_comItem(cdb:CommonDB, item):
	itnew = item + "/./"
	cdb.add_item(itnew)

def del_comItem(cdb:CommonDB, item):
	itdel = item + "/./"
	cdb.delete_item(itdel)

def add_comCost(cdb:CommonDB, value):
	val = float(int(value))
	cdb.update_est(val)

def clean_com(cdb:CommonDB):
	cdb.delete_all()

def add_monItem(mdb:MonthDB, month, item):
	itnew = item + "/./"
	mdb.add_item(itnew, month)

def add_comToMon(mdb:MonthDB, month):
	mdb.add_common_items(month)

def add_monCost(mdb:MonthDB, month, value):
	val = float(int(value))
	mdb.update_est(val, month)

def del_monItem(mdb:MonthDB, month, item):
	itdel = item + "/./"
	mdb.delete_item(itdel, month)

def clean_mon(mdb:MonthDB, month):
	mdb.delete_month(month)

# headless logic
def headless_open_common(cdb:CommonDB):
	while True:
		itlist, itcost = fetch_comItems(cdb)
		print("----\tCOMMON\t----\nItems:")
		for i, item in enumerate(itlist):
			print(f"{i+1}. {item}")
		print(f"Cost: {itcost}")
		inp = input("\n'a'to add\n'd'to delete\n'c'to add cost\n'clean'to delete all\n'b'to back:\n=> ")

		if inp == "a":
			newit = input("type new item:\n=> ")
			add_comItem(cdb,newit)
		if inp == "d":
			delIndex = input("index of item you want to delete:\n=> ")
			try:
				ind = int(delIndex)-1
			except ValueError:
				print("bad input")
			else:
				del_comItem(cdb, itlist[ind])
		if inp == "c":
			val = input("type the value:\n=> ")
			add_comCost(cdb, val)
		elif inp == "clean":
			clean_com(cdb)
		elif inp == "b":
			return
		else:
			print("bad input try again")

def headless_open_month(mdb:MonthDB, cdb:CommonDB, month):
	while True:
		itlist, itcost = fetch_monItems(mdb, month)
		print(f"----\tMONTH {month}\t----\nItems:")
		for i, item in enumerate(itlist):
			print(f"{i+1}. {item}")
		print(f"Cost: {itcost}")
		inp = input("\n'a' to add new item\n'ac' to add whole common list\n'c' to add to cost\n'd' to delete one item\n'clean' to delete all\n'oc' to open common menu\n'b' to back\n=> ")

		if inp == 'a':
			newit = input("type your new item:\n=> ")
			add_monItem(mdb, month, newit)
		elif inp == 'ac':
			add_comToMon(mdb, month)
		elif inp == 'c':
			costVal = input("type the value:\n=> ")
			add_monCost(mdb, month, costVal)
		elif inp == "d":
			delIndex = input("type the index of item you wish to remove:\n=> ")
			try:
				ind = int(delIndex)-1
			except ValueError:
				print("bad input try again")
			else:
				del_monItem(mdb, month, itlist[ind])
		elif inp == "clean":
			clean_mon(mdb, month)
		elif inp =="oc":
			return headless_open_common(cdb)
		elif inp == 'b':
			return
		else:
			print("bad input. try again")

def start_logic(mdb:MonthDB, cdb:CommonDB):
	while True:
		inp = input("select 1 to 12 for months\nor 'c' for common\nand 'e' for exit:\n=> ")
		try:
			inp = int(inp)
		except ValueError:
			if inp == "c":
				headless_open_common(cdb)
				pass
			elif inp == "e":
				break
			else:
				print("bad input try again")
		else:
			if 0 < inp <= 12:
				headless_open_month(mdb, cdb, inp)
			else:
				print("bad input try again")
