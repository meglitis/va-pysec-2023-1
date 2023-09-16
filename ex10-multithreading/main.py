import os
import threading


# meaningful example could be some process where multithreading is beneficial - time-consuming
# calculations (multiple cpu threads) or waiting for resources (iowait).

# I'll try to implement some sort of du -s command based on previous exercise's code
# I'll work exclusively in this repository's home dir to skip safeguard creation

# Intentionally left debugging statements

def traverse_directory(path):
    # print(path)
    global size # no locking implemented
    for entry in os.scandir(path):
        if entry.is_file():
            size += os.path.getsize(entry.path)
            # print(size)
        elif entry.is_dir():
            thread = threading.Thread(target=traverse_directory, args=(entry.path,))
            thread.start()
            thread.join()


size = 0
traverse_directory('..')
print(size)
