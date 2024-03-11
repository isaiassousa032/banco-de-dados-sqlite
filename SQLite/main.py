import sqlite3
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE cliente(nome text, idade integer, sex text)")
cursor.execute("INSERT INTO cliente VALUES('cynthia',40,'f'),('pedro',20, 'm')")
cursor.execute("Select * from cliente")
print(cursor.fetchall())
banco.commit()
cursor.close()
banco.close()

'''import os
os.remove('database.db')'''
