from config import djv, database_directory


def create_initial_database():
    djv.fingerprint_directory(database_directory, [".mp3"])
    print("Finished saving data to database :)")

