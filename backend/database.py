import sqlite3
from pathlib import Path

DB_PATH = "db/toShopApp.db"

months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

def init_db():
    Path("db").mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS months (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            month_order INTEGER NOT NULL,
            items TEXT DEFAULT "",
            est_cost INTEGER DEFAULT 0
        )
    ''')
    c.execute("SELECT COUNT(*) FROM months")
    count = c.fetchone()[0]
    if count == 0:
        for i, month_name in enumerate(months):
            c.execute("INSERT INTO months(name, month_order) VALUES (?, ?)", (month_name, i+1))
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS common (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            items TEXT DEFAULT "",
            est_cost INTEGER DEFAULT 0
            )
        ''')
    c.execute("SELECT COUNT(*) FORM common")
    count = c.fetchone()[0]
    if count == 0:
        c.execute("INSERT INTO common VALUES (items, est_cost)", ("", 0))
    conn.commit()
    conn.close()


def delete_all_items(monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE months SET items = ?, est_cost = ? WHERE month_order = ?", ("", 0, monthINT))
    conn.commit()
    conn.close()

def delete_all_common():
    onn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE common SET items = ?, est_cost = ?", ("", 0))
    conn.commit()
    conn.close()

def get_items(monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT (items, est_cost) FROM months WHERE month_order = ?", (monthINT, ))
    month_items = c.fetchall()
    conn.execute()
    return month_items

def get_common_items():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT (items, est_cost) FROM common")
    common_items = c.fetchone()
    conn.close()
    return common_items

def add_common_items(monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT items, est_cost FROM common")
    (cItems, cCost) = c.fetchone()
    c.execute("SELECT items, est_cost FROM months WHERE month_order = ?", (monthINT, ))
    mItems, mCost = c.fetchone()
    mItems = mItems + cItems
    mCost += cCost  
    c.execute("UPDATE months SET items = ?, est_cost = ? WHERE month_order = ?", (mItems, mCost, monthINT))
    conn.commit()
    conn.close()

def add_to_common_items(newItems):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT items FROM common")
    current_items = c.fetchone()[0]
    c.execute("UPDATE common SET items = ?", (current_items + newItems, ))
    conn.commit()
    conn.close()

def delete_one_common_item(item):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT items FROM common")
    current_items = c.fetchone()[0]
    current_items = current_items.replace(item, "", 1)
    c.execute("UPDATE common SET items = ?", (current_items, ))
    conn.commit()
    conn.close()

def set_est(value, isCommon, *monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if isCommon:
        c.execute("SELECT est_cost FROM common")
        current_est = c.fetchone()[0]
        current_est += value
        c.execute("UPDATE common SET est_cost = ?", (current_est, ))
    elif !isCommon:
        c.execute("SELECT est_cost FROM months WHERE month_order = ?", (monthINT, ))
        current_est = c.fetchone()[0]
        current_est += value
        c.execute("UPDATE months SET est_cost = ? WHERE month_order = ?", (current_est, monthINT))
    conn.commit()
    conn.close()

def add_to_month_items(newItems, monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT items FROM months WHERE month_order = ?", (monthINT, ))
    current_items = c.fetchone()[0]
    current_items += newItems
    c.execute("UPDATE months SET items = ? WHERE month_order = ?", (current_items, monthINT))
    conn.commit()
    conn.close()

def delete_one_month_item(item, monthINT):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT items FROM months WHERE month_order = ?", (monthINT, ))
    current_items = c.fetchone()[0]
    current_items = current_items.replace(item, "", 1)
    c.execute("UPDATE months SET items = ? WHERE month_order = ?", (current_items, monthINT))
    conn.commit()
    conn.close()

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
conn.commit()
conn.close()