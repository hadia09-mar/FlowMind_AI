import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/flowmind.db",
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