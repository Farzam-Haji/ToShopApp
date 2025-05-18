# from os import replace
# import sqlite3
# from pathlib import Path

# DB_PATH = "db/toShopApp.db"

# months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

# def init_db():
#     Path("db").mkdir(exist_ok=True)
    
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS months (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             month_order INTEGER NOT NULL,
#             items TEXT DEFAULT "",
#             est_cost INTEGER DEFAULT 0
#         )
#     ''')
#     c.execute("SELECT COUNT(*) FROM months")
#     count = c.fetchone()[0]
#     if count == 0:
#         for i, month_name in enumerate(months):
#             c.execute("INSERT INTO months(name, month_order) VALUES (?, ?)", (month_name, i+1))
    
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS common (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             items TEXT DEFAULT "",
#             est_cost INTEGER DEFAULT 0
#             )
#         ''')
#     c.execute("SELECT COUNT(*) FORM common")
#     count = c.fetchone()[0]
#     if count == 0:
#         c.execute("INSERT INTO common VALUES (items, est_cost)", ("", 0))
#     conn.commit()
#     conn.close()


# def delete_all_items(monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("UPDATE months SET items = ?, est_cost = ? WHERE month_order = ?", ("", 0, monthINT))
#     conn.commit()
#     conn.close()

# def delete_all_common():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("UPDATE common SET items = ?, est_cost = ?", ("", 0))
#     conn.commit()
#     conn.close()

# def get_items(monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT (items, est_cost) FROM months WHERE month_order = ?", (monthINT, ))
#     month_items = c.fetchall()
#     conn.commit()
#     conn.close()
#     return month_items

# def get_common_items():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT (items, est_cost) FROM common")
#     common_items = c.fetchone()
#     conn.close()
#     return common_items

# def add_common_items(monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT items, est_cost FROM common")
#     (cItems, cCost) = c.fetchone()
#     c.execute("SELECT items, est_cost FROM months WHERE month_order = ?", (monthINT, ))
#     mItems, mCost = c.fetchone()
#     mItems = mItems + cItems
#     mCost += cCost  
#     c.execute("UPDATE months SET items = ?, est_cost = ? WHERE month_order = ?", (mItems, mCost, monthINT))
#     conn.commit()
#     conn.close()

# def add_to_common_items(newItems):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT items FROM common")
#     current_items = c.fetchone()[0]
#     c.execute("UPDATE common SET items = ?", (current_items + newItems, ))
#     conn.commit()
#     conn.close()

# def delete_one_common_item(item):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT items FROM common")
#     current_items = c.fetchone()[0]
#     current_items = current_items.replace(item, "", 1)
#     c.execute("UPDATE common SET items = ?", (current_items, ))
#     conn.commit()
#     conn.close()

# def set_est(value, isCommon, *monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     if isCommon:
#         c.execute("SELECT est_cost FROM common")
#         current_est = c.fetchone()[0]
#         current_est += value
#         c.execute("UPDATE common SET est_cost = ?", (current_est, ))
#     elif not isCommon:
#         c.execute("SELECT est_cost FROM months WHERE month_order = ?", (monthINT, ))
#         current_est = c.fetchone()[0]
#         current_est += value
#         c.execute("UPDATE months SET est_cost = ? WHERE month_order = ?", (current_est, monthINT))
#     conn.commit()
#     conn.close()

# def add_to_month_items(newItems, monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT items FROM months WHERE month_order = ?", (monthINT, ))
#     current_items = c.fetchone()[0]
#     current_items += newItems
#     c.execute("UPDATE months SET items = ? WHERE month_order = ?", (current_items, monthINT))
#     conn.commit()
#     conn.close()

# def delete_one_month_item(item, monthINT):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT items FROM months WHERE month_order = ?", (monthINT, ))
#     current_items = c.fetchone()[0]
#     current_items = current_items.replace(item, "", 1)
#     c.execute("UPDATE months SET items = ? WHERE month_order = ?", (current_items, monthINT))
#     conn.commit()
#     conn.close()

#-------------------------------------
import sqlite3
from pathlib import Path

DB_PATH = "db/toShopApp.db"

class DB:
    def __init__(self):
        Path("db").mkdir(exist_ok=True)
        self.db_path = DB_PATH

    def connect(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.connect() as conn:
            c = conn.cursor()
            # month table
            c.execute('''
                CREATE TABLE IF NOT EXISTS months (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    morder INTEGER NOT NULL,
                    items TEXT DEFAULT "",
                    estcost INTEGER DEFAULT 0
                    )
                ''')
            c.execute("SELECT COUNT(*) FROM months")
            if c.fetchone()[0] == 0:
                months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
                for i, mname in enumerate(months):
                    c.execute("INSERT INTO months(name, morder) VALUES (?, ?)", (mname, i+1))

            # common table
            c.execute('''
                CREATE TABLE IF NOT EXISTS common (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    items TEXT DEFAULT "",
                    estcost INTEGER DEFAULT 0
                    )
                ''')
            c.execute("SELECT COUNT(*) FROM common")
            if c.fetchone()[0] == 0:
                c.execute("INSERT INTO common(items, estcost) VALUES (?, ?)", ("", 0))

            conn.commit()

class CommonDB(DB):
    def get_items(self) -> tuple[str, int]:
        with self.connect() as conn:
            return conn.execute("SELECT items, estcost FROM common").fetchone()

    def delete_all(self):
        with self.connect() as conn:
            conn.execute("UPDATE common SET items = ?, estcost = ?", ("", 0))
            conn.commit()

    def add_item(self, new_item):
        with self.connect() as conn:
            current_items = conn.execute("SELECT items FROM common").fetchone()[0]
            conn.execute("UPDATE common SET items = ?", (current_items + new_item,))
            conn.commit()

    def delete_item(self, item):
        with self.connect() as conn:
            current_items = conn.execute("SELECT items FROM common").fetchone()[0]
            current_items = current_items.replace(item, "", 1)
            conn.execute("UPDATE common SET items = ?", (current_items,))
            conn.commit()

    def update_est(self, value):
        with self.connect() as conn:
            current_cost = conn.execute("SELECT estcost FROM common").fetchone()[0]
            conn.execute("UPDATE common SET estcost = ?", (current_cost + value,))
            conn.commit()

class MonthDB(DB):
    def get_items(self, month:int) -> tuple[str, int]:
        with self.connect() as conn:
            return conn.execute("SELECT items, estcost FROM months WHERE morder = ?", (month,)).fetchone()

    def delete_month(self, month:int):
        with self.connect() as conn:
            conn.execute("UPDATE months SET items = ?, estcost = ? WHERE morder = ?", ("", 0, month))
            conn.commit()

    def add_item(self, new_item, month:int):
        with self.connect() as conn:
            current_items = conn.execute("SELECT items FROM months WHERE morder = ?", (month,)).fetchone()[0]
            conn.execute("UPDATE months SET items = ? WHERE morder = ?", (current_items + new_item, month))
            conn.commit()

    def delete_item(self, item, month:int):
        with self.connect() as conn:
            current_items = conn.execute("SELECT items FROM months WHERE morder = ?", (month,)).fetchone()[0]
            current_items = current_items.replace(item, "", 1)
            conn.execute("UPDATE months SET items = ? WHERE morder = ?", (current_items, month))
            conn.commit()

    def add_common_items(self, month:int):
        with self.connect() as conn:
            (month_items, month_cost) = conn.execute("SELECT items, estcost FROM months WHERE morder = ?", (month,)).fetchone()
            (common_item, common_cost) = conn.execute("SELECT items, estcost FROM common").fetchone()
            conn.execute("UPDATE months SET items = ?, estcost = ? WHERE morder = ?", (common_item + month_items, month_cost + common_cost, month))
            conn.commit()

    def update_est(self, value, month:int):
        with self.connect() as conn:
            current_cost = conn.execute("SELECT estcost FROM months WHERE morder = ?", (month,)).fetchone()[0]
            conn.execute("UPDATE months SET estcost = ? WHERE morder = ?", (current_cost + value, month))
            conn.commit()

    def get_months_names(self) -> list[str]:
        with self.connect() as conn:
            fetchlist = conn.execute("SELECT name FROM months").fetchall()
            return [x[0] for x in fetchlist]
