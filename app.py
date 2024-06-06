'''Docstring This is a python and sql code that has the information of Movie database
By Aaron Choi on 24.05.2024'''


#imports
import sqlite3


#contants and variables
database = ("Movie_database.db")


#function
def print_all_Movie_name():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie_name from Movie;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name")
    for Movie in results:
        print(f"{Movie[0]}")
    #loop finished here
    db.close()


def print_all_Genre_name():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT name from Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Genre_name")
    for Movie in results:
        print(f"{Movie[0]}")
    #loop finished here
    db.close()


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
    sql = "SELECT Movie.Movie_name,Movie.Rating, Movie.Release_date, Genre.name FROM Movie JOIN Genre ON Movie.Genre_id=Genre.Genre_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                             Rating    Release_date   Genre_name")
    for Movie in results:
        print(f"{Movie[0]:<55}{Movie[1]:<10}{Movie[2]:<15}{Movie[3]:<1}")
    #loop finished here
    db.close()

#main code
while True:
    user_input = input("\nWhat would you like to do in this Movie Database?\nEnter '1' to see all information\nEnter '2' to sort the data\n")
    if user_input == "1":
        user_input_information = input("What information would you like to see?\nEnter '1' to see all Movie name\nEnter '2' to see all Genre name\nEnter '3' to see all Movie database\nEnter '4' to see allMovie and Genre database\nEnter '4' to Exit the page\n")
        if user_input_information == '1':
            print_all_Movie_name()
        elif user_input_information == '2':
            print_all_Genre_name()