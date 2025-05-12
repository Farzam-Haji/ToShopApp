import sqlite3
from pathlib import Path

DB_PATH = "db/app.db"

def init_db():
    Path("db").mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placeholder TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
