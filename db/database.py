import sqlite3
import os
from datetime import datetime

def init_db():
    db_file = 'installation_state.db'
    if not os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS installations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                host TEXT NOT NULL,
                tool TEXT NOT NULL,
                version TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def log_installation(host, tool, version):
    conn = sqlite3.connect('installation_state.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO installations (host, tool, version, date)
        VALUES (?, ?, ?, ?)
    ''', (host, tool, version, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def check_installation(host, tool):
    conn = sqlite3.connect('installation_state.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM installations WHERE host = ? AND tool = ?
    ''', (host, tool))
    result = cursor.fetchone()
    conn.close()
    return result is not None
