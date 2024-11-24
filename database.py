import sqlite3

from bcrypt import hashpw, checkpw, gensalt


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")

    def init_tables(self):
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARYKEY AUTO_INCREMENT,
            email varchar(255) NOT NULL UNIQUE,
            hash_password varchar(255) NOT NULL
        )
        """)
        self.connection.commit()

    def reg_user(self, data):
        email = data.email
        hash_password = hashpw(data.password.encode("utf-8"), gensalt(4)).decode("utf-8")
        self.connection.execute(f"INSERT INTO users (email, hash_password) VALUES ('{email}', '{hash_password}')")
        self.connection.commit()

    def log_user(self, data):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT hash_password FROM users WHERE email = '{data.email}'")
        return checkpw(data.password.encode("utf-8"), cursor.fetchone()[0].encode("utf-8"))
