import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(10):
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example1{i}@gmail.com", str(random.randint(18,49)), random.randint(100,5000)))
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE f'username{i}' = ?", (500, f'username{i}'))
    # cursor.execute("UPDATE Users SET balance = ? WHERE balance = ?", (500,))
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# Удалите каждую 3ую запись в таблице начиная с 1ой:

connection.commit()
connection.close()