from start import create_initial_database
from new_song import check_duplicate_data, add_pending_files_to_database
from export_db import export_database
from import_db import import_database
from sys import exit
from config import create_project_structure
print("WELCOME TO SONG RECOGNISER")

while True:
    print("Please select your desired option from below:")

    print("0) Exit from this program.")
    print("1) Create project structure")
    print("2) create initial database.")
    print("3) Check new files with database.")
    print("4) Add pending unique files with database")
    print("5) Export the database")
    print("6) Create database from a database file")

    number = int(raw_input("\n\n\nEnter your choice:"))

    dic = {
        0: exit,
        1: create_project_structure,
        2: create_initial_database,
        3: check_duplicate_data,
        4: add_pending_files_to_database,
        5: export_database,
        6: import_database
    }

    dic.get(number, exit)()
