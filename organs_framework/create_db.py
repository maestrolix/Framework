import sqlite3

connection = sqlite3.connect('../project.sqlite')
cursor = connection.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cursor.executescript(text)
cursor.close()
connection.close()
print("Данные успешно занесены")
