from backend.database import DB, MonthDB, CommonDB
from backend.logic import start_logic
from gui.tkinter_gui import start_gui


if __name__ == "__main__" :

	baseDB = DB()
	baseDB.init_db()

	monthDB = MonthDB()
	commonDB = CommonDB()

	# start_logic(monthDB, commonDB)
	start_gui(monthDB)