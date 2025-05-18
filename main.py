from backend.database import DB, MonthDB, CommonDB
from backend.logic import start_logic
from gui.tkinter_gui import App


if __name__ == "__main__" :

	baseDB = DB()
	baseDB.init_db()

	monthDB = MonthDB()
	commonDB = CommonDB()

	# start_logic(monthDB, commonDB)
	app = App(monthDB, commonDB)
	app.mainloop()