import os
from subprocess import call
from config import database_import_directory, config


def import_database():
    user = config['database']['user']
    passwd = config['database']['passwd']
    database = config['database']['db']

    file_path = ""
    for file_name in os.listdir(database_import_directory):
        if file_name.endswith(".sql"):
            file_path = "{}/{}".format(database_import_directory, file_name)

    command = "mysql -u {} {} < {}".format(user, database, file_path)
    call(command, shell=True)
