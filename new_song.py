from config import djv, new_song_directory, unique_files, duplicate_files
from dejavu.recognize import FileRecognizer
import os
import shutil
from utils import write_to_excel_file


def check_duplicate_data():
    new_files_url = []
    duplicate_data = []

    for file in os.listdir(new_song_directory):
        if file.endswith(".mp3"):
            new_files_url.append(os.path.join(new_song_directory, file))

    for file in new_files_url:
        song = djv.recognize(FileRecognizer, file)
        if song and song['confidence'] > 1000:
            print song
            current_name = file.split('/')[-1].split('.')[0]
            orig_name = song['song_name']
            duplicate_data.append([current_name, orig_name])
            shutil.move(file, duplicate_files)
        else:
            shutil.move(file, unique_files)

    if duplicate_data:
        write_to_excel_file(duplicate_data)
    else:
        inp = raw_input("Do you want to add unique files to database? y/n:")
        if inp in ['Y', 'y', 'Yes', 'yes', 'YES']:
            djv.fingerprint_directory(unique_files, [".mp3"])
            print("Finished saving new data to database :)")


def add_pending_files_to_database():
    djv.fingerprint_directory(unique_files, [".mp3"])
    print("Finished saving new data to database :)")
