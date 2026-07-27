import sqlite3
from pathlib import Path

DB_PATH = Path("data/memory.db")

DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class Memory:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS memory(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT
        )
        """)
        self.conn.commit()

    def remember(self, key, value):
        self.conn.execute(
            """
            INSERT INTO memory(key,value)
            VALUES(?,?)
            ON CONFLICT(key)
            DO UPDATE SET value=excluded.value
            """,
            (key, value),
        )
        self.conn.commit()

    def recall(self, key):
        row = self.conn.execute(
            "SELECT value FROM memory WHERE key=?",
            (key,),
        ).fetchone()

        if row:
            return row["value"]

        return None

    def all(self):
        rows = self.conn.execute(
            "SELECT key,value FROM memory ORDER BY key"
        ).fetchall()

        return [
            dict(row)
            for row in rows
        ]
