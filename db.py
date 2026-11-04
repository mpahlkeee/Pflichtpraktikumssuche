import sqlite3

db_con  = sqlite3.connect('database.db')

sql= "create table todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)"

db_con.execute(sql)

sql= "Select"