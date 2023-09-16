import os
import time


# recursive
def traverse_directory(path, indent=''):
    for entry in os.scandir(path):
        if entry.is_file():
            row = [indent + '-' + entry.name, str(os.path.getsize(entry.path)) + "b",
                   time.ctime(os.path.getctime(entry.path))]

            print("{:<50} {:<10} {:<10}".format(*row))

        elif entry.is_dir():
            print(indent + '-' + entry.name + os.sep)
            traverse_directory(entry.path, indent + '-')


traverse_directory('../ex7-modules/')
