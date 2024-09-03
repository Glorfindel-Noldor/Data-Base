import sqlite3

CONN = sqlite3.connect("src/instance/database.db")
CURSOR = CONN.cursor()

