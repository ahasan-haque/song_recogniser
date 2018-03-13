from subprocess import call
from config import database_export_directory, config


def export_database():
    user = config['database']['user']
    passwd = config['database']['passwd']
    database = config['database']['db']
    path = "{}/db.sql".format(database_export_directory)
    command = "mysqldump -u {} -p{} {} > {}".format(user, passwd, database, path)
    call(command, shell=True)

