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
    sql = "SELECT ID, Movie_name from Movie;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        Movie_name")
    for Movie in results:
        print(f"{Movie[0]:<10}{Movie[1]}")
    #loop finished here
    db.close()


def print_all_Genre_name():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Genre_id, name from Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        Genre_name")
    for Movie in results:
        print(f"{Movie[0]:<10}{Movie[1]}")
    #loop finished here
    db.close()


def print_all_film():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie_name, Rating, Release_date from Movie;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date")
    for Movie in results:
        print(f"{Movie[0]:<53}{Movie[1]:<10}{Movie[2]:<16}")
    #loop finished here
    db.close()


def print_all_film_sorted_by_Rating():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie_name, Rating, Release_date from Movie ORDER BY Movie.Rating DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date")
    for Movie in results:
        print(f"{Movie[0]:<53}{Movie[1]:<10}{Movie[2]:<16}")
    #loop finished here
    db.close()


def print_all_film_sorted_by_Movie_name():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie_name, Rating, Release_date from Movie ORDER BY Movie.Movie_name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date")
    for Movie in results:
        print(f"{Movie[0]:<53}{Movie[1]:<10}{Movie[2]:<16}")
    #loop finished here
    db.close()


def print_all_film_sorted_by_Release_date():
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = "SELECT Movie_name, Rating, Release_date from Movie ORDER BY Movie.Release_date DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Movie_name                                           Rating    Release_date")
    for Movie in results:
        print(f"{Movie[0]:<53}{Movie[1]:<10}{Movie[2]:<16}")
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
    user_input = input("\nWhat would you like to do in this Movie Database?\nEnter '1' to see all information\nEnter '2' to sort the data\nEnter '3' to see the specific data\nEnter '4' to Exit the page\n")
    if user_input == "1":
        user_input_information = input("What information would you like to see?\nEnter '1' to see all Movie name\nEnter '2' to see all Genre name\nEnter '3' to see all Movie database\nEnter '4' to see all Movie and Genre database\nEnter '5' to Exit the page\n")
        if user_input_information == '1':
            print_all_Movie_name()
        elif user_input_information == '2':
            print_all_Genre_name()
        elif user_input_information == "3":
            print_all_film()
        elif user_input_information == "4":
            print_all_film_joint_with_Genre()
        elif user_input_information == "5":
            continue
        else:
            print("That is not a vailid option")
    elif user_input == "2":
        user_input_sort = input("What data would you like to sort by?\nEnter '1' to sort by Movie name\nEnter '2' to sort by Rating\nEnter '3' to sort by Release date\nEnter '4' to Exit the page\n")
        if user_input_sort == "1":
            print_all_film_sorted_by_Movie_name()
        elif user_input_sort == "2":
            print_all_film_sorted_by_Rating()
        elif user_input_sort == "3":
            print_all_film_sorted_by_Release_date()
        elif user_input_sort == '4':
            continue
        else:
            print("That is not a valid option")
    elif user_input == '3':
        user_input_specific = input("What data would you like to specificly see?\nEnter '1' to see all Movie with a Rating on 8\nEnter '2' to see all Movie with a Rating on 9\nEnter '3' to see all Movie that is made before the year 2000\nEnter '4' to see all Movie that is made in betweeen the year 2000 to 2010\nEnter '5' to see all Movie that is made in between the year 2010 ro 2020\n")
    elif user_input == "4":
        print("Goodbye")
        break
    else:
        print("That is not a valid option")