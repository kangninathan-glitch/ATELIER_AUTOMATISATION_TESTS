import sqlite3
import json
from datetime import datetime

DB = "runs.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            success INTEGER,
            failed INTEGER,
            total INTEGER,
            error_rate REAL,
            results TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_run(data):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO runs(date, success, failed, total, error_rate, results)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        data["success"],
        data["failed"],
        data["total"],
        data["error_rate"],
        json.dumps(data["results"])
    ))

    conn.commit()
    conn.close()


def list_runs():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT date, success, failed, total, error_rate FROM runs ORDER BY id DESC LIMIT 10")

    rows = cur.fetchall()

    conn.close()

    return rows
