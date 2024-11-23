import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")

    def init_tables(self):
        pass