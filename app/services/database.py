import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "database" / "flowmind.db"

class Database:

    def __init__(self):

        # Folder agar na ho to bana do
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(
            str(DB_PATH),
            check_same_thread=False,
        )

        self.cursor = self.connection.cursor()

    def execute(self, query, values=()):

        self.cursor.execute(query, values)
        self.connection.commit()

    def fetchone(self):

        return self.cursor.fetchone()

    def fetchall(self):

        return self.cursor.fetchall()


db = Database()