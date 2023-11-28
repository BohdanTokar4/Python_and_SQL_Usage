import sqlite3 as sq

with sq.connect("database.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS user")
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex TEXT NOT NULL DEFAULT "Male",
        age INTEGER,
        score INTEGER
        )""")

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    for result in cur:
        print(result)