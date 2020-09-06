import sys, os, shutil
from datetime import datetime

def backup(file):
    [file_name, file_type] = os.path.splitext(f"{file}")
    backup_dir = create_backup_dir(file_name)

    backup_file = copy_file(file, backup_dir)
    date_time = datetime.now().strftime('%d-%m-%Y %H.%M.%S')
    new_backup_file = os.path.join(backup_dir, f"{file_name} - Backup ({date_time}){file_type}")

    try:
        os.rename(backup_file, new_backup_file)
    except OSError as err:
        print(f"Backup file could not be renamed!")
        raise err
    else:
        print("Backup file was renamed!")
        print("====================")

    print(f"Backup of file {file} completed!")
        

def copy_file(file, dir):
    try:
        shutil.copy(file, dir)
    except OSError as err:
        print(f"File could not be copied!")
        raise err

    else:
        print("File was copied!")
        print("====================")
        return os.path.join(dir, file)

def create_backup_dir(path_name):
    path = path_name + " - Backup"

    #Check if the backup directory already exists
    if os.path.isdir(f'{path}'):
        print(f"Backup directory {path} is already existing!")
        print("====================")
        return path

    try:
        os.mkdir(path)
    except OSError as err:
        print(f"Creation of the backup directory {path} failed!")
        raise err
    else:
        print(f"Creation of the backup directory {path} succeeded!")
        print("====================")
        return path


if __name__ == "__main__":
     # When this script is called, the argument structure should be: backer.py FILE_TO_BACKUP
    # If no file name or extra arguments were provided
    if len(sys.argv) != 2:
        raise ValueError("Invalid number of arguments provided!")

    backup_file = sys.argv[1]
    # Check if the provided file name is a file
    if not os.path.isfile(f"./{backup_file}"):
        raise ValueError("No file with the provided name was found in the directory!")

    backup(backup_file)

        