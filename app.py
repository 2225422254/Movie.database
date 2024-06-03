'''Docstring This is a python and sql code that has the information of Movie database
By Aaron Choi on 24.05.2024'''


#imports
import sqlite3


#contants and variables
database = ("Movie_database.db")




#function
def print_all_film():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT * from Movie;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date    Genre_id")
    for Movie in results:
        print(f"{Movie[1]:<53}{Movie[2]:<10}{Movie[3]:<16}{Movie[4]:<4}")
    #loop finished here
    db.close()


def print_all_film_sorted_by_Rating():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT * from Movie ORDER BY Movie.Rating DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date    Genre_id")
    for Movie in results:
        print(f"{Movie[1]:<53}{Movie[2]:<10}{Movie[3]:<16}{Movie[4]:<4}")
    #loop finished here
    db.close()


def print_all_film_sorted_by_Release_date():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT * from Movie ORDER BY Movie.Release_date DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date    Genre_id")
    for Movie in results:
        print(f"{Movie[1]:<53}{Movie[2]:<10}{Movie[3]:<16}{Movie[4]:<4}")
    #loop finished here
    db.close()


def print_all_film_joint_with_Genre():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie.ID, Movie.Movie_name, Movie.Release_date, Genre.name FROM Movie JOIN Genre ON Movie.Genre_id=Genre.Genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date    Genre_id")
    for Movie in results:
        print(f"{Movie[1]:<53}{Movie[2]:<10}{Movie[3]:<16}{Movie[4]:<4}")
    #loop finished here
    db.close()

#main code
while True:
    user_input = input("\nWhat would you like to do.\n1.Print all film\n2.Exit\n")
    if user_input == "1":
        print_all_film()
    elif user_input == "2":
        break
    elif user_input == "3":
        print_all_film_sorted_by_Rating()
    elif user_input == "4":
        print_all_film_sorted_by_Release_date()
    elif user_input == "5":
        print_all_film_joint_with_Genre()
    else:
        print("That was not an option\n")