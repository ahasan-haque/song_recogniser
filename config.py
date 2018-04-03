from dejavu import Dejavu
import MySQLdb
import os

config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "",
         "db": "dejavu",
     },
     "database_type" : "mysql",
     "fingerprint_limit" : None
 }


def create_database():
    db1 = MySQLdb.connect(host="localhost", user="root", passwd="")
    cursor = db1.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS dejavu;"
    cursor.execute(sql)
    return Dejavu(config)


djv = create_database()

project_root_directory = "{}/song_recogniser".format(os.path.expanduser('~'))
database_directory = "{}/initial_database".format(project_root_directory)
new_song_directory = "{}/new_song".format(project_root_directory)
database_export_directory = "{}/exported_database_file".format(project_root_directory)
database_import_directory = "{}/importable_database_file".format(project_root_directory)

unique_files = "{}/unique/".format(project_root_directory)
duplicate_files = "{}/duplicate/".format(project_root_directory)
excel_files = "{}/excels".format(project_root_directory)


def create_project_structure():
    for path in [database_directory, unique_files, duplicate_files,excel_files,
                 new_song_directory, database_export_directory, database_import_directory]:
        if not os.path.exists(path):
            os.makedirs(path)