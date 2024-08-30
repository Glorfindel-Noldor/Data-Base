import sqlite3

CONN = sqlite3.connect("database.db", check_same_thread=False)
CURSOR = CONN.cursor()
