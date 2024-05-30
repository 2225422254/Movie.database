'''Docstring This is a python and sql code that hasthe information of Movie database
By Aaron Choi on 24.05.2024'''

import sqlite3

#containsand variable
database = "Movie_database.db"


#function
def print_all_


#Main code
db = sqlite3.connect("database")
cursor= db.cursor()
sql = "SELECT * from Movie;"
cursor.execute(sql)
results = cursor.fetchall
print(results)
db.close()